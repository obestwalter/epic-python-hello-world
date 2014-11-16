# see:
#   * https://docs.docker.com/articles/dockerfile_best-practices/
#   * http://phusion.github.io/baseimage-docker
#   * [Production] http://jpetazzo.github.io/2014/06/23/docker-ssh-considered-evil/

# see: https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
FROM phusion/baseimage:0.9.13
MAINTAINER Oliver Bestwalter <oliver@bestwalter.de>

ENV HOME /root

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init", "--enable-insecure-key"]

# BEGIN MY STUFF ##############################################################

#RUN apt-get update && apt-get install -y \
#    python
#    pandoc

#COPY ./ /app
#RUN pip install -r /app/requirements.txt

# END MY STUFF ################################################################

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
