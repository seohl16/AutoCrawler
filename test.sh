#!/bin/bash

python3 parsejson.py

if [ -d download ] ; then
 mv download olddownload
fi

python3 main.py --limit 7 --full true

