FROM ubuntu:16.04

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        busybox \
        strace \
        telnet \
        net-tools \
        iputils-ping \
        mtr \
        ffmpeg && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    useradd -m developer

USER developer

COPY ./ffserver.conf /home/developer/

WORKDIR /home/developer/

CMD ffserver -d -f ffserver.conf
