from socket import *
from getpass import getpass
import hashlib
import sys
import time

# 服务器地址
HOST = "127.0.0.1"
PORT = 7777
ADDR = (HOST, PORT)
sockfd = socket()
sockfd.connect(ADDR)


# 注册功能
def do_register():
    while True:
        name = input("UserName:")
        passwd = getpass("Password:")
        passwd1 = getpass("Again:")
        if passwd != passwd1:
            print("两次密码输入不一致")
            continue
        if (" " in name) or (" " in passwd):
            print("用户名密码不能有空格")
            continue
        passwd = hashlib.md5(passwd.encode()).hexdigest()
        msg = "R %s %s" % (name, passwd)
        sockfd.send(msg.encode())  # 发送请求
        data = sockfd.recv(1024).decode()  # 接收反馈
        if data == "OK":
            print("注册成功")
        else:
            print("注册失败")
        return


# 登录功能
def do_login():
    name = input("UserName:").strip(" ")
    passwd = getpass("Password:").strip(" ")
    passwd = hashlib.md5(passwd.encode()).hexdigest()
    msg = "L %s %s" % (name, passwd)
    sockfd.send(msg.encode())  # 发送请求
    data = sockfd.recv(1024).decode()  # 接收反馈
    if data == "OK":
        print("登录成功")
        two_main(name)
    else:
        print("登录失败")


# 查单词
def check_word(name):
    while True:
        word = input("word(##退出):")
        if word == "##":
            break
        msg = "C %s %s" % (name, word)
        sockfd.send(msg.encode())  # 发送请求
        data = sockfd.recv(10240).decode()  # 接收反馈
        print(word, ":", data)


# 历史记录
def history(name):
    msg = "H %s" % name
    sockfd.send(msg.encode())  # 发送请求
    data = sockfd.recv(1024).decode()  # 是否有历史记录
    if data == "OK":
        while True:
            data = sockfd.recv(1024).decode()
            if data == "##":
                break
            print(data)
            # data = data.split(" ",1)
    else:
        print("没有历史记录")


# 二级界面
def two_main(name):
    while True:
        print("\t---------Welcome---------")
        print("\t 1.查单词 2.历史记录 0.注销 ")
        print("\t-------------------------")
        num = input("请选择:")
        if num == "1":
            check_word(name)
        elif num == "2":
            history(name)
        elif num == "0":
            main()
        else:
            print("请输入正确命令")


# 主界面
def main():
    while True:
        print("\t-------Welcome------")
        print("\t 1.登录 2.注册 0.退出 ")
        print("\t--------------------")
        num = input("请选择:")
        if num == "1":
            do_login()
        elif num == "2":
            do_register()
        elif num == "0":
            sockfd.send(b"E")
            sys.exit("谢谢使用")
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
