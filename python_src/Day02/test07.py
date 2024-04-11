# date : 2024-01-16
# desc : 연산자(operator)
import math
print(5 / 2)    # 실수(정확하게) 나누기
print(5 // 2)   # 정수로 나누기
print(5 % 2)    # 나머지
print('2 ** 10 => {} / math.pow(2, 10) => {}'.format(2 ** 10, math.pow(2, 10)))

# ()
print((3 + 5) * 10)
print(3 + (5 * 10))

print('-' * 30)

# 문자열 연산
# +(문자열 합치기), *(문자열 반복 출력)
g = 'Hello'
h = 'World'
print(g + h)
print(g, h)
print(g * 10)
print(g[0])
print(len(g))

# (문자열)리스트 자르기
print(g[0:4])
print(g[2:5])
print(g[-2:5])  # lo

# 날짜시간 문자열로 자르기 연습
curr_datetime = '2024-01-16 15:07:35'
print(curr_datetime[0:4] + '년')
print(curr_datetime[5:7] + '월')
print(curr_datetime[8:10] + '일')
date, time = curr_datetime.split()
print(time[0:2] + '시')
print(time[3:5] + '분')
print(time[6:] + '초')

# 리스트 자를 때 뒤의 인덱스는 찾고자하는 인덱스 + 1
arr = [2, 4, 6, 8, 10]
print(arr[1:3])

arr2 = [1, 3, 5]
print(arr + arr2)   # 리스트 합치기
print(arr* 2)       # 리스트 반복
