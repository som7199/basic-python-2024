# date : 2024-01-18
# desc : 예외처리

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def divide(x, y):
    result = x / y
    return result

try:
    a, b = map(int, input('두 수를 입력 > ').split())
    print(plus(a, b))
    print(divide(a, b))
    print(minus(a, b))
except:
    print('입력값이 잘못되었습니다.')
    print('정수 입력 또는 제수에 0을 입력하지 마세요.')


