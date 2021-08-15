import discord
from bot import bot
from discord.ext import commands

# 턴제 RPG 게임 구현

class rpg_ustat: # 개체 플레이어 타입 인스턴스 생성
    def __init__(self, ulevel, uhp, umana, uattack, udefense, uskill_name, uskill_damage):
        self.ulevel = ulevel
        self.uhp = uhp
        self.umana = umana
        self.uattack = uattack
        self.udedense = udefense
        self.uskill_name = uskill_name
        self.uskill_damage = uskill_damage


class rpg_mstat: # 개체 몬스터 타입 인스턴스 생성
    def __init__(self, level, hp, mana, attack, defense, skill_name, skill_damage):
        self.level = level
        self.hp = hp 
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.skill_name = skill_name
        self.skill_damage = skill_damage
    
# 몬스터 설정 생성 

slime = rpg_mstat(level=1, hp=20, mana=40, attack=8, defense=0, skill_name='산성액 분출', skill_damage=20)
bat = rpg_mstat(2, 20, 50, 10, 0.2, '흡혈', 25)
goblin = rpg_mstat(5, 50, 100, 25, 0.4, '난타', 40)
gargoyle = rpg_mstat(20, 100, 170, 50, 0.6, '석화', 250)
eins = rpg_mstat(40, 1500, 0, 0, 0, '섹드립', 0)
red_dragon = rpg_mstat(100, 1000, 2500, 350, 0.8, '드래곤 브레스', 550)

@bot.command()
async def 게임(ctx, *, arg):
    
    # 명령어를 완성시키지 못했을 때 도움말 을 치도록 유도
    if arg in None:
        await ctx.send('RPG 게임을 시작하시려면 `&게임 도움말`을 입력하세요.')
    
    elif arg in '도움말':
        await ctx.send("""`$게임 정보`: 해당 게임 시스템에 대해서 설명합니다.
                          `$게임 내정보`: 게임의 내 정보를 확인합니다.
                          `게임 시스템`: 어쩌구 저쩌구 """)
    
    elif arg in '내정보':
        await ctx.send('가나다라마바사')

    

# 만약에 에러가 발생된다면 값을 반환
@게임.error
async def rpg_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('잘못된 명령어 사용입니다. `&게임 도움말`을 통해 사용하세요')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('잘못된 명령어 사용입니다. `&게임 도움말`을 통해 사용하세요')
