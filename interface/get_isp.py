import requests
from params import MD
from params import data
from interface import login


def prepare_data():
    """
    准备发送get_isp接口数据
    :return: 请求头、后端加密后的密码
    """

    config = data.Config()
    head = config.res_header
    ret_data = login.login_request()

    session_id = ret_data['session_id']
    pwd = ret_data['info']['pwd']

    head['session-id'] = session_id

    return head,  pwd, config

def get_isp_data():
    """
    获取get_isp接口数据
    :return:
    """
    head, pwd, config = prepare_data()
    endpoint = "/api/v2/get_line_list"
    url = f'{config.res_url1}{endpoint}'
    username = head['username']

    password = MD.MdEncode(pwd, 'a8b1c1J9Q2K2')

    user = MD.MdEncode(username, 'a8b1c1J9Q2K2')

    files = {
        'pwd': (None, f'{password}'),
        'user': (None, f'{user}'),
        'num': (None, '1'),
        'city': (None, ''),
        'postal': (None, ''),
        'state': (None, ''),
        'end_ip': (None, ''),
        'isp': (None, ''),
        'country': (None, ''),
        'start_ip': (None, ''),
    }

    response = requests.post(url=url, headers=head, files=files)
    if response.status_code == 200:
        return response.json(), user, head, config
    else:
        return None