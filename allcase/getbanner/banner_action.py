from interface import banner


def banner_data():
    """
    海报返回链接处理
    :return:
    """
    data = banner.get_banner()
    datalist = {}
    for member in data:
        member_id = member['id']
        datalist.setdefault(member_id, []).append({'img': member['img'], 'jump_url': member['jump_url']})

    link = datalist[2]

    return link
