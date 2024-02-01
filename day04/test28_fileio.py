# 20240201
# desc : 텍스트 파일 입출력

# mode : a(append : 내용 추가) / r(read : 파일 읽기) / w(write : 파일 쓰기)
# encoding : cp949(euc-kr : 한글), utf-8(만국공통어)
# f = open(r'C:\Sources\Basic-Python-2024\day04\sample.txt', mode='w', encoding='utf-8')
f = open(r'sample.txt', mode='w', encoding='utf-8')

# write()에서 엔터를 추가하려면 마지막에 \n 추가!
f.write('안녕하세요. 우리는 IoT 개발자 과정입니다.\n') # mode = a, w
f.write('반갑습니다!!')

f.close()   # 파일은 무조건 마지막에 닫는다!
print('파일이 생성되었습니다.')