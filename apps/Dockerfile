FROM selenium/standalone-firefox
LABEL maintainer 'Alan Viegas <alan.viegas at gmail.com>'
WORKDIR /app
ADD ./apps/API_consultaReclameAqui /app
RUN sudo apt-get update && \
	sudo apt-get install -y apt-utils && \
    sudo apt-get install -y python && \
    sudo apt-get install -y python-pip && \
    sudo chmod +x /app/utils/geckodriver && \
    sudo pip install -r /app/requirements.txt
USER seluser
CMD python /app/src/service/api.py
EXPOSE 5000