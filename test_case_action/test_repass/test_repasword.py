from interface import repassword


def test_repasswords():
    """
    测试发送验证码以及密码重置功能
    :return:
    """
    response = repassword.password_forget()
    assert response['code'] == 0