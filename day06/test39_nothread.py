# 20240205
# desc : Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget):  # QWidget [상속] 받기, QWidget이 가진 모든 것을 사용할 수 있다.
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self)      # QtDesigner에서 만든 UI 로드
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked)     # ui 파일 내에 있는 위젯 접근은 vscode상에서 색상으로 표시 안됨

    def btnStartClicked(self):
        maxVal = 10000001
        print('시작 버튼 클릭')
        self.pgbTask.setValue(0)        # 프로그레스바 0부터 시작
        self.pgbTask.setRange(0, maxVal - 1)   # 0 ~ 100
        for i in range(maxVal):
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txbLog.append(print_str)
            self.pgbTask.setValue(i)

    def closeEvent(self, QCloseEvent) -> None:      # X버튼 종료 확인
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    loop = QApplication(sys.argv)   # 내 소스 위치로 애플리케이션 생성
    instance = qtwin_exam()         # QWidget을 상속한 qtwin_exam 객체 생성
    instance.show()
    loop.exec_()