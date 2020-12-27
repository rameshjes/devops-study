FROM python:3.8-buster
MAINTAINER Ramesh Kumar "rameshkjes@gmail.com"

RUN apt-get update -y

RUN apt-get install -y --fix-missing python3-pip python3-dev build-essential
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN ln -sf /usr/bin/pip3 /usr/bin/pip
RUN apt-get install -y curl
RUN apt-get install -y git

WORKDIR /home/app

COPY . /home/app
RUN pip install -r requirements.txt