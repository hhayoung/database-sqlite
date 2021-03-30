import sqlite3

conn = sqlite3.connect('./resource/practice.db',isolation_level= None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS studentGrade(\
    stu_id TEXT PRIMARY KEY, \
    manaSystem INTEGER CHECK (manaSystem>=0 and manaSystem<=100), \
    vision INTEGER CHECK (vision >= 0 AND vision  <= 100), \
    database INTEGER CHECK (database >= 0 AND database  <= 100), \
    FOREIGN KEY(stu_id) \
    REFERENCES studentInfo(stu_id))")

c.execute("CREATE TABLE IF NOT EXISTS studentInfo(stu_id TEXT PRIMARY KEY, name TEXT, phoneNum TEXT, address TEXT )")

def menu_display():
    print('==========================')
    print('       학사관리 시스템     ')
    print('==========================')
    print('1. 학생 정보 입력')
    print('2. 학생 정보 출력')
    print('3. 학생 성적 입력')
    print('4. 학생 성적 출력')
    print('X. 프로그램 종료')
    print('==========================')
    menu = input('메뉴 선택 : ')
    return menu

def ViewStuInfo():
    print('--------------------------------------------------')
    print('학번'+'\t이름' +'\t전화번호'+'\t주소'+'\t성적입력여부')
    print('--------------------------------------------------')

    c.execute("SELECT * FROM studentInfo")
    students = c.fetchall()

    for student in students:
        print(student[0], end ='\t')
        print(student[1], end ='\t')
        print(student[2], end ='\t')
        print(student[3], end ='\t')
        
        n = len(c.execute("SELECT * FROM studentGrade WHERE stu_id = ?",(student[0],)).fetchall())
        if n == 1:
            print('입력완료')
        else: 
            print('미입력') 
            
        
    c.execute("SELECT COUNT(*) FROM studentInfo")
    print('전체 학생 수:',c.fetchall()[0][0],'명')
    
# c.execute("SELECT * FROM studentInfo")
# cnt_stus = c.fetchall()
# for cnt_stu in cnt_stus:
#     print(cnt_stu)

def student_info():
    stu_id = input('학번 입력 : ')
    name = input('이름 입력 : ')
    phoneNum = input('전화번호 입력: ')
    address = input('주소 입력: ')
    print("학생 정보가 올바르게 입력 되었습니다")

    c.execute("INSERT INTO studentInfo VALUES(?,?,?,?)",(stu_id,name,phoneNum,address))

def grade_():
    id = input('학번 입력하세요:')
    
    chk_stu = len(c.execute("SELECT * FROM studentInfo WHERE stu_id = ?",(id,)).fetchall())
    # print(chk_stu)
    if chk_stu == 1:
        chk_grade = len(c.execute("SELECT * FROM studentGrade WHERE stu_id = ?",(id,)).fetchall())
        # print(type(chk_grade))

        c.execute("SELECT * FROM studentInfo WHERE stu_id = ?",(id,))
        students = c.fetchall()

        for student in students:
            print(student[0], end ='\t')
            print(student[1], end ='\t')
            print(student[2], end ='\t')
            print(student[3], end ='\t')
        if chk_grade == 1:
            # print('성적 입력 되어 있음')
            print('입력완료')
            
        else:
            # print('성적 미입력된 상태')
            print('미입력')
            manaSystem= int(input('운영체제 점수 입력 : '))
            vision = int(input('컴퓨터 비전 점수입력: '))
            database = int(input('데이터 베이스 점수 입력: '))
            c.execute("INSERT INTO studentGrade VALUES(?,?,?,?)",(id,manaSystem,vision,database))
            print("성적 입력 성공!")
            print()
    else:
        print('존재하지 않는 학번입니다.')

def ViewGrade():
    print('-----------------------------------------------------')
    print('학번'+'\t이름'+' 운영체제'+' 컴퓨터비전'+' 테이더베이스'+'\t총점'+'\t평균')
    print('-----------------------------------------------------')
    
    c.execute("SELECT si.stu_id, si.name, sg.manaSystem, sg.vision, sg.database FROM studentGrade sg, studentInfo si where sg.stu_id = si.stu_id")

    # c.execute("SELECT * FROM studentGrade")
    grades = c.fetchall()

    for grade in grades:
        print(grade[0], end ='\t')
        print(grade[1], end ='\t')
        print(grade[2], end ='\t')
        print(grade[3], end ='\t')
        print(grade[4], end= '\t')
        
        score = int(grade[2]) + int(grade[3]) + int(grade[4])
        print(score, end = '\t')
        avg = round(score/3, 2 )
        print(avg)
        

    c.execute("SELECT COUNT(*) FROM studentGrade")
    print('전체 학생 수:',c.fetchall()[0][0],'명')

while True:
    menu = menu_display()
    if menu == '1':
        student_info()
    elif menu == '2':
        ViewStuInfo()
    elif menu == '3':
        grade_() 
    elif menu == '4':
        ViewGrade()
    elif menu == 'X' or menu == 'x':
        break
    else:
        print(' 1~4 숫자만 입력하d세요')

# ViewStuInfo()
# student_info()
# grade_()
# ViewGrade()
# Search()


conn.close()