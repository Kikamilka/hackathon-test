FROM paulinus/opensfm-docker-base:opencv3

RUN pip install opencv-python

WORKDIR /opt
RUN git clone https://github.com/mapillary/OpenSfM.git
WORKDIR /opt/OpenSfM/

RUN pip install virtualenv
RUN virtualenv env
RUN pip install -r requirements.txt
RUN python setup.py build

ENTRYPOINT ["bin/opensfm_run_all","/data/images"]





