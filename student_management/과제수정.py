import sqlite3

conn = sqlite3.connect('./resource/db_task.db',isolation_level=None)
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS student_info( \
            student_id INTEGER PRIMARY KEY, \
            name TEXT, \
            tel TEXT, \
            region TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS student( \
            student_id, \
            os INTEGER NOT NULL CHECK (os>=0 and os<=100), \
            cv INTEGER NOT NULL CHECK (cv>=0 and cv<=100), \
            db INTEGER NOT NULL CHECK (db>=0 and db<=100), \
            FOREIGN KEY(student_id) \
            REFERENCES student_info(student_id))')

chk_student = []
cur.execute('select * from student_info')
for row in cur.fetchall():
    chk_student.append(row[0])
# print(chk_student)
chk_grade = []
cur.execute('select * from student')
for row in cur.fetchall():
    chk_grade.append(row[0])
# print(chk_grade)

#################################학생정보입력####################################
def student_insert():
    student_id = int(input('학번 입력 : '))
    name = input('이름 입력 : ')
    tel = input('전화번호 입력 : ')
    region = input('주소(지역) 입력 : ')
    print()

    cur.execute('INSERT INTO student_info VALUES(?,?,?,?)',(student_id, name, tel, region))
    chk_student.append(student_id)

#################################성적정보입력####################################
def grade_insert():
    while True:
        id_chk = int(input('학번 검색 : '))
        print()
        if id_chk in chk_student:
            cur.execute('SELECT * FROM student_info WHERE student_id = ?',(id_chk,))
            for student in cur.fetchall():
                print(student[0], end=', ')
                print(student[1], end=', ')
                print(student[2], end=', ')
                print(student[3], end=', ')
            if id_chk in chk_grade:
                print('입력완료')
            else:
                print('미입력')

                os = int(input('운영체제 : '))
                cv = int(input('컴퓨터비전 : '))
                db = int(input('데이터베이스 : '))
                try:
                    cur.execute('INSERT INTO student VALUES(?,?,?,?)',(id_chk, os, cv, db))
                    print('성적 입력 성공!!')
                    chk_grade.append(id_chk)
                except IntegrityError:
                    print('0~100점 사이의 점수만 입력해주세요.')
                    continue
            print()
        else:
            print('존재하지 않는 학번입니다..')
            break
            
#################################학생정보출력####################################
def student_select():
    print('-------------------------------------------------')
    print('학번\t이름\t전화번호\t주소\t성적입력여부')
    print('-------------------------------------------------')

    cur.execute('SELECT * FROM student_info')
    stu_cnt = 0
    for student in cur.fetchall():
        stu_cnt += 1
        print(student[0], end='\t')
        print(student[1], end='\t')
        print(student[2], end='\t')
        print(student[3], end='\t')

        if student[0] not in chk_grade:
            print('미입력')
        else:
            print('입력완료')

    print()
    print(f'전체 학생수 : {stu_cnt}명')
    
#################################성적정보출력####################################
def grade_select():
    print('--------------------------------------------------------------')
    print('학번\t이름\t운영체제 컴퓨터비전 데이터베이스 총점\t평균')
    print('--------------------------------------------------------------')
    
    cur.execute('SELECT s.student_id, s.name, g.os, g.cv, g.db  \
    FROM student g, student_info s \
    WHERE g.student_id = s.student_id')
    
    grade_cnt = 0
    for student in cur.fetchall():
        grade_cnt += 1
        print(student[0], end='\t')
        print(student[1], end='\t')
        print(student[2], end='\t  ')
        print(student[3], end='\t\t')
        print(student[4], end='\t  ')
        score_sum = student[2]+student[3]+student[4]
        print(score_sum, end='\t')
        score_avg = format(score_sum/3, '.2f')
        print(score_avg)

    print()
    print(f'전체 학생수: {grade_cnt}명')

#################################학생정보수정###############################
######
def student_update():
    id = int(input('학번 입력 : '))
    if id in chk_student:
        while True:
            print('-----------------------------------------')
            print('1. 이름 변경')
            print('2. 전화번호 변경')
            print('3. 주소 변경')
            print('4. 수정 완료')
            print('-----------------------------------------')
            update_menu = int(input('> 수정할 내용 : '))
            if update_menu == 1:
                update_name = input('변경할 이름 입력 : ')
                cur.execute('UPDATE student_info SET name=? WHERE student_id=?',(update_name, id,))
            elif update_menu == 2:
                update_tel = input('변경할 전화번호 입력 : ')
                cur.execute('UPDATE student_info SET tel=? WHERE student_id=?',(update_tel, id,))
            elif update_menu == 3:
                update_region = input('변경할 주소 입력 : ')
                cur.execute('UPDATE student_info SET region=? WHERE student_id=?',(update_region, id,))
            elif update_menu == 4:
                break
            else:
                print('1부터 4의 숫자만 입력하세요.')
    else:
        print('학번이 존재하지 않습니다..')

#################################성적정보수정####################################
def grade_update():
    id = int(input('학번 입력 : '))
    if id in chk_student:
        if id in chk_grade:
            while True:
                print('-----------------------------------------')
                print('1. 운영체제 점수 수정')
                print('2. 컴퓨터비전 점수 수정')
                print('3. 데이터베이스 점수 수정')
                print('4. 수정 완료')
                print('-----------------------------------------')
                update_menu = int(input('> 수정할 과목 : '))
                if update_menu == 1:
                    update_os = int(input('변경할 점수 입력 : '))
                    cur.execute('UPDATE student SET os=? WHERE student_id=?',(update_os, id,))
                elif update_menu == 2:
                    update_cv = int(input('변경할 점수 입력 : '))
                    cur.execute('UPDATE student SET cv=? WHERE student_id=?',(update_cv, id,))
                elif update_menu == 3:
                    update_db = int(input('변경할 점수 입력 : '))
                    cur.execute('UPDATE student SET db=? WHERE student_id=?',(update_db, id,))
                elif update_menu == 4:
                    break
                else:
                    print('1부터 4의 숫자만 입력하세요.')
        else:
            print('성적 정보를 먼저 입력해주세요.')

    else:
        print('학번이 존재하지 않습니다..')
#################################학생정보삭제####################################
def student_delete():
    id = int(input('학번 입력 : '))
    if id in chk_student:
        if id in chk_grade:
            # cascade
            cur.execute('DELETE FROM student WHERE student_id = ?',(id,))
            chk_grade.remove(id)
            cur.execute('DELETE FROM student_info WHERE student_id = ?',(id,))
            chk_student.remove(id)
            print(f'학번이 {id}인 학생이 삭제되었습니다.')
        else:
            cur.execute('DELETE FROM student_info WHERE student_id = ?',(id,))
            chk_student.remove(id)
            print(f'학번이 {id}인 학생이 삭제되었습니다.')
    else:
        print('학번이 존재하지 않습니다.')

#################################메뉴화면####################################
def menu_display():
    print('-----------------------------------------')
    print('            학사관리 시스템               ')
    print('-----------------------------------------')
    print('1. 학생 정보 입력')
    print('2. 학생 정보 출력')
    print('3. 학생 정보 수정')
    print('4. 학생 정보 삭제')
    print('5. 학생 성적 입력')
    print('6. 학생 성적 출력')
    print('7. 학생 성적 수정')
    print('X. 프로그램 종료')
    print('-----------------------------------------')

    menu = input('메뉴 선택 : ')
    return menu

############################################################################

while True:
    menu = menu_display()
    if menu == '1':
        student_insert()
    elif menu == '2':
        student_select()
    elif menu == '3':
        student_update()
    elif menu == '4':
        student_delete()
    elif menu == '5':
        grade_insert()
    elif menu == '6':
        grade_select()
    elif menu == '7':
        grade_update()
    elif menu == 'x' or menu == 'X':
        print('종료')
        break
    else:
        print('메뉴를 다시 선택해주세요.')

# student_insert()
# student_select()
# grade_insert()
# grade_select()
# student_update()
# grade_update()
# student_delete()

conn.close()


