# 20240131
# desc : 객체지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person:   # 사람 클래스 선언
    name = ''   # 멤버변수
    age = 0
    gender = ''

    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할 때 동작
    # inin == initialization(초기화)
    def __init__(self) -> None:
        self.name = '홍길동'
        self.age = 29
        self.gender = '남자'

    # 클래스를 호출 시 원하는 형태로 변환해서 보여줄 때
    def __str__(self) -> str:
        strs = f'커스텀 출력, 이름 {self.name} 객체 생성!'
        return strs

    # 멤버함수 매개변수 self 필수!
    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

# 사람 객체 생성, Instance(사례, 예제)
mg = Person()
sm = Person()

# print(type(mg))
# print(id(mg))     # 다른 객체인지 확인
# print(id(es))

mg.name = '성명건'
mg.age = 47
mg.gender = '남자'

sm.name = '김소민'
sm.age = 26
sm.gender = '여자'

print(f'mg => 이름 : {mg.name} / 나이 : {mg.age}세 / 성별 : {mg.gender}')
print(f'es => 이름 : {sm.name} / 나이 : {sm.age}세 / 성별 : {sm.gender}')

mg.walk()
print('1분동안 걷는다.')
mg.stop()

sm.walk()
print('그만 걸을래요')
sm.stop()

print('\n------- 생성자 함수 추가 -------')
gd = Person()
print(f'gd => 이름 : {gd.name} / 나이 : {gd.age}세 / 성별 : {gd.gender}')
print(gd)