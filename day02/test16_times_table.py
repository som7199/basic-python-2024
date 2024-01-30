# 20240130
# desc : 구구단 프로그램
# spec : for문 잘 써야함, 2중 for문의 이해
# debugging
# F9(중단점 토글), F5(디버그 시작), F10(한줄씩 실행), F11(함수 안으로 진입)

for x in range(2, 10):
    print(f'[{x}단] =>', end = ' ')
    for y in range(1, 10):
        print(f'{x} x {y} = {x * y:2d}', end=' | ')
    print()

# x = 2
# while x <= 9:
#     for y in range(1, 10):
#         print(f'{x} x {y} = {x * y:2d}')
#     x += 1