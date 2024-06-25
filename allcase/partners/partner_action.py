from interface import partner

def partner_data():
    """
    处理合作伙伴数据
    :return:
    """
    #接收合作伙伴作为列表
    AdsPower, Hubstudio, BitBrowser = partner.get_partner()

    partner_member = {"browser": partner.get_partner()}

    partners = {browser['name']: {'logo': browser['logo'], 'url': browser['url'], 'img': browser['img']}for browser in partner_member["browser"]}

    return partners

print(partner_data())
    # partner_member = [AdsPower, Hubstudio, BitBrowser]
    #
    # #创建合作伙伴链接
    # AdsPowerlist = []
    # Hubstudiolist = []
    # BitBrowserslist = []
    #
    # AdsPowerlink = []
    # Hubstudiolink = []
    # BitBrowserslink = []

    #遍历合作伙伴成员
    # link_match = re.compile(r'^(https?://\S+)$')
    # for member in partner_member:                  #对字典集合遍历
    #     for key, value in member.items():          #对单个字典遍历
    #         if value == 'AdsPower':                #区分是那个合作伙伴
    #             for ads in AdsPower.values():      #继续对当前合作伙伴遍历（和上层for循环的字典重复了，暂时没想到什么方法）
    #                 AdsPowerlist.append(ads)
    #                 if isinstance(ads, str):
    #                     if link_match.match(ads):
    #                         AdsPowerlink.append(ads)
    #         elif value == 'Hubstudio':
    #             for Hub in Hubstudio.values():
    #                 Hubstudiolist.append(Hub)
    #                 if isinstance(Hub, str):
    #                     if link_match.match(Hub):
    #                         Hubstudiolink.append(Hub)
    #         elif value == 'BitBrowser':
    #             for Bit in BitBrowser.values():
    #                 BitBrowserslist.append(Bit)
    #                 if isinstance(Bit, str):
    #                     if link_match.match(Bit):
    #                         BitBrowserslink.append(Bit)
    #
    # return AdsPowerlink,Hubstudiolink, BitBrowserslink
    # data_list = [AdsPowerlink,Hubstudiolink,BitBrowserslink]
    # print(data_list)
    #
    # member_list = [AdsPowerlist,Hubstudiolist,BitBrowserslist]
    # print(member_list)