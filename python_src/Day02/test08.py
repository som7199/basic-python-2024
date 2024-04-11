# date : 2024-01-16
# desc : 흐름제어
name = '솜'
state = '감기'

if name == '솜' and state == '감기':
    print('진료실로 가서')   
    print('선생님 감기에요. 주사주세요')   
elif name == '솜' and state == '몸살':
    print('진료실로 가서')
    print('몸살이에요 주사주세요.')
elif name == '길동' and state == '감기':
    print('주사실로 가서')
    print('주사를 맞는다.')
else:
    print('대기!')

# if name == '솜':
#     print('진료실로 들어갑니다.')
#     if state == '감기':
#         print('선생님 아파요 ㅠ')
#         print('기침이 계속 나요')
#     elif state == '몸살':
#         print('선생님 아파요!')
#         print('몹시 춥고 몸이 떨려요')
# elif name == '길동':
#     print('주사실로 간다.')
# else:
#     print('대기실에서 기다린다.')