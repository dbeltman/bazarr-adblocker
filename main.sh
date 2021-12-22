#!/bin/bash
cd /scripts/postprocess
pip3 install --prefix=/tmp/local -r /scripts/postprocess/requirements.txt
echo $1
python3 /scripts/postprocess/main.py -rw "`realpath -s "$1"`"
