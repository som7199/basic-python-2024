# date : 2024-01-17
# desc : 별표찍기

# for i in range(1, 6):
#     print('*' * i)    

# for i in range(1, 6):
#     for j in range(6 - i):
#         print('*', end="")
#     print()

for i in range(1, 6):
    for j in range(6 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')

for i in range(1, 6):
    for j in range(6 - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print('')
