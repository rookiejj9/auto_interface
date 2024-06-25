from interface import loginout


def test_loginouts():
    """
    退出登录
    :return:
    """
    response = loginout.logout()

    assert response['code'] == 1
    print("退出成功！")

