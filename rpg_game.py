from datetime import date
from os import putenv
import discord
from bot import bot
from database import conn
from discord.ext import commands

# 커서 획득
c = conn.cursor()

# 턴제 RPG 게임 구현

class user_data: # 개체 플레이어 타입 인스턴스 생성
    def __init__(self, uuid, ulevel, uhp, umana, uattack, udefense, uskill_id):
        self.uuid = uuid
        self.ulevel = ulevel
        self.uhp = uhp
        self.umana = umana
        self.uattack = uattack
        self.udedense = udefense
        self.uskill_id = uskill_id


class skill_data:
    def __init__(self, skill_id, skill_name, skill_desc, skill_damage, skill_ctime):
        self.skill_id = skill_id
        self.skill_name = skill_name
        


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
    
    if args == '도움말':
        await ctx.send("""
        `$게임 도움말`: 해당 게임 시스템에 대해서 설명합니다.
        `$게임 내정보`: 게임의 내 정보를 확인합니다.
        `게임 시스템`: 어쩌구 저쩌구 """)
    
    elif args == '내정보':
        
        # DB에서 uuid 테이블의 모든 정보를 가져옴
        uuid_sql= "SELECT uuid FROM user_data WHERE uuid=?"
        c.execute(uuid_sql, (ctx.message.author.id,))
        uuid_table = c.fetchall()
        uuid_data = tuple(*uuid_table)


        # uuid 테이블에 유저 데이터가 있는지 체크 없으면 생성

        if ctx.message.author.id in uuid_data:

            # 유저의 아바타 이미지 링크를 임베드에 넣기 위해 설정
            avatar_url = ctx.message.author.avatar_url

            # 임베드에 각종 스테이터스를 담기 위해 DB에서 조회및 데이터 호출
            stat_sql = "select * from user_data where uuid=?"
            c.execute(stat_sql, (ctx.message.author.id,))
            stat_table = c.fetchall()
            stat_data = tuple(*stat_table) 
            
            embed=discord.Embed(title=f"[Lv.{stat_data[1]}] {ctx.message.author.name}의 정보", description="플레이어의 스테이터스 데이터를 표시했습니다.", color=0xFF5733)
            embed.set_author(name=f"{ctx.message.author.name}", icon_url=f"{avatar_url}")
            embed.set_thumbnail(url="https://www.mikufan.com/wp-content/uploads/2021/01/cfm_mikuexpo2021online_2_prev.jpg")
            embed.add_field(name="체력", value=f"[ +{stat_data[2]} ]", inline=True)
            embed.add_field(name="마나", value=f"[ +{stat_data[3]} ]", inline=True)
            embed.add_field(name = chr(173), value = chr(173))
            embed.add_field(name="공격력", value=f"[ +{stat_data[4]} ]", inline=True)
            embed.add_field(name="방어력", value=f"[ +{stat_data[5]} ]", inline=True)
            embed.add_field(name = chr(173), value = chr(173))
            embed.add_field(name="보유스킬", value=f"패치중...", inline=True)
            await ctx.send(embed=embed)

        else:
             await ctx.send('데이터가 존재하지 않습니다 새 데이터를 생성합니다...')
             conn.execute("INSERT INTO user_data VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (ctx.message.author.id, 1, 20, 20, 8, 0, 0, 0))
             await ctx.send('완료!! 데이터 생성에 성공했습니다 명령어를 다시 입력하세요')
    

# 만약에 에러가 발생된다면 값을 반환
# @게임.error
# async def rpg_error(ctx, error):
#     if isinstance(error, commands.CommandError):
#         await ctx.send('잘못된 명령어 사용입니다. `&게임 도움말`을 통해 사용하세요')
