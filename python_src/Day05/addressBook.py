# date : 2024-01-18
# desc : 주소록 프로그램
import os

# 콘솔(터미널 또는 명령프롬프트) 클리어 함수
def clears():
    command = 'clear'   # OS 윈도우 => cls / Linux, Unix, Mac => clear
    if os.name in ('nt', 'dos'):    # 윈도우면
        command = 'cls'
    os.system(command)

# 연락처 입력 함수
def set_contact():  
    try:
        name, phone, mail, addr = input('입력(이름/핸드폰번호/이메일/주소) > ').split('/')
        contact = [name, phone, mail, addr]
        return contact
    except:
        return None # 오류 났으니 None 리턴

# 연락처 출력 함수
def get_contact(lst):
    print(f'이름\t핸드폰\t이메일\t주소')
    for item in lst:
        for i in item:
            print(f'{i}\t', end='')
        print()

# 연락처 확인
def chK_del_context(name, lst):
    del_index = 0
    for item in lst:
        if item[0] == name:
            return del_index
        else:
            del_index += 1

# 종료 시 연락처 저장
def save_contact(lst):
    f = open('contact_db.txt', mode='w', encoding='utf-8')
    for item in lst:
        f.write(item[0] + ',')
        f.write(item[1] + ',')
        f.write(item[2] + ',')
        f.write(item[3] + '\n')

    f.close()

#  실행 시 연락처 로드
def load_contact(lst):
    f = open('contact_db.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line: 
            break

        lines = line.replace('\n', '').split(',') # ,로 분리된 길이 4 리스트 lines 생성
        contact = [lines[0], lines[1], lines[2], lines[3]]
        lst.append(contact)

    f.close()

# 프로그램 실행함수
def run():
    lst_contact = []
    load_contact(lst_contact)

    while True:
        menu = show_menu()
        if menu == 1:       # 연락처 추가
            clears()
            contact = set_contact()
            if contact != None:
                lst_contact.append(contact)
            else:
                continue

        elif menu == 2:     # 연락처 출력    
            clears()
            get_contact(lst_contact)
            
        elif menu == 3:     # 연락처 삭제
            clears()
            name = input('삭제할 이름 입력 > ')
            del_num = chK_del_context(name, lst_contact)
            if del_num != None:
                lst_contact.pop(del_num)

        elif menu == 4:     # 종료
            save_contact(lst_contact)
            break

        else:
            clears()

# 메뉴 표시 및 메뉴 선택값 리턴 함수
def show_menu():    
    str_menu = ('주소록 프로그램 v0.2\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)

    try:
        num = int(input('메뉴 입력 : '))
        return num
    except:
        return 0

if __name__ == '__main__':
    run()

print('프로그램 종료')