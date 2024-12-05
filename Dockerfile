FROM python:3.10.3-slim

RUN apt update && \
  apt install -y --no-install-recommends \
  git \
  curl \
  wget \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash python

RUN pip install pdm

COPY .docker/start-app.sh /home/python/app/.docker/start-app.sh
RUN chmod +x /home/python/app/.docker/start-app.sh && \
  chown python:python /home/python/app/.docker/start-app.sh

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

CMD ["./.docker/start-app.sh"]
