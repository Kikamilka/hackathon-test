from subprocess import call
import math
import json
import statistics

from plyfile import PlyData

class Processing:
    def make3D(self):
        call(["mkdir", "data"])
        call(["mkdir", "data/images"])
        call(["cp", "./imgages", "./data/images"])
        call(["docker", "run", "-it", "-v", "./data:/data", "sfm"])

    def prune(self):

    def normalize(self):
        plydata = PlyData.read("data/depthmaps/merged.ply")
        x = statistics.mean(map(lambda p: p.x, plydata.elements))
        y = statistics.mean(map(lambda p: p.y, plydata.elements))
        z = statistics.mean(map(lambda p: p.z, plydata.elements))

        for element in plydata.elements:
            element.x = element.x - x
            element.y = element.y - y
            element.z = element.z - z

        PlyData(plydata).write("normalized.ply")

    def calculate(self):
        def dist(a,b):
            math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

        filename = (".human/body.bin")
        file = open(filename, "r")
        body = json.loads(file.read())

        points = body[3].union(body[4])
        ymax = sorted(points, lambda p: p.y, reverse=False)[0]
        ymin = sorted(points, lambda p: p.y, reverse=True)[0]
        xmax = sorted(points, lambda p: p.x, reverse=False)[0]
        xmin = sorted(points, lambda p: p.x, reverse=True)[0]

        waist = (3.14/2.82)*(dist(ymax, xmin) + dist(ymax, xmax) + dist(ymin, xmin) + dist(ymin, xmax))

        return {waist: waist}

    def humanize(self):

    def run(self):
        self.make3D()
        self.prune()
        self.normalize()
        self.humanize()
        self.calculate()


