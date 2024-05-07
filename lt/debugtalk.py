import logging
import time
from typing import List
import os
import sys
rsa_fapath = os.path.dirname(os.path.dirname("rsa_utils/utils.py"))
sys.path.append(rsa_fapath)
from rsa_utils.utils import rsa_decrypt,rsa_encrypt

def d_rsa_decrypt(text):
    result = rsa_decrypt(text)
    return result

def d_rsa_encrypt(text):
    result = rsa_encrypt(text)
    return result

def sleep(n_secs):
    time.sleep(n_secs)

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
    reslut = d_rsa_encrypt("123456")
    print(reslut)
