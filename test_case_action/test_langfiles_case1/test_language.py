from allcase.langfile_action import language_action
from params import data

def test_language():
    """
    断言国家代码、语言包、国家图片
    :return:
    """
    config = data.Config()
    langfile = language_action.get_langlink()

    for country,link in langfile.items():
        print(f"\n检测{country}语言包")
        for link in link.values():
            code = config.check_url(link)
            assert code == 200

