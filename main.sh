#!/bin/bash

pip3 install -r requirements.txt
echo $(whoami)
python3 main.py $1 $2 $3 $4