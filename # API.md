# API

API라는건 어떤 기능을 제공하는데 그 목적이 있음 - 결국 중요한 것은 어떤 기능을 어떤 형태로 제공하는지 파악하는게 핵심

## API를 사용하는 두 가지 일반적인 방법

- API를 직접 사용한다
- SDK를 사용한다

### API를 직접 사용하는 방법

메뉴얼 보고 그냥 잘 쓰면 됨
 
네트워크를 통한 방법들:

- HTTP(또는 Websocket이나 grpc)를 통한 방법(제일 흔함)
- TCP/UDP 위에서 자체 프로토콜을 사용하는 방법 (OSI 7계층에서 7레벨 `Application`에 해당) e.g. DBMS

네트워크를 통하지 않는 방법:

- Plugin 서비스를 사용하는 방법 e.g. 마인크래프트 서버 플러그인
- 자체 함수를 제공하는 방법

### SDK를 사용하는 방법

API를 직접 쓰기가 어렵고 복잡해! 더 간단한 방법은 없나? -> SDK의 등장

SDK는 일반적으로 프로그래밍 언어를 사용해서 API를 사용하려 할 때 제공됨. 같은 API여도 언어/환경마다 개별 SDK를 제공하는 경우가 일반적임. e.g. AWS SDK for Javascript/Go/Java/C#/PHP/...

SDK는 내부적으로 자체 API를 호출하는 기능을 포함하고 있음. 단지 이를 더 쉽게 사용할 수 있도록 하는데 그 목적이 있다. 다시 말해서, SDK 없이도 API를 그냥 쓸 수도 있다! SDK는 필수는 아님.

SDK는 일반적으로 API를 제공하는 곳에서 같이 제공한다. 그렇지만 아닌 경우도 있다. e.g. discord

## discord를 통해 API를 써보자

여기서는 discord의 API를 그 예시로써 직접 사용해보도록 하자.

### SDK를 사용하는 경우

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [discord.js](https://discord.js.org/)

자기가 쓸 언어와 환경에 따라서 적절한 SDK를 선택하고 문서대로 따라서 사용하면 된다.

### API를 직접 사용하는 경우

[이 문서](https://discord.com/developers/docs/reference)를 보고 직접 사용해보자. 행운을 빈다...
