FROM python:3.6

RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y
RUN python -m pip install --upgrade pip
RUN pip install jupyterlab
RUN pip install opencv-python
RUN pip install opencv-contrib-python
RUN pip install matplotlib
RUN pip install scikit-image
RUN pip install imutils
RUN pip install dlib==19.8.1

CMD [ "jupyterlab" ]
