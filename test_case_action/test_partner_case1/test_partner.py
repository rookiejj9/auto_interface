from allcase.partners import partner_action
from params import data

Config_DATA = data.Config()

def test_partner_action():
    """
    断言合作伙伴的图片跳转链接
    :return:
    """

    member_links = partner_action.partner_data()

    for member,member_links in member_links.items():
        print(f"\n检测{member}的链接")
        for link in member_links.values():
            code = Config_DATA.check_url(link)
            assert code == 200