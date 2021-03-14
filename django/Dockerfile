# NGINX Unit image of Python3.9
FROM python:3.9
ENV PYTHONUNBUFFERED 1

# create work directory of container
WORKDIR /usr/src/app

COPY . .

RUN apt-get update \
    && apt-get install -y python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pipenv

# port used by the listener in config.json
EXPOSE 8080