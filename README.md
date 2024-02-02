# 파이썬 기초 2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어 -  파이썬

## 1일차
- 개발환경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 파이썬 개발자는 귀도 반 로섬~!!
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10  # 정수, 실수, 불, 문자열 모두 가능
    print(var01)
    print(type(var01))

    print(5 + 4 / 2)    # 7.0
    print(5 == 4)       # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참/거짓으로 조건 분기 (다른 언어 switch)
        - for : 반복문 기분 (다른 언어 foreach)
        - while : 반복문 변형 (다른 언어 do ~ while)
    - 복합자료형 + 연산자(연산함수)
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷, 입력 방법
    - 함수
    - 구구단 + 디버깅

    ```python
    # debugging
    # F9(중단점 토글), F5(디버그 시작), F10(한줄씩 실행), F11(함수 안으로 진입)
    # Shift + F5(디버깅 종료)
    for x in range(2, 10):
        print(f'[{x}단] =>', end = ' ')
        for y in range(1, 10):
            print(f'{x} x {y} = {x * y:2d}', end=' | ')
        print()
    ```
 
## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기(피라미드 만들기)
    - 함수, 람다함수는 나중에 0_<
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화(__plateNumber)
    - 패키지, 모듈

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        - pip 사용
        ```shell
        > pip --version             # 버전확인
        > pip list                  # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명      # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명    # 패키지 삭제
        ```
    - 예외처리 : 비정상적 프로그램종료 막기

    ```python
    def divide(x, y):
        try:
            return x / y        # ZeroDivisionError 발생
        except ZeroDivisionError as e:
            print('[오류!] 제수는 0이 될 수 없습니다!')
            return 0
    ```
    - 텍스트 파일 입출력

    ```python
    f = open('파일명', mode = 'r|w|a', encoding='cp949|utf-8')
    f.read()
    f.readline()    # 읽기
    f.write('text') # 쓰기
    f.close()       # 파일은 반드시 닫는다!
    ```

- 파이썬 응용
    - 주피터 노트북
        - Ctrl + Shift + P (명령팔레트)로 시작
        - 사용방법 (test31_jupyternb.ipynb 참조)
    - folium 기본 사용
    ![folium 사용법](https://github.com/som7199/basic-python-2024/blob/main/images/python_001.png)

## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(Colab)
    - folium 계속
    - json 입출력
    - 응용예제 연습
        - IP주소 확인
        - QRCODE 만들기
    
## 언젠가
- 가상환경
- 객체지향(나중에...)
    - 오버로딩, 오버라이딩
    - 상속, 다중상속
    - 추상 클래스