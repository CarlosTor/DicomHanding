FROM ubuntu:20.04

RUN apt update

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install python3.8 python3-pip python3-opencv -y

WORKDIR /workspace

COPY . .

RUN pip install -r requirements/requirements.txt
