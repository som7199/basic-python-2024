# date : 2024-01-17
# desc : 구구단

# for i in range(2, 10):
#     print('# {}단 시작'.format(i))
#     for j in range(1, 10):
#         # print('{} X {} = {}'.format(i, j, i*j))
#         print(i, 'X', j, '=', i * j, end=' ')
#     print()
#     print('-' * 98)
# print('구구단 끝~!!')

a = int(input('2단부터 출력할 마지막단을 입력하세요(숫자만) > '))

for i in range(2, a + 1):
    # print(i, '단 시작')
    for j in range(1, 10):
        # print(i, 'X', j, '=', f'{i * j:2}', end='\t')
        print(i, 'X', j, '=', f'{i * j:2}', end=' | ')
    print()