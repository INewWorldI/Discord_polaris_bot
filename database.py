import sqlite3
from sqlite3.dbapi2 import SQLITE_UPDATE

# DB 생성 (오토 커밋)
conn = sqlite3.connect("rpg_game.db", isolation_level=None)

# 커서 획득
c = conn.cursor()


# 테이블이 있는지 체크 후 생성이 안되있으면 생성
db_path = c.execute('SELECT * FROM rpg_game_data')

    #c.execute('CREATE TABLE rpg_game_data(uuid integer PRIMARY KEY, ulevel integer, uhp integer, uattack integer, udefense integer)')
    #print('데이터 베이스가 없어서 rpg_game.db를 생성했습니다.')

print(c.execute('SELECT * FROM rpg_game_data'))