import requests
import time
from params import MD
from allcase.get_isp import get_isp_action


def extractip():
    """
    上报提取IP
    :return:
    """
    tiqu, head, config = get_isp_action.getisp()
    endpoint = "/api/put_tl"
    url = f"{config.res_url1}{endpoint}"
    bind_name = int(time.time())

    ip = MD.MdDecode(tiqu[-1],'a8b1c1J9Q2K2')
    print(ip)

    files = {
        'username': (None, f"{tiqu[4]}"),
        'bind_name': (None,f'{bind_name}'),
        'sn': (None, f'{tiqu[3]}'),
        'server': (None, f'{tiqu[5]}'),
        'ip': (None, f'{tiqu[-1]}'),
        'country': (None, f'{tiqu[1]}'),
        'state': (None, f'{tiqu[-2]}'),
        'city': (None, f'{tiqu[2]}'),
        'area': (None, f'{tiqu[0]}'),
        'cate': (None, ''),
    }

    response = requests.post(url, files=files, headers=head)
    print(response.text)

