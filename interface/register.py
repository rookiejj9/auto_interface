import requests
from params import data


config_data = data.Config()
headers, version = config_data.test_version()


def reister_user():
    """
    注册接口
    :return: ret_data
    """
    endpoint = "/v2/user/register"
    url = f"{config_data.PC_url}{endpoint}"
    email = config_data.email_random()
    headers['session-id'] = ''

    files = {
        'email': (None, f'{email}'),
        'password': (None, 'Li@199789'),
        're_password': (None, 'Li@199789'),
        'code': (None, ''),
        'inviter_code': (None, ''),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        print(response.json())
        return response.json()['ret_data']
    else:
        print(f"请求登录失败，{response.status_code},{response.json()}")

