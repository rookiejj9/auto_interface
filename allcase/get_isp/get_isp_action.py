from interface import get_isp

def getisp():
    """
    获取返回IP数据处理
    :return:
    """
    ipdata, user, head, config = get_isp.get_isp_data()
    ip = ipdata['data'][0]['ip']
    country = ipdata['data'][0]['country']
    city = ipdata['data'][0]['city']
    server = ipdata['data'][0]['server']
    sn = ipdata['data'][0]['server']
    state = ipdata['data'][0]['state']
    area = f"{country}-{city}-{state}"
    tiqu = [area, country, city, sn, user, server, state, ip]

    return tiqu, head, config

print(getisp())