# date : 2024-01-18
# desc : Lottery

import random   # 랜덤

numbers = [i for i in range(1, 46)]
lotto = []  # 숫자 6개 담을 것

for i in range(6):
    lotto.append(random.choice(numbers))    # 1 ~ 45 중 하나를 골라서 lotto에 담음

print(lotto)