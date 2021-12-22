#!/bin/bash
if [[ $(whoami) != "root" ]] ; then
    echo "NOT RUNNING AS ROOT"
    exit 1
fi
cd /scripts/postprocess
pip3 install -r /scripts/postprocess/requirements.txt
echo $(whoami)
python3 /scripts/postprocess/main.py $1 $2 $3 $4