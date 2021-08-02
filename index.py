from config import CONFIG
from bot import bot
import command
#import rpg_game
import discord
from discord.ext import commands

# 설정 가지고 뭔가 함
print('config loaded:', CONFIG)

@bot.event 
async def on_ready():
    print(f'서버에 {bot.user} 봇으로 접속했습니다')
    print('현재 버전은 {0} 입니다'.format(CONFIG.get('bot_version')))

bot.run(CONFIG.get('bot_token'))
