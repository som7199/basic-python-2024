# 20240130
# desc : 흐름제어 if

## 조건이 참일때와 거짓일때로 나누어서 어떤 일 처리 if
number = int(input('정수 입력 > '))     # 입력함수 int(input()) - 문자로 된 입력값을 정수로 변경

if number > 0:      # if 조건: - 참인 조건  
    print('양수입니다.')
elif number == 0:   # 양수X, 음수X
    print('0 입니다.')
elif number < 0:               
    print('음수입니다.')
else:               # else: - 거짓인 조건
    print('정의할 수 없습니다.')