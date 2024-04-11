# date : 2024-01-16
# desc : 자료형 상세

# None 타입
c = None
# == 같으면 True, 다르면 False
# None 은 0이 아님
print(c == None)
print(c == 0)

# 숫자 타입
galaxy = 100
print(galaxy)
print(type(galaxy))
galaxy = 10_000_000
print(galaxy)
print(type(galaxy))
galaxy = 3.14159265757
print(galaxy)
print(type(galaxy))

# 진수
galaxy = 0b10000000000  # 2진수
print(galaxy)
galaxy = 0o17           # 8진수
print(galaxy)
galaxy = 0xff           # 16진수
print(galaxy)

# 문자열형 ', " 둘 다 가능
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)
bruce_eckel = 'Life is short, \n\tYou need Python'
print(bruce_eckel)

text = '''안녕하세요
배고파요
얼른 점심 먹어요'''
print(text)

# 불형 boolean, True(참, 1) False(거짓, 0)
print(1 + 1 == 1)
print(2 * 15 == 30)
print(True is True)

# 배열 == 리스트
# 리스트
c = [i for i in range(1, 11)]
print(c)

arr = [1, False, 'True', 3.14, [1, 3, 5, 7]]
print(arr)

arr1 = []   # 빈 리스트
print(arr1 is None)

b = [1,2,3,4,5,6,7,8,9,10]
b[3] = 30
print(b)

# 튜플 == 리스트's 친척
d = (1, 3, 5, 7, 9)
print(d)
# d[2] = 30     # 튜플은 들어있는 값을 수정할 수 없음
# print(d)

# 딕셔너리
dinr = {'school' : '학교', 'grade' : '학년'}
spiderman = {'name' : 'Peter Park', 'age' : 18, 'weapon' : 'Web shooter'}
print(spiderman)
print(spiderman['weapon'])