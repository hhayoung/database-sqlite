# 테이블 수정 / 삭제

import sqlite3

# DB 접속 및 생성
conn = sqlite3.connect('./resource/database.db')

# cursor 바인딩
c = conn.cursor()

# 데이터 수정 1 (기본방식)
c.execute("UPDATE users SET username = ? WHERE id = ?", ('Cho',3))

# 데이터 수정 2 (딕셔너리형식)
c.execute("UPDATE users SET username = :username WHERE id = :id", {'username' : 'Kang', 'id' : 5})

# 데이터 수정 3 (포맷형식)
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" %( 'Hong', 4))
c.execute(f"UPDATE users SET username = '{'Hong2'}' WHERE id = {4}")
# -> 문자열을 넣어줘야 하기 때문에 {} 앞뒤로 '' 필요


# 데이터 삭제 1 (기본방식)
c.execute("DELETE FROM users WHERE id = ?",(2,))

# 데이터 삭제 2 (딕셔너리형식)
c.execute("DELETE FROM users WHERE id = :id",{'id':5})

# 데이터 삭제 3 (포맷형식)
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

# [문제1] 데이터 확인하기
c.execute("SELECT * FROM users")
for user in c.fetchall():
    print('조회 : ', user)

# [문제2] 남은 데이터 모두 삭제하기 (삭제된 행의 수 출력)
print('삭제 : ', c.execute("DELETE FROM users").rowcount, "행")


# 커밋(데이터베이스 반영하기 위해)
conn.commit()

# 접속 해제
conn.close()