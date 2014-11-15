FROM ubuntu
MAINTAINER Oliver Bestwalter <oliverr@bestwalter.de>
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python python-pipk
ADD ./ /app
RUN pip install -r /app/requirements.txt
