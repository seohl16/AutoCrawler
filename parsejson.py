#-*-coding utf-8-*-
import json
import io
import sys

# 한글 깨짐 막기 위한 코드. python3부터 지원 
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# utf-8 형식으로 연다 
with io.open('getnames.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 유니코드 x 위해서 ensure_ascii 옵션을 false 설정 
# dumps 는 예쁘게 프린트하는 용도 
# print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))

# print(data["data"][3]["company_name"])

output = ''
for i in range(len(data["data"])):
    output += data["data"][i]["company_name"] + '\n'
# print(output)

with io.open('names.txt', 'w', encoding='utf-8') as outputfile:
    outputfile.write(output)

# Iterating through the json
# list
# for i in data['emp_details']:
# 	print(i)

# Closing file
f.close()
