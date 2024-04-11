# date : 2024-01-17
# desc : 입출력

# 단일입력
# a = int(input('정수를 입력하세요 > ')) # 문자열을 정수로 변환
# print(a * 3)

# 다중입력
# x, y = input('영단어 2개를 입력하세요(구분자 ,) > ').split(',')
# print('첫 번째 단어', x)
# print('두 번째 단어', y)

print('Hello\nWorld\tI\'m Som! \b!')

name = '솜'
age = 20
gender = '여'
print('안녕하세요. 저는 %s 입니다. \n저는 %4d대입니다. %s자입니다.'%(name, age, gender))
print('안녕하세요. 나는 {0}입니다. 나는 {1}대입니다. {2}자입니다.'.format(name, age, gender))
print(f'안녕하세요. 나는 {name}입니다. 나는 {age:4}대입니다. {gender}자입니다.')
print('%4.4f'%(245.123456789), '%4.4d'%(245.123456789))