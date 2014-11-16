FROM python
MAINTAINER Oliver Bestwalter <oliverr@bestwalter.de>

RUN apt-get update && apt-get install -y \
    pandoc

COPY ./ /app
COPY ./requirements.txt /root
RUN pip install -r /root/requirements.txt
