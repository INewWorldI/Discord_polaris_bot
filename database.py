import sqlite3
from sqlite3.dbapi2 import SQLITE_UPDATE

# 데이터 베이스 정의
db = sqlite3.connect('rpg_game.db')

data = db.cursor()

data.execute('CREATE TABLE rpg_game_data(uuid integer, ulevel integer, uhp integer, uattack integer, udefense integer)')
