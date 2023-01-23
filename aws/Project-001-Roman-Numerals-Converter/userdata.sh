#! /bin/bash

yum update -y
yum install python3 -y
pip3 install flask
yum install git -y
cd /home/ec2-user
wget -P templates https://raw.githubusercontent.com/AydinTokuslu/my-projects/main/aws/Project-001-Roman-Numerals-Converter/templates/index.html
wget -P templates https://raw.githubusercontent.com/AydinTokuslu/my-projects/main/aws/Project-001-Roman-Numerals-Converter/templates/result.html
wget https://raw.githubusercontent.com/AydinTokuslu/my-projects/main/aws/Project-001-Roman-Numerals-Converter/flask-2.py
python3 flask-2.py