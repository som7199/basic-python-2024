# 20240130
# desc : while문

# while 참인 조건:
# 공통점 - : -> if 조건: elif 조건: else:, for _ in range():, while 조건:

count = 0

# while count < 10:      # count 변수값이 10보다 작은 동안 반복
while True:              # 무한루프(Infinite Loop) : Window OS, 모바일OS, 자동차네비게이션, 라즈베리파이, 아두이노, 게임, Winform 개발, ...
    count += 1
    print('나무찍기', count)
    if count == 10:
        break           # 무한루프 탈출~~!

# number = 0
# while True:
#     number += 1
#     if '3' in str(number) or '6' in str(number) or '9' in str(number):
#         print('짝!', end = ' ')
#     else:
#         print(number, end = ' ')
    
#     if number == 30: break
    
# print()

number = 0
while True:
    number += 1
    if number > 30: break   # break : 반복문 완전히 빠져나가기
    if str(number).count('3') >= 1 or str(number).count('6') >= 1 or str(number).count('9') >= 1:
        print('짝!', end = ' ')     # 짝! 대신 continue로 변경
        continue    # 반복에서 제외
    else:
        print(number, end = ' ')