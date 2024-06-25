import requests
from allcase.VersionCheck import normal_request
import pytest

#******************************批量执行测试用例并且生成测试报表*******************************#
#*************pytest test_version_action_case1.py -s -q --alluredir=./result************#
#***************************allure serve ./result/**************************************#



def test_not_update():
    """
    断言不需要更新
    :return:
    """

    code, msg = normal_request.check_not_update()

    assert code == 2
    assert msg == '不需要陞級'
    print(f'\n{code},{msg}')


# def test_update():
#     """
#     断言需要更新
#     :return:
#     """
#
#     code, msg, Popup_Messages, update_url = normal_request.check_update()
#
#     updatepackage = requests.get(update_url)
#     # if updatepackage.status_code == 200:
#     #     print("922客户端更新包下载链接请求成功，正在检测文件是否存在")
#     #     if len(updatepackage.content) > 0:
#     #         print("文件存在")
#     #     else:
#     #         print("文件不存在")
#     # else:
#     #     print(f"请求失败，状态码: {updatepackage.status_code}")
#
#     assert code == 0
#     assert msg == '發現新版本'
#     print("正在断言下载版本链接是否有效")
#     assert updatepackage.status_code == 200
#     assert len(updatepackage.content) > 0
#     print("响应版本下载链接访问成功")
#     print(f'\n响应码：{code},\n{msg},\n下载地址：{update_url},\n弹窗文案：\n{Popup_Messages}')