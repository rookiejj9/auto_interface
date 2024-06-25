import pytest
import requests
from params.data import Config
from allcase.initialization_interface_action import initialization_action

#******************************批量执行测试用例并且生成测试报表*******************************#
#*************pytest test_version_action_case1.py -s -q --alluredir=./result************#
#***************************allure serve ./result/**************************************#

link , data = initialization_action.link_action()
Config_DATA = Config()

def test_link():
    """
    测试初始化接口链接
    :return:
    """
    for key,value in link.items():
        code = Config_DATA.check_url(value)
        assert code == 200
        print(f"{key}访问成功！")

