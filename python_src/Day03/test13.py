# date : 2024-01-17
# desc : 함수 만들기

def plus(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result

def multiple(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y  # 0으로 나눌 수 없음!
    return result


# 매개변수가 몇개든 상관없이 더하는 함수
def adds(*params):
    result = 0
    for i in params:
        result += i

    return result


print(f'adds(1,2,3,4) = {adds(1,2,3,4)}')
print(f'adds(1,2,3,4,5,7,8,9,10) = {adds(1,2,3,4,5,6,7,8,9,10)}')

# a, b = map(int, input('두 수를 입력하세요 > ').split())
# print(f'더하기 결과는 {plus(a, b)}')
# print(f'빼기 결과는 {minus(a, b)}')
# print(f'곱하기 결과는 {multiple(a, b)}')
# print(f'나누기 결과는 {divide(a, b)}')