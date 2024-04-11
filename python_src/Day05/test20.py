# date : 2024-01-19
# desc : csv 파일 읽기

f = open('./Day05/busanbus_20221231.csv', mode='r', encoding='cp949')    
# 파일 읽는 처리
while True:
    line = f.readline()
    if not line:
        break

    print(line)
f.close()