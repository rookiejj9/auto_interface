import requests
from params import data

Config = data.Config()
header, version = Config.test_version()

def get_language():
    """
    获取语言包
    :return:
    """
    endpoint = "/v2/support_la"
    url = f"{Config.PC_url}{endpoint}"

    headers = header

    files = {
        "": (None, ""),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        print("接口访问成功")
        return response.json()["ret_data"]
    else:
        print(f"接口访问失败，状态码为{response.status_code}")

get_language()