import sys
from socket import *
from multiprocessing import Process
import time
import signal

# 全局变量
HOST = "0.0.0.0"
PORT = 7777
ADDR = (HOST, PORT)


def handle(connfd):
    while True:
        request = connfd.recv(1024).decode()
        print(request)
        if request == 1:
            pass


def main():
    # 创建TCP监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待处理客户端连接
    while True:
        print("等待连接...")
        try:
            connfd, addr = s.accept()
            print(addr, "连接了")
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务端")
        except Exception as e:
            print(e)
            continue

        # 为客户端创建进程
        p = Process(target=handle, args=(connfd,))
        p.start()


if __name__ == '__main__':
    main()
