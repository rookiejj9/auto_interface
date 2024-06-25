from allcase.register_action import registers
from params import data

config = data.Config()


def test_userregister():
    """
    测试用户注册
    :return:
    """
    link, others = registers.register_data()

    for key, url in link.items():
        print(f"\n要测试的链接是{key}")
        code = config.check_url(url)
        assert code == 200