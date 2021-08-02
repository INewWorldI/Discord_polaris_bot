import random
from bot import bot

@bot.command()
#가위바위보 게임 구현 함수
async def 가위바위보(ctx, *arg):
    const_list = ['가위', '바위', '보']

    if len(arg) != 1:
        await ctx.send('잘못된 사용법입니다. `$가위바위보 가위` 형태로 입력해주세요.')
        return

    arg = arg[0]
    
    comm_list = ('가위', '바위', '보')
    print(f'comm_list: {comm_list}')
    print(f'arg: {arg}')
    print(f'not in: {arg not in comm_list}')

    if arg not in comm_list:
        await ctx.send('가위, 바위, 보 중에 하나를 입력해주세요')
        return

    bot_select = random.choice(comm_list)
    await ctx.send(f'당신은 {arg}를 냈습니다')

    if arg in '가위':
        await ctx.send(f'봇이 {bot_select}를 냈습니다')
        if bot_select in '가위':
            await ctx.send('가위 = 가위 :: 당신은 비겼습니다. ')
        elif bot_select in '바위':
            await ctx.send('가위 < 바위 :: 당신은 졌습니다.')
        elif bot_select in '보':
            await ctx.send('가위 > 보 :: 당신은 이겼습니다.')

    elif arg in '바위':
        await ctx.send(f'봇이 {bot_select}를 냈습니다')
        if bot_select in '가위':
            await ctx.send('바위 > 가위 :: 당신은 이겼습니다.')
        elif bot_select in '바위':
            await ctx.send('바위 = 바위 :: 당신은 비겼습니다.')
        elif bot_select in '보':
            await ctx.send('바위 < 보 :: 당신은 졌습니다.')

    elif arg in '보':
        await ctx.send(f'봇이 {bot_select}를 냈습니다')
        if bot_select in '가위':
            await ctx.send('가위 > 보 :: 당신은 졌습니다.')
        elif bot_select in '바위':
            await ctx.send('보 > 바위 :: 당신은 이겼습니다.')
        elif bot_select in '보':
            await ctx.send('보 = 보 :: 당신은 비겼습니다.')

