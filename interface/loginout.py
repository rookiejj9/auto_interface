import requests
from allcase.login_action import user_logindata
from params import data

#初始化数据
config = data.Config()
header, version = config.test_version()


def logout():
    """
    退出登录
    :return:
    """
    # 更新头部
    link, logindata = user_logindata.login_data()

    print(logindata['session_id'])
    sesion = logindata['session_id']
    uid = str(logindata['info']['uid'])
    username = logindata['info']['username']
    header['session-id'] = sesion
    header['uid'] = uid
    header['username'] = username

    # 更新url
    base_url = config.PC_url
    endpoint = "/v1/logout"
    url = f'{base_url}{endpoint}'

    files = {
        '': (None, ''),
    }

    response = requests.post(url, headers=header, files=files)

    return response.json()