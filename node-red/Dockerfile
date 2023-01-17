FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04 as base

# Install Node
RUN apt-get update &&\
    apt-get -y install curl &&\
    curl -sL https://deb.nodesource.com/setup_16.x | bash - &&\
    apt-get -y install nodejs &&\
    ln -s /usr/bin/nodejs /usr/local/bin/node

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq \
        zip \
        unzip \
        git \
        wget \
        build-essential \
        python3 \
        python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install nvidia-ml-py3>=7.352.0 \
    && pip3 install tensorflow==2.10.0 \
    && pip3 install matplotlib>=3.2.1 \
    && pip3 install scikit-learn>=0.23.2 \
    && pip3 install imgaug>=0.4.0 \
    && pip3 install imutils>=0.5.3 \
    && pip3 install opencv-python>=4.2.0 \
    && pip3 install tensorflowjs \
    && pip3 install opencv-python-headless \
    && pip3 install numpy==1.23.5 \
    && echo "setup complete, now clean" \
    && DEBIAN_FRONTEND=noninteractive apt-get autoremove -y --purge \
    && DEBIAN_FRONTEND=noninteractive apt-get clean \
    && rm -rf /tmp \
    && mkdir /tmp \
    && rm /=* \
    && echo "build complete"

RUN apt-get update \
    && apt-get install -y openssh-server \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


COPY scripts/*.sh /tmp/

RUN set -ex && \
    apt-get update && \
    apt-get install -y \
        openssl \
        openssh-client \
        ca-certificates && \
    mkdir -p /usr/src/node-red /data


WORKDIR /usr/src/node-red

COPY known_hosts.sh .
RUN ./known_hosts.sh /etc/ssh/ssh_known_hosts && rm /usr/src/node-red/known_hosts.sh
RUN echo "PubkeyAcceptedKeyTypes +ssh-rsa" >> /etc/ssh/ssh_config

COPY package.json .
COPY flows.json /data
COPY scripts/entrypoint.sh .

RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production
RUN npm config set cache /data/.npm --global 
RUN npm config set python `which python3` --global

# Env variables
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu/:/usr/local/cuda-11.7/targets/x86_64-linux/:/usr/local/cuda/lib:$LD_LIBRARY_PATH \
    NODE_RED_VERSION=$NODE_RED_VERSION \
    NODE_PATH=/usr/src/node-red/node_modules:/data/node_modules \
    PATH=/usr/src/node-red/node_modules/.bin:${PATH} \
    FLOWS=flows.json

EXPOSE 1880


ENTRYPOINT ["./entrypoint.sh"]
