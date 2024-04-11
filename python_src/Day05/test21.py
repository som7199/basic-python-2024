# date : 2024-01-19
# desc : csv 모듈 사용 파일 읽기

# csv 파일로 읽으면 한 줄마다 리스트로 만들어줌
# utf-8로 못읽음, 파일 자체가 utf-8로 안되어있어서 구랭
# notepad++로 열어본  busanbus_20221231 csv 파일은 잘 여림
# notepad++에서 인코딩 utf-8로 변환하니까 vscode에서도 파일 안깨지고, encoding='utf-8' 가능!@

import csv

filename = 'busanbus_20221231.csv'
dirname = './Day05/'

# f = open(dirname + filename, mode='r', encoding='cp949')
f = open(dirname + filename, mode='r', encoding='utf-8')
reader = csv.reader(f, delimiter=',')
next(reader)
for line in reader:
    print(line)

f.close()