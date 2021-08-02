import discord
import random
from bot import bot

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
async def rpg(ctx, *args):
    await ctx.send('디스코드 봇으로 간단하게 구현하는 RPG 게임 시스템 입니다.')

    if args in 'info':
        username = bot.get_user()
        await ctx.send('내 정보를 출력합니다')
        await ctx.send(f'내 이름 {username}')
