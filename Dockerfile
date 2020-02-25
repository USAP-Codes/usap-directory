# base image

FROM python:3.8.0-alpine

# dependencies
RUN apk update && \
    apk add --no-cache --virtual build-deps \
    openssl-dev libffi-dev gcc python3-dev musl-dev \
    bash bash-doc bash-completion \
    curl grep git openssh make cmake \
    postgresql-dev netcat-openbsd

# Env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory in the container
WORKDIR /usr/usap/server

# install requirements
COPY ./requirements.txt /usr/usap/server/requirements.txt
RUN pip install -r requirements.txt

# entry script
COPY ./service/server/app.sh /usr/usap/server/app.sh

# modify permissions to run script
RUN chmod +x /usr/usap/server/app.sh

# copy code base
COPY . /usr/usap/server
