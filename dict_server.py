"""
dict 服务端
"""
import sys
import time
import signal
from socket import *
from dict_db import Database
from multiprocessing import Process

# 全局变量
HOST = "0.0.0.0"
PORT = 7777
ADDR = (HOST, PORT)
DATABASE = "dict"

# 创建数据库连接
db = Database(DATABASE)


# 处理注册请求
def do_register(connfd, name, passwd):
    if db.register(name, passwd):
        connfd.send(b"OK")
    else:
        connfd.send(b"FAIL")


# 处理登录请求
def do_login(connfd, name, passwd):
    if db.login(name, passwd):
        connfd.send(b"OK")
    else:
        connfd.send(b"FAIL")


# 处理查询单词请求
def check_word(connfd, name, word):
    db.insert_history(name, word)
    mean = db.find(name, word)
    if mean:
        connfd.send(mean[0].encode())
    else:
        connfd.send("没有该单词".encode())


def history():
    mean = db.find(name, word)
    if mean:
        connfd.send(mean[0].encode())
    else:
        connfd.send("没有该单词".encode())


def handle(connfd, addr):
    while True:
        request = connfd.recv(1024).decode()
        tmp = request.split()
        if not request or tmp[0] == "E":
            print(addr, "退出了")
            return
        elif tmp[0] == "R":
            # R name passwd
            do_register(connfd, tmp[1], tmp[2])
        elif tmp[0] == "L":
            do_login(connfd, tmp[1], tmp[2])
        elif tmp[0] == "C":
            check_word(connfd, tmp[1], tmp[2])


def main():
    # 创建TCP监听套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待处理客户端连接
    while True:
        print("等待连接...")
        try:
            connfd, addr = sockfd.accept()
            print(addr, "连接了")
        except KeyboardInterrupt:
            sockfd.close()
            db.close()
            sys.exit("退出服务端")
        except Exception as e:
            print(e)
            continue

        # 为客户端创建进程
        p = Process(target=handle, args=(connfd, addr,))
        p.start()


if __name__ == '__main__':
    main()
