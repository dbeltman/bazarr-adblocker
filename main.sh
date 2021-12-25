#!/bin/bash
cd /scripts/postprocess
PYTHONUSERBASE=/config/pipcache/ pip3 install --prefix=/config/pipcache --no-cache-dir -r /scripts/postprocess/requirements.txt
echo $1
PYTHONUSERBASE=/config/pipcache/ python3 /scripts/postprocess/main.py -rw "`realpath -s "$1"`"
