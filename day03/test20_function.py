# 20240131
# desc : 함수 만들기(계산기 기능)

def add(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result

def multiple(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y
    return result

def say_hello() -> None:
    print('Hello')

say_hello()
a, b = map(int, input('두 정수 입력 > ').split(' '))
print(f'{a} + {b} = {add(a, b)}')
print(f'{a} - {b} = {minus(a, b)}')
print(f'{a} x {b} = {multiple(a, b)}')
print(f'{a} / {b} = {divide(a, b)}')