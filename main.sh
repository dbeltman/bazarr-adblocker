#!/bin/bash
cd /scripts/postprocess
pip3 install -r /scripts/postprocess/requirements.txt
python3 /scripts/postprocess/main.py -rw "$1"
