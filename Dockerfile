# I recommend setting the CUDA image version to the same one supported by your GPU(s).
FROM nvidia/cuda:12.2.0-devel-ubuntu20.04

ENV PYTHONUNBUFFERED True
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Etc/GMT

WORKDIR /vid-tinyllama
COPY . .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends python3 python3-pip
RUN apt-get install -y gcc build-essential cmake
RUN pip install -r requirements.txt

# Comment the below line to *not* install the nano text editor for debugging.
RUN apt-get update && apt-get install -y nano

WORKDIR /vid-tinyllama/src