import sqlite3

# DB 파일 연결
# DB 파일이 있으면 연결하고, 없으면 생성
conn = sqlite3.connect('./resource/database.db')

# 커서 생성(바인딩)
c = conn.cursor()

# execute() : 쿼리문 날리기

# 데이터 조회(전체 데이터)
c.execute("SELECT * FROM users")

# 현재 데이터들을 메모리로 가져온 상태
# 이때 커서의 위치는 첫번째 레코드에 있는 상태

# 조회한 결과를 가져오기 위한 함수들
print('first : \n', c.fetchone())
# fetchone() : 하나씩 가져오는 함수
# -> 한 개의 레코드만 가져오는 함수기 때문에 리스트에 담지 않는다.

# 지정한 만큼 가져오기
print('second : \n', c.fetchmany(size=3)) 
# -> 현재 커서의 위치부터 3개의 레코드를 리스트에 담아서 가져온다.
# -> 커서의 위치는 초기화되는게 X

# 전체 행(row) 가져오기
print('All : \n', c.fetchall())
# -> 5번째 레코드만 나오는 이유는 
#    앞에서 다 뽑아갔기 때문에(커서위치가 이동해서) 나머지가 전체 출력되는 것.
# -> 하나의 레코드만 나오지만 그래도 리스트에 담아서 가져온다.
# -> 커서의 위치가 처음으로 돌아가지 않기 때문에 나머지만 출력된 것.

# 반복문 사용하기 1
rows = c.fetchall()

for row in rows:
    print('조회 : ', row)


# 반복문 사용하기 2 --> 사용하기 제일 편해보임
for row in c.fetchall():
    print('조회 : ', row)

# 반복문 사용하기 3
for row in c.execute("SELECT * FROM users ORDER BY id DESC"):
    print('조회 : ', row)


# WHERE 패턴 1
param1 = (2,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print('param1 :', c.fetchone())
# 현재 위치에서 더이상의 레코드 없음
print('param1 :', c.fetchall())

# WHERE 패턴 2(포맷형식)
param2 = 3
# c.execute("SELECT * FROM users WHERE id='%s'" % param2)
c.execute(f"SELECT * FROM users WHERE id={param2}")
print('param2 :', c.fetchone())
print('param2 :', c.fetchall())

# WHERE 패턴 3 (딕셔너리 타입)
c.execute("SELECT * FROM users WHERE id=:Id", {'Id': 4})
print('param3 :', c.fetchone())

# WHERE 패턴 4
param4 = (2,5)  # 2랑 5
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4 :', c.fetchall())

# WHERE 패턴 5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,4))
print('param5 :', c.fetchall())

# WHERE 패턴 6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {'id1':2, 'id2':5})
print('param6 :', c.fetchall())

# conn.close()

# Dump 출력
with conn:  # 디비에 연결되어 있고,
    # 덤프파일 만들거임. 확장자는 .sql로
    with open('./resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
        print('Dump 완성!!')   

# conn.iterdump() : 해당 데이터베이스에 있는 내용 하나하나씩을 순회하면서 가져온다. sql명령문들
# dump.sql 파일 만들어진거를 실행해봤는데 sql 명령문들이 모여 있다.
# 이 파일만 실행해도 users 테이블이 만들어지고 데이터까지 다 들어갈 것.
# 디비브라우저에 sql 실행에다가 dump.sql의 내용을 복사해서 붙여넣기 하고 
# 실행해보면 그대로 구조와 데이터가 다 만들어진다. 
# dump파일은 무조건 commit 명령어가 마지막에 붙어이써야 한다.


conn.close()