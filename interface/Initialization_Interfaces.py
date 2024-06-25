import requests
from params import data


Config_DATA = data.Config()
test_header,test_version = Config_DATA.test_version()

def Initialization_Interface():
    """
    初始化接口
    :return: 接口返回code、ret_data
    """

    # 初始化接口
    endpoint = "/v1/config"
    url = f"{Config_DATA.PC_url}{endpoint}"

    headers = test_header

    files = {
        "": (None, ""),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        ret_data = response_data["ret_data"]
        return ret_data
    else:
        print(f"初始化接口访问失败！接口返回码是{response.status_code}")

Initialization_Interface()