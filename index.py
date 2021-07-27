from config import CONFIG
import discord
import random 
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

# 설정 가지고 뭔가 함
print('config loaded:', CONFIG)

@bot.event 
async def on_ready():
    print('서버에 {0.user} 봇으로 접속했습니다'.format(bot))
    print(f'현재 버전은 {0} 입니다'.format(CONFIG.get('bot_version')))

@bot.command()
#가위바위보 게임 구현 함수
async def 가위바위보(ctx, *arg):

    const_list = ['가위', '바위', '보']
    
    if arg in const_list:
        rnd_var = random.choice(const_list)
        await ctx.send(f'당신은 {arg}를 냈습니다')

        if arg in '가위':
            await ctx.send(f'봇이 {rnd_var}를 냈습니다')
            if rnd_var in '가위':
                await ctx.send('가위 = 가위 :: 당신은 비겼습니다. ')
            elif rnd_var in '바위':
                await ctx.send('가위 < 바위 :: 당신은 졌습니다.')
            elif rnd_var in '보':
                await ctx.send('가위 > 보 :: 당신은 이겼습니다.')

        elif arg in '바위':
            await ctx.send(f'봇이 {rnd_var}를 냈습니다')
            if rnd_var in '가위':
                await ctx.send('바위 > 가위 :: 당신은 이겼습니다.')
            elif rnd_var in '바위':
                await ctx.send('바위 = 바위 :: 당신은 비겼습니다.')
            elif rnd_var in '보':
                await ctx.send('바위 < 보 :: 당신은 졌습니다.')

        elif arg in '보':
            await ctx.send(f'봇이 {rnd_var}를 냈습니다')
            if rnd_var in '가위':
                await ctx.send('가위 > 보 :: 당신은 졌습니다.')
            elif rnd_var in '바위':
                await ctx.send('보 > 바위 :: 당신은 이겼습니다.')
            elif rnd_var in '보':
                await ctx.send('보 = 보 :: 당신은 비겼습니다.')

    else:
        await ctx.send('가위, 바위, 보 중에 하나를 입력해주세요')

bot.run(CONFIG.get('bot_token'))
