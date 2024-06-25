import requests
from allcase.login_action import user_logindata
from params import data


base_data = data.Config()
baseheader, baseversion = base_data.test_version()


def get_banner():
    """
    海报获取接口
    :return:
    """
    endpoint = '/v1/banner'
    url = f"{base_data.PC_url}{endpoint}"

    # 更新头部
    link, logindata = user_logindata.login_data()
    sesion = logindata['session_id']
    uid = str(logindata['info']['uid'])
    username = logindata['info']['username']
    baseheader['session-id'] = sesion
    baseheader['uid'] = uid
    baseheader['username'] = username

    files = {
        '': (None, ''),
    }

    response = requests.post(url, headers=baseheader, files=files)

    if response.status_code == 200:
        return response.json()['ret_data']
    else:
        print(f"获取海报接口请求失败{response.status_code}")
