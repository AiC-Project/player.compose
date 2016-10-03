FROM ubuntu:16.04

ENV ANDROID_NDK /opt/android-ndk
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_NDK}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        busybox \
        telnet \
        net-tools \
        iputils-ping \
        android-tools-adb \
        build-essential \
        autoconf \
        vim-common \
        git \
        curl \
        unzip && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /opt/android-ndk-tmp && \
    cd /opt/android-ndk-tmp && \
    curl -sL -o android-ndk.zip http://dl.google.com/android/repository/android-ndk-r12-linux-x86_64.zip && \
    unzip -q android-ndk.zip && \
    mv ./android-ndk-r12 ${ANDROID_NDK} && \
    rm -rf /opt/android-ndk-tmp

RUN dpkg --add-architecture i386 && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386

RUN mkdir /opt/android-sdk-tmp && \
    cd /opt/android-sdk-tmp && \
    curl -sL -o android-sdk.tgz https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \
    tar xf android-sdk.tgz && \
    mv ./android-sdk-linux ${ANDROID_HOME} && \
    rm -rf /opt/android-sdk-tmp


# For a list of the packages that can be installed:  android list sdk --no-ui --all --extended

# "echo y" can only be used for one pacakge at a time.

# XXX There is too much stuff here.

RUN echo y | android update sdk --no-ui --all --filter platform-tools | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-android-support | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter android-24 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter android-23 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-22 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-21 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-20 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter android-19 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-17 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-15 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-10 | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.0 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.3 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.2 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-22.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-21.1.2 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-20.0.0 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-19.1.0 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-17.0.0 | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-24 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-23 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-22 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-21 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-19 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-17 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-15 | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-google_play_services | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-23 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-22 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-21 | grep 'package installed'


RUN useradd -m developer

USER developer

RUN cd /home/developer/ && \
    git clone -b 2.0.0 https://github.com/mmariani/fb-adb.git && \
    cd ./fb-adb && \
    ./autogen.sh && \
    mkdir build && \
    cd build && \
    ../configure --with-android-sdk=${ANDROID_HOME} && \
    make

RUN chown -R developer.developer /home/developer

CMD tail -f /dev/null
