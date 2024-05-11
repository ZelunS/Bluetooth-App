import logging
import time
from typing import List
import os
import sys
rsa_fapath = os.path.dirname(os.path.dirname("rsa_utils/utils.py"))
sys.path.append(rsa_fapath)
from rsa_utils.utils import rsa_decrypt,rsa_encrypt
gmail_fapth = os.path.dirname(os.path.dirname("getMail.py"))
sys.path.append(gmail_fapth)
from getMail import getMail
import re
import random
import string


def d_rsa_decrypt(text):
    """使用私钥进行解密"""
    result = rsa_decrypt(text)
    return result

def d_rsa_encrypt(text):
    """使用公钥进行加密"""
    result = rsa_encrypt(text)
    return result

def getCode():
    """获取验证码"""
    pattern = r'\b\d{6}\b'
    mail = getMail()
    verification_code = re.search(pattern, mail)
    if verification_code:
        return verification_code.group()
    else:
        return None

def sleep(n_secs):
    """睡眠等待"""
    time.sleep(n_secs)

def randomChoice(num):
    """随机选择"""
    randomNum = random.randint(0,num-1)
    return randomNum

def randomLge():
    """随机选择语言"""
    language_list = ["zh","en","ja","de"]
    return random.choice(language_list)

def generate_random_string(num):
    """生成随机字符"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(num))


def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def sum_ints(*args: List[int]) -> int:
    result = 0
    for arg in args:
        result += arg
    return result


def sum_two_int(a: int, b: int) -> int:
    return a + b


def sum_two_string(a: str, b: str) -> str:
    return a + b


def sum_strings(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += arg
    return result


def concatenate(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += str(arg)
    return result


def setup_hook_example(name):
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"


def teardown_hook_example(name):
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"


if __name__ == '__main__':
    # a = randomChoice(83)
    # print(a)
    a = generate_random_string(500)
    print(a)