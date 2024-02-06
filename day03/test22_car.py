# 20240131
# desc : Car 클래스 만들기

class Car:
    wheel_num = 4
    color = 'white'
    __plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다.')
    
    def moveLeft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def moveRight(self):
        print(f'{self.__plate_num}이 우회전합니다.')
    
    # 생성자를 변경했으므로 변경된 생성자로 호출
    def __init__(self, number, comp, col, gear) -> None:
        self.__plate_num = number
        self.company = comp
        self.color = col
        self.gear_type = gear

    def __str__(self) -> str:   # print(객체) 출력되는 부분
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다.'

    # 외부에서는 접근할 수 없도록 막는 조치
    def getPlateNumber(self):
        return self.__plate_num
    
    def setPlateNumber(self, new_plateNumber):
        self.__plate_num = new_plateNumber

sarah = Car('54라 9538', '현대자동차', '흰색', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차 번호는 {sarah.getPlateNumber()}')
print(f'차 색상은 {sarah.color}')
sarah.moveForward()

sarah.__plate_num = '98하 7789'   # 악의적인 의도를 가지고 변경
print(sarah)

sarah.__plate_num = '98하 999999'   # 초보의 실수
print(sarah)
sarah.setPlateNumber('75마 9999')   # 클래스에 인정받은 동작으로 값을 바꾸기
print(sarah)

csuv = Car('경남88 1922', '기아자동차', '회색', '자동')
print(f'차 번호는 {csuv.getPlateNumber()}')