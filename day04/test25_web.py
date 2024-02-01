# 20240201
# desc : urllib 모듈 사용법

# from urllib.request import *                  # request 모듈 안의 모든 내용 다 사용
from urllib.request import Request, urlopen     # Request 클래스와 urlopen만 사용

req = Request('https://m.naver.com/')   # 네이버 웹주소(url)
res = urlopen(req)  # url 주소로 웹사이트 열어달라고 요청

print(f'응답코드 : {res.status}')   # url로 요청된 웹사이트 응답 확인
print(res.read())

# urllib.request 보다 성능이 조금 더 나은 모듈
import requests

res2 = requests.get('https://m.naver.com/')
# print(res2)     # <Response [200]>

print(res2.status_code)
print(res2.text)