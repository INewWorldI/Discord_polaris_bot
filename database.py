import sqlite3
from sqlite3.dbapi2 import SQLITE_UPDATE

# DB 생성 (오토 커밋)
conn = sqlite3.connect("rpg_game.db", isolation_level=None)

# 커서 획득
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS user_data(
    uuid integer PRIMARY KEY,
    ulevel integer,
    uexp integer,
    uhp integer,
    umana integer,
    uattack integer,
    udefense integer,
    umoney integer
)''')

c.execute('''
CREATE TABLE IF NOT EXISTS class_data(
    class_uuid integer PRIMARY KEY,
    class_id integer,
    class_desc text,
    class_url text null,
    class_skill_data text null
)''')