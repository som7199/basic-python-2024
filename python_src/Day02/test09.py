# date : 2024-01-16
# desc : 반복문

arr = [i for i in range(1, 101, 2)]
sum = 0

for i in arr:
    sum += i
    
print('합계는', sum)
print('출력완료')

for j in range(5):
    print(j)

for k in 'Hello':
    print(k)

# while문
hit = 0

while hit < 10:
    hit += 1

    if hit == 10:
        print('열번찍어 나무가 넘어갔습니다.')
    else:
        print(hit, '번 나무를 찍었습니다.')

print('나무 찍기 완료')