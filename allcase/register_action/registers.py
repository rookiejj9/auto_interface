from interface import register
import re


def register_data():
    """
    注册数据
    :return:链接网址，和其他的用户数据
    """
    ret_data = register.reister_user()
    url = re.compile(r'^(https?://\S+)$')
    link = {}
    other = {}

    for key, value in ret_data.items():
        if isinstance(value, str):
            if url.match(value):
                link[key] = value
            else:
                other[key] = value
        elif isinstance(value, dict):
            other[key] = value
            for key2, value2 in value.items():
                if isinstance(value2, str):
                    if url.match(value2):
                        link[key2] = value2
        else:
            other[key] = value

    return link, other
