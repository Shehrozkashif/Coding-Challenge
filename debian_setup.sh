#!/bin/bash
set -e

sudo apt update
sudo apt install -y python3 python3-pip gcc

pip3 install -r requirements.txt

python3 yaml_to_header.py add.yaml > generated_header.h
gcc header_to_yaml.c -o header_to_yaml
./header_to_yaml generated_header.h > regenerated.yaml
