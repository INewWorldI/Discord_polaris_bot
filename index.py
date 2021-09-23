from config import CONFIG
from bot import bot
import rps_game # 가위바위보 게임 Load
import rpg_game # 폴라리스 판타지 게임 Load
import database # 데이터베이스 관련 Load
import discord # discord API load
from nextcord.ext import commands # discord ext load

# 설정 가지고 뭔가 함
print('config loaded:', CONFIG)

@bot.event 
async def on_ready():
    print(f'서버에 {bot.user} 봇으로 접속했습니다')
    print('현재 버전은 {0} 입니다'.format(CONFIG.get('bot_version')))

bot.run(CONFIG.get('bot_token'))
