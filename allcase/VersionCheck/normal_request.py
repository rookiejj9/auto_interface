from interface import VersionCheck
import requests

code, msg, ret_data = VersionCheck.CheckVersion()

def check_not_update():
    """
    版本检测不需要更新
    :return:code, msg, ret_data
    """
    print(msg)

    return code, msg


def check_update():
    """
    版本检测需要更新
    :return:弹窗文案、下载地址
    """
    #升级弹窗文案消息
    Popup_Messages = ret_data['desc']

    #下载链接
    update_url = ret_data['down_url']

    return code,msg,Popup_Messages, update_url
