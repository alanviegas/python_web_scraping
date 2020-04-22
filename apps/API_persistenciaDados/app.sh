#!/bin/sh
apt-get update
apt-get install -y python3.7
apt-get install -y python-pip

pip install -r requirements.txt  >> ./log/output.log
python -u ./src/service/api.py >> ./log/output.log