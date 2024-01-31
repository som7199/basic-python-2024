# 20240131
# desc : 별찍기 또는 피라미드 만들기

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()
    
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print('*', end='')
    print()

for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(' ', end='')
    for j in range(1, i + 1):
        print('*', end='')
    print()