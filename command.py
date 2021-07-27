import random 
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
#가위바위보 게임 구현 함수
async def 가위바위보(ctx, arg):
    
    if arg in ['가위', '바위', '보']:
        select_var = ['가위', '바위', '보']
        rnd_var = random.choice(select_var)
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
        print('가위, 바위, 보 중에 하나를 입력해주세요')
