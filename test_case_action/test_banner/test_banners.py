import requests
from allcase.getbanner import banner_action


def test_bannerlink():
    """
    断言海报链接
    :return:
    """

    link = banner_action.banner_data()

    for values in link:
        for links in values.values():
            resp = requests.get(links)
            assert resp.status_code == 200
