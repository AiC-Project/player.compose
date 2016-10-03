FROM busybox

ADD ./run.sh /root/
RUN chmod 755 /root/*.sh

# it's a bit more complicated than that
# see https://github.com/docker/docker/issues/7198
# we want to use the same uid/gid everywhere

USER root
WORKDIR /root/

CMD /root/run.sh
