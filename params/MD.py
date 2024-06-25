import random
import time
import string
import base64
import hashlib


def MdXor(strings, key):
    """
    异或算法处理字符串
    :param strings:要做异或的字符串
    :param key:加密密钥
    :return:经过异或算法处理的待加密字符串
    """

    if strings == '' or key == '':
        return ''
    else:
        # 字符串转字节数组
        string_byte = bytearray(strings, 'utf-8')
        string_len = len(string_byte)

        # 字符串转字节数组
        key_byte = bytearray(key, 'utf-8')
        key_len = len(key_byte)

        #对两组字节数组异或处理并添加进列表
        rt = []
        for i in range(0, string_len):
            j = i % key_len
            rt.append(string_byte[i] ^ key_byte[j])

        #将异或处理过后的字节数组转成字符串
        MdXor_rt = bytearray(rt).decode()

        return MdXor_rt


def MdEncode(strings, key):
    """
    加密算法
    :param strings:待加密内容
    :param key:密钥
    :return:加密后的内容
    """
    #获取13位毫秒级时间戳及13位随机字符串
    time_str = int(time.time_ns() / 1e6) + 120 * 1000
    RandStr = string.ascii_letters + string.digits
    rand_str13 = ''.join(random.choices(RandStr, k=13))

    #对要加密内容转化13位字节数组，然后进行b64编码，再转化位字符串
    string_byte = bytearray(strings, 'utf-8')
    base64_encoded = base64.b64encode(string_byte).decode('utf-8')

    #计算字节数组的 MD5 哈希值，（时间戳+随机字符串+key)获取随机密钥
    md5_hash = hashlib.md5()
    s = str(time_str) + rand_str13 + key
    s_byte = bytearray(s, 'utf-8')
    md5_hash.update(s_byte)
    rand_key_md5 = md5_hash.hexdigest()

    #对加密内容进行异或处理，将结果转化为字节数组，然后进行b64编码，再转化位字符串
    str_xor = MdXor(base64_encoded, rand_key_md5) + MdXor(str(time_str), rand_str13) + MdXor(rand_str13, key)
    jiami = bytearray(str_xor, 'utf-8')
    base64_jiami = base64.b64encode(jiami).decode('utf-8')

    return base64_jiami

def MdDecode(strings, key):
    """
    解密算法
    :param strings:待解密内容
    :param key:密钥
    :return:解密后的内容
    """
    #将传入的字符串的空格替换为加号
    strings = strings
    stringss = strings.replace(" ", "+")

    #对加密的内容先进行b64解码，得到字节数组，然后转化位字符串，并获取字符串长度
    dec64_str = base64.b64decode(stringss).decode('utf-8')
    len_dec64_str = len(dec64_str)

    #将加密后的13位随机字符分离出来
    rand_str = MdXor(dec64_str[len_dec64_str - 13:], key)

    #将加密后的时间戳分离出来
    time_str = MdXor(dec64_str[len_dec64_str - 26:len_dec64_str - 13], rand_str)

    #先用分离的13位字符+加密后的时间戳+key生成随机key,再用异或算法得到b64编码后的解密内容
    md5_hash = hashlib.md5()
    s = time_str + rand_str + key
    s_byte = bytearray(s, 'utf-8')
    md5_hash.update(s_byte)
    rand_key_md5 = md5_hash.hexdigest()

    rand_key_str = MdXor(dec64_str[0:len_dec64_str - 26], rand_key_md5)
    fanally_str = base64.b64decode(rand_key_str).decode('utf-8')

    return fanally_str


# print(MdEncode('37151829', "a8b1c1J9Q2K2"))
# print(MdEncode('bSYPcSlmXAB5SAMAfXgHQQl/V0F/eF8BWy13VURSeS9AH30kAA0=', "a8b1c1J9Q2K2"))
# print(MdDecode('L0xQHnY1dQYrWw0NAXN/Tm4HYFdZS1JlAFF8LUs1ARtdOUAgZlI=', 'a8b1c1J9Q2K2'))