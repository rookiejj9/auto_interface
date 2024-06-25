from interface.Initialization_Interfaces import Initialization_Interface
import re


def link_action():
    """
    测试初始化接口的链接
    :return: 返回客户端所需链接及其他所需数据
    """

    mydict = Initialization_Interface()
    url_pattern = re.compile(r'^(https?://\S+)$')

    # 其他数据
    other_data = {}
    # 链接数据
    link_data = {}

    for key, value in mydict.items():
        # 检查值是否是字符
        if isinstance(value, str):
            if url_pattern.match(value):
                link_data[key] = value
            else:
                other_data[key] = value
        elif isinstance(value, dict):
            help_dict = value
            for help_key, help_value in help_dict.items():
                if isinstance(help_value, str):
                    if url_pattern.match(help_value):
                        link_data[help_key] = help_value
                    else:
                        other_data[help_key] = help_value
                else:
                    other_data[key] = value
        else:
            other_data[key] = value
    # print(other_data)
    # print(link_data)
    return link_data, other_data

# link_action()
