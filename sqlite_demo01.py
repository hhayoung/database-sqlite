'''
SQLite : DB 서버가 필요없는(DB서버 설치 불필요)
임베디드 관계형 데이터베이스로 경량의 사용이 쉽고,
편리하며 비용이 들지 않는(오픈소스) DB 엔진이다.
자신이 서비스하는 애플리케이션 영역 내부에 공존하는
형태의 데이터베이스
모바일이나 임베디드 기기에서 많이 사용되며, 신뢰성이 높다.
'''

import sqlite3 # 바로 불러올 수 있다.
import datetime

# 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

# 형식 지정하기
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDataTime : ', nowDateTime)

# sqlite3 버전
print('sqlite version : ',sqlite3.version)

# DB 생성 & Auto Commit 설정
# autocommit : DB에 바로 영구적으로 반영되는 것
# 우리는 그냥 학습하는 거니까 그때 그때 commit하면 힘드니까 설정하는 거
# conn - 접속객체라고 생각하면 됨
conn = sqlite3.connect('./resource/database.db', isolation_level = None)  
# db파일위치 지정. 이 때 resource폴더가 미리 생성되어있지 않으면 에러발생.
# isolation_level = None 넣어주면 conn.commit() 생략할 수 있다.

'''
commit : isolation_level = None 일 경우 자동 커밋
isolation_level = None이 아닐 경우에는
conn.commit() 명령으로 DB 반영해줘야 함.

rollback 명령 사용하기 : conn.rollback()
'''

# Cursor 생성(연결, 바인딩)
c = conn.cursor()
print('type : ', type(c))

'''
보통 select로 한 레코드만 가져오는게 아니라 보통은 여러 레코드를 한번에 가져오는데
가져오면 레코드 하나하나씩 읽어야 하는데 
하나의 레코드를 읽으면 그다음 레코드를 읽고, 끝까지 읽어나갈텐데
그 때 커서가 이용된다. (포인터같은 개념)
그 데이터에 하나하나씩 접근할 때 커서라는 포인터 같은 애가 위치를 찾아가서 읽음.
'''

# execute() : 쿼리문을 날리는 함수

# 테이블 생성
# Data Type : Text, NUMERIC, INTEGER, REAL, BLOB
# 구분을 위해서 키워드는 보통 대문자 사용
# 테이블이 이미 있는데 또 생성하면 안되니까 IF NOT EXISTS
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
        username TEXT, email TEXT, tel TEXT, website TEXT, reg_date TEXT)")

# 데이터 삽입하기(sql문에서 문자열 넣을 때는 ''인거 까먹지 말기)
# ? Placeholder : 값을 써줘야 하는 자리에 ? 로 해놓고 변수 넣어주면 된다.
# c.execute("INSERT INTO users VALUES(1, 'KIM', 'test@naver.com', \
#         '010-1234-1234', 'www.test.com', ?)",(nowDateTime,))
# 주의사항
# 튜플 형태로 넣어준다.(속도가 빨라서 튜플 사용)
# 리스트는 추가하고 삭제하고 이런 함수들이 더 많다 보니까 더 느림
# 이게 실행될 때의 그 때의 시간을 넣어준다.

# c.execute("INSERT INTO users VALUES(2, 'Park', 'test2@naver.com', \
#         '010-1234-1234', 'www.test.com', ?)",(nowDateTime,))

# executeMany를 이용한 삽입(튜플, 리스트)
user_list = (
        (3,'Choi','test3@google.com','010-1234-1234','www.test.com', nowDateTime),
        (4,'Lee','test4@google.com','010-1234-1234','www.test.com', nowDateTime),
        (5,'Joo','test5@google.com','010-1234-1234','www.test.com', nowDateTime)
)

c.executemany("INSERT INTO users(id, username, email, tel, website, reg_date) \
                VALUES(?,?,?,?,?,?)",user_list)


# 테이블의 전체 데이터를 삭제하기
# conn.execute('DELETE FROM users')
# 삭제할 때는 cursor 쓰지 X.

# 삭제 결과값을 확인하는 함수 사용
# print('users db deleted : ',conn.execute('DELETE FROM users').rowcount, '행')


# conn 객체 반환(접속 해제)
conn.close()
