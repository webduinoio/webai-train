FROM ubuntu:18.04

MAINTAINER Webduino service@webduino.io

RUN apt-get update -qq\
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN DEBIAN_FRONTEND=noninteractive \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
        zip \
        unzip \
        git \
        wget \
        python3 \
        python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install nvidia-ml-py3>=7.352.0 \
    && pip3 install tensorflow>=2.3.1 \
    && pip3 install matplotlib>=3.2.1 \
    && pip3 install scikit-learn>=0.23.2 \
    && pip3 install imgaug>=0.4.0 \
    && pip3 install imutils>=0.5.3 \
    && pip3 install opencv-python>=4.2.0 \
    && echo "setup complete, now clean" \
    && DEBIAN_FRONTEND=noninteractive apt-get autoremove -y --purge \
    && DEBIAN_FRONTEND=noninteractive apt-get clean \
    && rm -rf /tmp \
    && mkdir /tmp \
    && rm /=* \
    && echo "build complete"