#-*-coding utf-8-*-
import json
import io
import sys
import urllib.request, json

url = "http://3.94.119.184/location"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

# 한글 깨짐 막기 위한 코드. python3부터 지원 
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# # utf-8 형식으로 연다 
# with io.open('getnames.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# 유니코드 x 위해서 ensure_ascii 옵션을 false 설정 
# dumps 는 예쁘게 프린트하는 용도 
# print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))

# print(data["data"][3]["company_name"])

newkeywords = set()
oldkeywords = set()

# old keywords set 
with io.open('oldkeywords.txt', 'r', encoding='utf-8') as old:
    lines = old.readlines()
    for line in lines:
        oldkeywords.add(line.strip())

# crawl new keywords set 
for i in range(len(data["data"])):
    keyword = data["data"][i]["company_name"]
    newkeywords.add(keyword)

onlyNew = newkeywords - oldkeywords

output = ''
for new in onlyNew:
    print(new)
    output += new + '\n'

with io.open('keywords.txt', 'w', encoding='utf-8') as new:
    new.write(output)



# Closing file
# f.close()
old.close()
new.close()