FROM ubuntu:14.04

RUN pip install tensorflow
RUN apt-get install python-pil python-numpy
RUN pip install jupyter
RUN pip install matplotlib pyyaml easydict cython munkres

WORKDIR /opt
RUN git clone https://github.com/eldar/pose-tensorflow.git
WORKDIR /opt/pose-tensorflow

RUN download_models.sh
ENTRYPOINT ["python", "demo/singleperson.py", "normalize.ply"]
