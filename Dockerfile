FROM ubuntu:18.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python-pip
RUN pip install -U pip

RUN rm /usr/lib/python2.7/lib-dynload/_hashlib.x86_64-linux-gnu.so

WORKDIR /build
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
