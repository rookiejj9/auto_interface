from allcase.login_action import user_logindata
from params import data

config = data.Config()


def test_loginuser():
    """
    测试用户注册
    :return:
    """
    link, others = user_logindata.login_data()
    print(link)
    for key, url in link.items():
        print(f"\n要测试的链接是{key}")
        code = config.check_url(url)
        assert code == 200