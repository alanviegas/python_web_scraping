FROM mongo
LABEL maintainer 'Alan Viegas <alan.viegas at gmail.com>'
WORKDIR /app
ADD ./apps/API_persistenciaDados /app
RUN apt-get update && \
	apt-get install -y apt-utils && \
    apt-get install -y python && \
    apt-get install -y python-pip && \
    pip install -r /app/requirements.txt
EXPOSE 5000