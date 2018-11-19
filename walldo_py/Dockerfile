FROM python:3.6-alpine

# Install SSH client
RUN apk add openssh-client

# Elasticsearch deps
RUN pip3 install elasticsearch pymongo

# Copy walldo code
COPY ./waldo /

WORKDIR /waldo