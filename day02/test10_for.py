# 20240130
# desc : for 반복문

std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]
kor_sum = 0

for i in std:   # 리스트 std의 값을 하나씩 i에 넣어서 반복할 요소가 있을 때까지 반복
    kor_sum += i

print(kor_sum)
print(kor_sum / len(std))

list_a = [[1,3,5], [2,4,8], [10,15,20]]     # 2차원 리스트

for in_list in list_a:
    for item in in_list:
        print(item, end=' ')
    print()