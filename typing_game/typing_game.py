import random
import time
import winsound

import sqlite3
import datetime

# DB생성 & Autocommit
conn = sqlite3.connect('./resource/typing_game_records.db',isolation_level=None)

# Cursor 연결
cur = conn.cursor()

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS records(\
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            cor_cnt INTEGER, \
            time_rec TEXT, \
            regdate TEXT)")
# AUTOINCREMENT : 자동으로 숫자를 증가시켜 넣어준다.
# 오라클은 autoincrement 없고 sequence 사용
# mysql은 autoincrement 사용

words = []
n = 1 # 게임 횟수

correct_cnt = 0 # 정답 개수

with open('./game_resource/word.txt','r') as f:
    for word in f:
        words.append(word.strip())

input('엔터키를 누르세요! 게임 시작됩니다.')

start = time.time()
# time() - 70년 1월 1일 0시 0분부터의 시간흐름을 초단위로

while n <= 5:  # 다섯 문제 추출 
    random.shuffle(words)
    question = random.choice(words)  # 랜덤으로 하나를 추출

    print()
    print('******Question')
    print(question) # 문제 출력

    answer = input() # 사용자 입력값 
    print()

    if str(question).strip() == str(answer).strip():
        print('정답')

        # 정답 사운드 
        winsound.PlaySound('./game_resource/good.wav', winsound.SND_FILENAME)
        correct_cnt += 1
    else:
        print('땡')
        winsound.PlaySound('./bad.wav', winsound.SND_FILENAME)

    n += 1 

end = time.time()

game_time = end - start # 게임 진행 시간 

game_time = format(game_time, '.2f') # 소수점 둘째자리 까지 출력

if correct_cnt >= 3:
    print('합격')
else:
    print('불합격')

print(f'게임 시간: {game_time}초, 정답수 : {correct_cnt}개')

# DB 기록하기
cur.execute("INSERT INTO records('cor_cnt', 'time_rec', 'regdate') \
                VALUES(?,?,?)", (correct_cnt, game_time, \
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))