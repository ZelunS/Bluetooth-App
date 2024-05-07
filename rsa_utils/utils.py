from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from pathlib import Path


def create_rsa_key():
    """
    创建RSA密钥
    步骤说明：
    1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码
    2、生成 1024/2048 位的 RSA 密钥
    3、调用 RSA 密钥实例的 exportKey 方法，传入口令、使用的 PKCS 标准以及加密方案这三个参数。
    4、将私钥写入磁盘的文件。
    5、使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件。
    """
    # 利用伪随机数来生成私钥和公钥
    random_generator = Random.new().read

    key = RSA.generate(2048, random_generator)  # 生成 1024/2048 位的 RSA 密钥
    encrypted_key = key.exportKey()  # 密钥实例
    with open("rsa_private_key.pem", "wb") as f:  # 私钥写入磁盘
        f.write(encrypted_key)
    with open("rsa_public_key.pem", "wb") as f:  # 公钥写入磁盘
        f.write(key.publickey().exportKey())


def rsa_decrypt(text):
    """使用私钥进行解密"""
    private_key = open(Path(__file__).parent / "rsa_private_key.pem").read()
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(private_key))
    retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
    return retval


def rsa_encrypt(text):
    """使用公钥进行加密"""
    rsakey = RSA.importKey(open(Path(__file__).parent / "rsa_public_key.pem").read())
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    return base64.b64encode(cipher.encrypt(text.encode('utf-8'))).decode()


if __name__ == '__main__':
    result = rsa_encrypt("123456")
    print(result)
    # result = "bNK23yToydmB/N1UohrEDnxt2YtozaSYie17HkS1UwXK9nYMlm44hqugWk+a2LHsakDa1O2iti85ZDo5qgKfAbjWJVk+PSmJqGH6gMKhu1x5bMxqO3PJaeS4OEq8cQzahhKq+AI1w/8ZgBNID0ft48MMF15BCCxzxRbr9SxoMUQSwSq4XUF/cAoCov5f4ga7BUX9qoaoACmURXKclkzpChTZfbvKTk4gsiTeK1q1JbybGv7Hi/IsiY6jyrXmHvUgdVPQF/su6tkwB0iVgvZBKrei6aqXAJQrO6hDmvqBDwHSMCI7ivZN/ALoZ1rE+t2sRkeG3funu+i518KnEvSfqQ=="
    # print(rsa_decrypt(result))
