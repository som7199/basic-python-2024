# 20240201
# file : test27_eh.py
# desc : 예외발생 처리
# 프로그램이 실행되다가 갑자기 비정상적으로 종료되는 것 => 예외

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y        # ZeroDivisionError 발생
    except ZeroDivisionError as e:
        print('[오류!] 제수는 0이 될 수 없습니다!')
        return 0

def getOperands():      # 계산할 수를 입력받는 함수
    # 34. 을 입력했을 때 예외발생 ValueError
    try:
        a, b = map(int, input('두 수 입력(구분자 공백) > ').split())
        return a, b
    except ValueError as e:
        print(e)    # 정확한 예외 메시지 출력 => invalid literal for int() with base 10: '34.'
        print('[오류!] 정수만 입력하세요')
        return 1, 1

while True:
    mnu = input('메뉴입력(p[덧셈],m[뺄셈],t[곱셈],d[나눗셈],x[종료]) > ')

    if mnu == 'p':
        a, b = getOperands()
        print(f'[덧셈] \n{a} + {b} = {add(a, b)}')   

    elif mnu == 'm':
        a, b = getOperands()
        print(f'[뺄셈] \n{a} - {b} = {minus(a, b)}')   

    elif mnu == 't':
        a, b = getOperands()
        print(f'[곱셈] \n{a} * {b} = {multiple(a, b)}')   

    elif mnu == 'd':
        a, b = getOperands()
        print(f'[나눗셈] \n{a} ÷  {b} = {divide(a, b)}')   

    elif mnu == 'x':
        print('종료!')
        break

    else:
        continue    # 다시 메뉴 선택으로 올라감