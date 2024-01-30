# 20240130
# desc : 홀수/짝수 구분

number = int(input('정수입력 > '))  # 입력 받은 후 정수로 변경

if number % 2 == 0: # 짝수 또는 2의 배수
    print('짝수!')
else:
    print('홀수!')