"""
name:peter
chatroom client
"""

from socket import *
import sys
import os
import signal


# 子进程发送消息
def do_child(s, name, addr):
    while True:
        text = input("发言(输入quit退出)：")
        # 用户退出
        if text == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(), addr)
            # 从子进程中结束父进程
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit("退出聊天室")
        # 正常聊天
        else:
            msg = 'C %s %s' % (name, text)
            s.sendto(msg.encode(), addr)


# 父进程接受消息
def do_parent(s):
    while True:
        msg, addr = s.recvfrom(1024)
        print(msg.decode() + "\n发言(输入quit退出):",
              end='')


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    s = socket(AF_INET, SOCK_DGRAM)

    while True:
        name = input("请输入用户名：")
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("＠进入聊天室＠")
            break
        else:
            print(data.decode())

    pid1 = os.fork()
    if pid1 < 0:
        print("Create first process failed")
    elif pid1 == 0:
        # 发消息
        do_child(s, name, ADDR)
    else:
        do_parent(s)


if __name__ == "__main__":
    main()
