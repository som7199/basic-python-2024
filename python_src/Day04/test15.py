# date : 2024-01-18
# desc : 예외처리

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def divide(x, y):
    try:
        result = x / y
    except:
        print('제수는 0을 쓸 수 없습니다.')
        result = 0
    return result

try:
    a, b = map(int, input('두 수를 입력 > ').split())
except:
    print('정수만 입력하세요.')
    a = 1
    b = 1


print(plus(a, b))
print(divide(a, b))
print(minus(a, b))