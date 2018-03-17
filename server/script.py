from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import base64
import os

hostName = "0.0.0.0"
hostPort = 9000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        print(content_len)
        data = self.rfile.read(content_len)

        todecode = data[22:]
        print(todecode)
        encoded = base64.b64decode(todecode)

        directory = "img"
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)

        filename = os.path.join(directory, "time"+time.strftime("%Y%m%d-%H%M%S")+".png")
        file = open(filename, "wb+")
        file.write(encoded)
        file.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes("ok", "utf-8"))


if __name__ == "__main__":
    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
