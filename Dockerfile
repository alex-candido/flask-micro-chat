FROM python:3.10.3-slim

RUN apt update && \
  apt install -y --no-install-recommends \
  git \
  curl \
  wget \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash python

RUN pip install pdm

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

CMD [ "tail", "-f", "/dev/null" ]