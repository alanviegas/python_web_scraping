#!/bin/sh
apt-get update
apt-get install -y firefox
apt-get install -y python3.7
apt-get install -y python-pip
apt-get install -y nginx
chmod +x ./utils/geckodriver  >> ./log/output.log

pip install -r requirements.txt  >> ./log/output.log
python -u ./src/service/api.py >> ./log/output.log