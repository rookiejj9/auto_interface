from interface import get_isp


def test_get_isp():
    """
    code及msg断言
    :return:
    """
    data, _, _, _ = get_isp.get_isp_data()
    code = data['code']
    msg = data['msg']
    assert code == 0 and msg == 'Success'
    print(data)
