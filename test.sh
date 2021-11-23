#!/bin/bash

python3 parsejson.py

python3 main.py --limit 7 --full true

python3 update.py