# see: https://docs.docker.com/articles/dockerfile_best-practices/

FROM python
MAINTAINER Oliver Bestwalter <oliverr@bestwalter.de>

RUN apt-get update && apt-get install -y \
    pandoc

COPY ./ /app
RUN pip install -r /app/requirements.txt
