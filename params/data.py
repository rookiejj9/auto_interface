import requests
import json
import random
import string
import mysql.connector


class Config:
    """
    测试共享参数,及公共方法
    """
    def __init__(self):
        """
        初始化共享数据,这个方法可有可无，纯粹为了提醒自己创建类还可以自定义类的特性参数
        :return: 共享域名
        """
        self.PC_url = ""
        self.res_url1 = ""
        self.basic_header = {
            'Host': '',
            'session-id': '',
            'auth-name': '',
            'platform': '',
            'oem': '',
            'language': '',
            'time-zone': '  ',
            'channel': '',
            'uid': '0',
            'sign': '',
            'lang': 'zh-tw',
            'union-id': '',
            'version': '',
            'timestamp': '',
            'username': '',
            'MIME-Version': '',
            'Content-Length': '',
            'Connection': '',
            'Accept-Encoding': '',
            'Accept-Language': '',
            'User-Agent': '',
        }
        self.res_header = {
            'Host': '',
            'session-id': '',
            'auth-name': '',
            'platform': '',
            'oem': '',
            'language': '',
            'time-zone': '',
            'channel': '',
            'uid': '',
            'sign': '',
            'lang': 'zh-tw',
            'union-id': '',
            'version': '',
            'timestamp': '',
            'username': '',
            'MIME-Version': '1.0',
            'Content-Length': '266',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en,*',
            'User-Agent': 'Mozilla/5.0',
        }


    def test_version(self):
        """
        获取测试版本号
        :return:
        """
        version = ''
        header = self.basic_header
        header['version'] = version

        return header, version


    def email_random(self):
        """
        生成随机邮箱
        :return:一个随机生成的邮箱名email
        """
        random_number = [random.randint(0, 10) for _ in range(5)]
        number = map(str, random_number)
        str_number = ''.join(number)

        random_abc = [random.choice(string.ascii_lowercase) for _ in range(5)]
        str_abc = ''.join(random_abc)
        email = str_number + str_abc + '@qq.com'
        return email

    def interface_action(self, resp):
        """
        接口处理
        :return:接口成功&失败的响应
        """
        statue_code = resp.status_code
        if statue_code // 100 == 2:
            respose_body = resp.json()
            print(f"\n请求成功")
            return respose_body
        else:
            print("\n请求失败")
            return resp.text

    def check_url(self, link):
        """
        请求连接处理方法
        :param link: 传入要测试的链接
        :return:请求状态code
        """
        try:
            response = requests.get(link)
            code = response.status_code
            # 检查HTTP状态码，200表示成功
            if response.status_code == 200:
                print(f"\n可以访问链接 {link}。")
                return code
            else:
                print(f"\n无法访问链接 {link}。\n状态码: {response.status_code}")
                return code
        except requests.ConnectionError:
            print(f"\n无法连接到链接 {link}。")
            return code

    def check_json_url(self, link):
        """
        json文件处理方法
        :param link: json下载链接
        :return: 解析
        """
        try:
            response = requests.get(link)
            # 检查HTTP状态码，200表示成功
            code = response.status_code
            if response.status_code == 200:
                try:
                    # 尝试解析JSON
                    json_data = response.json()
                    print(f"URL {link} 指向一个有效的 JSON 文件。")
                    return code
                except json.JSONDecodeError:
                    print(f"URL {link} 不包含有效的 JSON。")
                    jsonerror = "json解析失败！"
                    return jsonerror
            else:
                print(f"无法访问链接 {link}。状态码: {response.status_code}")
        except requests.ConnectionError:
            print(f"无法连接到链接 {link}。")
            return response.status_code

    def connect_mysql(self):
        """
        链接数据库方法，返回可操作的游标对象
        :return:可操作的游标对象cursor
        """

        connection = mysql.connector.connect(
            host="",
            port="",
            user="",
            password="",
            database="",
        )

        return connection
