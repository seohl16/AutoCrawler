
import json
import io
import sys
import urllib.request, json

output = ""
with io.open('keywords.txt', 'r', encoding='utf-8') as new:
	lines = new.readlines()
	for line in lines:
		output += line


with io.open('oldkeywords.txt', 'a', encoding='utf-8') as old:
    old.write(output)
