FROM ubuntu:16.04

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        busybox \
        telnet \
        net-tools \
        iputils-ping \
        android-tools-adb && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd -m developer

COPY ./start_adb /home/developer/start_adb
COPY ./fb-adb /usr/local/bin/fb-adb
RUN chown -R developer.developer /home/developer

USER developer

CMD sh /home/developer/start_adb
