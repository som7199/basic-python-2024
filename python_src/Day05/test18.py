# date : 2024-01-19
# desc : 파일 입출력

# 한글을 쓰기 위해선 utf-8 방식의 인코딩을 써야함!, ascii(영어만 처리), cp949(한글처리)
f = open('./Day05/PFRO.log', mode='r', encoding='utf-8')    # 유니코드 8바이트
# 파일 읽는 처리
while True:
    line = f.readline()
    if not line:
        break

    print(line)
f.close()