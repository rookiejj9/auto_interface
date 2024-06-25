import requests
from params import data

config_partner = data.Config()
test_header, test_version = config_partner.test_version()

def get_partner():
    """
    获取合作伙伴
    :return: 合作伙伴的列表
    """
    endpoint = "/v2/msg/partner"
    url = f"{config_partner.PC_url}{endpoint}"

    headers = test_header

    files = {
        "limit": (None, "10"),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        response_data = response.json()
        ret_data = response_data["ret_data"]
        return ret_data
    else:
        print("接口访问失败！")