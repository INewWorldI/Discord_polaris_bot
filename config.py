import yaml
from os import path

# 봇 설정 파일 생성 및 설정

CONFIG = {
    'bot_token': 'please enter your token here'
}

if not path.isfile('config.yaml'):
    # 설정 파일이 없으면 기본 설정 생성하고 종료
    with open('config.yaml', 'w') as cfg:
        yaml.dump(CONFIG, cfg)
    
    print('설정 파일을 생성했습니다. 설정 후 다시 실행해주세요')

    exit(-1)

# 설정 파일이 있으면 불러오기
with open('config.yaml', 'r') as cfg:
    CONFIG = yaml.load(cfg.read(), Loader=yaml.Loader)

token = CONFIG.get('bot_token')

if token is None or len(str(token).strip()) == 0:
    print("설정 파일 내에 bot_token이 없습니다. ㅇㄹㅇㅇㅇㄴㅁㄹㄹ")    

