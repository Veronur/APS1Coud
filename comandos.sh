#!/bin/bash
sudo apt update
sudo apt install snapd
sudo apt --assume-yes install python3-pip
pip3 install boto3 
pip3 install flask

