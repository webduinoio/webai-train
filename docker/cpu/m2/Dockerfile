FROM armswdev/tensorflow-arm-neoverse:latest

USER root

RUN apt-get update -qq\
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update &&\
    apt-get -y install curl &&\
    curl -sL https://deb.nodesource.com/setup_10.x | bash - &&\
    apt-get -y install nodejs &&\
    ln -s /usr/bin/nodejs /usr/local/bin/node


# Patch
RUN pip install scikit-learn && pip install tensorflowjs

WORKDIR /media/shared/

# Install puppeteer so it's available in the container.
RUN npm install
RUN npm i pm2 -g
RUN NODE_ENV=production npm install

CMD ["sh","app.sh"]