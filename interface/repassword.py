from params import data
import requests

config = data.Config()
header, version = config.test_version()
header['session-id'] = ''


def sand_email():
    """
    发送查询邮件
    :return:最新的邮件验证码
    """
    endpoint = "/v2/user/send_code"
    url = f"{config.PC_url}{endpoint}"

    files = {
        'email': (None, '2023113001@qq.com'),
        'type': (None, 'find'),
    }

    response = requests.post(url, headers=header, files=files)
    print(response.text)
    if response.status_code == 200:
        connection = config.connect_mysql()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT `email_code` FROM `md_email_code` where `email` = '2023113001@qq.com' and `enable` = 'true' order by `expire_time` desc limit 1")

        emailcode = cursor.fetchall()
        cursor.close()
        connection.close()
        email = emailcode[0][0]
        return email
    else:
        print("访问发送邮件接口失败")


def password_forget():
    """
    忘记密码请求
    :return:
    """

    email = sand_email()
    endpoint = "/v2/user/forget"
    url = f"{config.PC_url}{endpoint}"

    files = {
        'email': (None, '2023113001@qq.com'),
        'password': (None, 'Li@199789'),
        're_password': (None, 'Li@199789'),
        'code': (None, f'{email}'),
    }

    response = requests.post(url, headers=header, files=files)

    if response.status_code == 200:
        return response.json()
        print(f'{response.json()}')
    else:
        print("访问忘记密码接口失败,请检查发送邮件接口或者忘记密码接口")

