FROM ubuntu:latest
LABEL maintainer 'Alan Viegas <alan.viegas at gmail.com>'
WORKDIR /app
ADD ./apps/API_persistenciaDados /app
RUN apt-get update && \
	apt-get install -y apt-utils && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install -r /app/requirements.txt
CMD python3 /app/src/service/api.py
EXPOSE 5005