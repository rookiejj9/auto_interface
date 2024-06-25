from interface import language

def get_langlink():
    """
    获取国家代码、语言包、国家图片
    :return: 包含语言包、国家图片的连接的国家列表
    """
    ret_data = {"ret_data": language.get_language()}

    country_language = {country['code']: {'img' : country['img'], 'file': country['url']}for country in ret_data["ret_data"]}

    return country_language