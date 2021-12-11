#!/bin/bash
folder=$1
for file in $folder/*.nl.srt; do python3 /home/dbtman/bazarr-adblocker/main.py "$file"; done
