import requests


def deduction():
    """
    扣费接口，需要打开922客户端环境
    :return:
    """
    header = {
        'Host': '127.0.0.1:9049',
        'session-id': '8a0c48200068f06d141d7627356c28ba',
        'auth-name': 'socks5',
        'platform': 'pc',
        'oem': '922',
        'language': 'Chinese',
        'time-zone': 'China Standard Time',
        'channel': 'normal',
        'uid': '67600',
        'sign': '410b7aa73763e08dbebd2e31c7571cca',
        'lang': 'zh-tw',
        'union-id': 'a7831f479037296cd1b579c631b9f9bc',
        'version': '152',
        'timestamp': '1703748598',
        'username': '37151829',
        'MIME-Version': '1.0',
        'Content-Length': '266',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en,*',
        'User-Agent': 'Mozilla/5.0',
    }

    files = {
        # username
        'user_session': (None, 'ehsHGXgxfQd9Uw8Nawhsb218UQlAD25GYzsHPms+fioCIQwdRjo='),
        'area': (None, 'US-houstonk-texas'),
        # union-id
        'session_id': (None, 'a7831f479037296cd1b579c631b9f9bc'),
        'port': (None, '30001'),
        'sn': (
        None, 'fVwwCX43d1poYCYLK2dZWCwEJA57DHhRLjJyBX1/Kgx+SyAIfzR8An9jBAR6WUdQaXABb2F2bV90KlYVVDp1cmEFfRNeJw=='),
        'server': (None, 'f2cHFHlTIRV+XgdLKDBtRnlSflR3D0BfYExveWQPTERlJwASWzNJHHcABDJFNg=='),
        'ip': (None, '73.32.215.99'),
        'forward': (None, 'LHZ7QXplMwN8XX4We10jAXxPWlMqYSJOfmJ3AnZXC2NhDw1rVC5tJQYlUnhtBQRzagc='),
        'sync': (None, '0'),
    }

    url = 'http://127.0.0.1:9049/api/set_port_session'

    resps = requests.post(url, headers=header, files=files)

    print(resps.text)