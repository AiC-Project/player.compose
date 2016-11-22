FROM ubuntu:16.04

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        busybox \
        strace \
        telnet \
        net-tools \
        iputils-ping \
        mtr \
        xserver-xorg-core \
        xserver-xorg-video-dummy \
        x11-xserver-utils \
        python-pkg-resources \
        oathtool \
        websockify \
        x11vnc && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    echo "allowed_users=anybody" > /etc/X11/Xwrapper.config && \
    mkdir /tmp/.X11-unix && chown root.root /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

RUN useradd -m developer
COPY ./select_res.py /home/developer/select_res.py
COPY ./start_xorg /home/developer/start_xorg
RUN chown -R developer.developer /home/developer
COPY ./xorg.conf /home/developer/xorg.conf

USER developer

ENV DISPLAY :0.0

CMD sh /home/developer/start_xorg
