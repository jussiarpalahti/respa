
FROM ubuntu:18.04

WORKDIR /usr/src/app

ENV APP_NAME respaubu3
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update; apt-get install -y python3-venv python3-pip gettext postgresql-client libgdal-dev

COPY requirements.txt .
COPY deploy/requirements.txt ./deploy/requirements.txt

RUN python3 -m pip install --no-cache-dir -r deploy/requirements.txt

COPY . .

RUN groupadd -r respa && useradd --no-log-init -r -g respa respa

RUN mkdir -p www/media; mkdir -p /logs; mkdir -p /usr/src/app/static

RUN chown -R respa:respa /logs  www/media /usr/src/app

USER respa:respa

CMD deploy/server.sh
