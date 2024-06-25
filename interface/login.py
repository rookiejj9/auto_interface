import requests
from params import data

config = data.Config()
header, version = config.test_version()


def login_request():
    """
    登录接口
    :return:
    """
    endpoint = "/v2/user/login"
    url = f'{config.PC_url}{endpoint}'
    header['session-id'] = ''
    header['username'] = '510999593@qq.com'

    files = {
        'email': (None, '510999593@qq.com'),
        'password': (None, 'Li@199789')
    }

    response = requests.post(url=url, headers=header, files=files)

    if response.status_code == 200:
        # print(response.json())
        return response.json()['ret_data']
    else:
        print(f"请求登录失败，{response.status_code},{response.json()}")