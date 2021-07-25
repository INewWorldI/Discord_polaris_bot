from config import CONFIG
import discord

# 설정 가지고 뭔가 함
print('config loaded:', CONFIG)

bot = discord.Client()

@bot.event 
async def on_ready():
    print('서버에 {0.user} 봇으로 접속했습니다'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('hello!')

bot.run(CONFIG.get('bot_token'))
