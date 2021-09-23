import sqlite3
from sqlite3.dbapi2 import SQLITE_UPDATE

# DB 생성 (오토 커밋)
conn = sqlite3.connect("rpg_game.db", isolation_level=None)

# 커서 획득
c = conn.cursor()

# 플레이어 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS user_data(
    user_uuid integer PRIMARY KEY,
    user_level integer,
    user_exp integer,
    user_hp integer,
    user_mp integer,
    user_atk integer,
    user_def integer,
    user_money integer,
    user_class text, 
    user_inv text null,
    user_eqip text null
)''')

# 직업 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS class_data(
    class_id text PRIMARY KEY,
    class_name text,
    class_desc text,
    class_skill text null
)''')

# 레벨 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS level_data(
    level_name integer PRIMARY KEY,
    level_exp integer
)''')

# 스킬 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS skill_data(
    skill_id       text PRIMARY KEY,
    skill_name     text,
    skill_desc     text,
    skill_value    integer,
    skill_criticul real,
    skill_ctime    integer,
    skill_userpt   int
)''')

# 상점 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS shop_data(
    item_id text PRIMARY KEY,
    item_name text, 
    item_desc text,
    item_price integer
)''')

# 던전 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS dungeon_data(
    dgn_id text PRIMARY KEY,
    dgn_name text, 
    dgn_desc text,
    dgn_mobs_form text null,
    dgn_stage_form text null
)''')

# 몬스터 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS monster_data(
    mb_id text PRIMARY KEY,
    mb_name text,
    mb_desc text,
    mb_chance real,
    mb_text text
)''')

# 스테이지 테이블 생성
c.execute('''
CREATE TABLE IF NOT EXISTS stage_data(
    stg_id text PRIMARY KEY,
    stg_name text,
    stg_desc text,
    stg_chance real,
    stg_info text
)''')