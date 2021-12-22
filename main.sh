#!/bin/bash

pip3 install -r /scripts/postprocess/requirements.txt
echo $(whoami)
python3 /scripts/postprocess/main.py $1 $2 $3 $4