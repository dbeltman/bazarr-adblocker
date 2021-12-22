#!/bin/bash

pip3 install -r /scripts/postprocess/requirements.txt
echo $(whoami)
python3 main.py $1 $2 $3 $4