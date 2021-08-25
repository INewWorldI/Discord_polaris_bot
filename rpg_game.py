from datetime import date
import discord
from database import conn
from bot import bot
from database import conn
from discord.ext import commands

# 커서 획득
c = conn.cursor()

# 턴제 RPG 게임 구현

class user_data: # 개체 플레이어 타입 인스턴스 생성
    def __init__(self, uuid, ulevel, uhp, umana, uattack, udefense, uskill_name, uskill_damage):
        self.uuid = uuid
        self.ulevel = ulevel
        self.uhp = uhp
        self.umana = umana
        self.uattack = uattack
        self.udedense = udefense
        self.uskill_name = uskill_name
        self.uskill_damage = uskill_damage


class monstaer_data: # 개체 몬스터 타입 인스턴스 생성
    def __init__(self, level, hp, mana, attack, defense, skill_name, skill_damage):
        self.level = level
        self.hp = hp 
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.skill_name = skill_name
        self.skill_damage = skill_damage
    
# 몬스터 설정 생성 

slime = monstaer_data(level=1, hp=20, mana=40, attack=8, defense=0, skill_name='산성액 분출', skill_damage=20)
bat = monstaer_data(2, 20, 50, 10, 0.2, '흡혈', 25)
goblin = monstaer_data(5, 50, 100, 25, 0.4, '난타', 40)
gargoyle = monstaer_data(20, 100, 170, 50, 0.6, '석화', 250)
eins = monstaer_data(40, 1500, 0, 0, 0, '섹드립', 0)
red_dragon = monstaer_data(100, 1000, 2500, 350, 0.8, '드래곤 브레스', 550)

@bot.command()
async def 게임(ctx, *args):

    args = args[0]

    print(args)
    
    if args == '도움말':
        await ctx.send("""
        `$게임 도움말`: 해당 게임 시스템에 대해서 설명합니다.
        `$게임 내정보`: 게임의 내 정보를 확인합니다.
        `게임 시스템`: 어쩌구 저쩌구 """)
    
    elif args == '내정보':
        
        pid = conn.execute("SELECT * FROM user_data")

        # uuid 테이블에 유저 데이터가 있는지 체크 없으면 생성
        if ctx.message.author.id == pid:
            await ctx.send('데이터가 있습니다.')
        
        else:
            await ctx.send('데이터가 존재하지 않습니다 새 데이터를 생성합니다.')
            conn.execute("INSERT INTO user_data VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (ctx.message.author.id, 1, 20, 20, 8, 0, 0, 0))
            await ctx.send('데이터 생성에 성공했습니다 명령어를 다시 작성하세요')
    

# 만약에 에러가 발생된다면 값을 반환
@게임.error
async def rpg_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send('잘못된 명령어 사용입니다. `&게임 도움말`을 통해 사용하세요')
