import requests
from params import data

#参数类实例化
Config_DATA = data.Config()
test_header,test_version = Config_DATA.test_version()

def CheckVersion():
    """
    版本检测
    :return:预留返回值，后续测试需要取参
    """
    #接口地址
    endpoint = "/v2/check_version"
    url = f"{Config_DATA.PC_url}{endpoint}"

    # 构建请求头,version也可以修改110， --version 110
    headers = test_header

    # 构建请求体
    # 在 requests 库中，当你使用 files 参数来传递文件或表单数据时，它会根据你提供的内容自动生成合适的请求头,若非必要不要手动添加Content-Type#
    files = {
        'version': (None, f'{test_version}'),
        'type': (None, 'install'),
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, files=files)

    action = Config_DATA.interface_action(response)
    code = action['code']
    msg = action['msg']
    ret_data = action['ret_data']

    return code,msg,ret_data

print(CheckVersion())