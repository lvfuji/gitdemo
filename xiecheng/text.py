import gevent
from gevent import monkey
monkey.patch_all()
from socket import *
import time

def main():
    s = socket()
    s.bind(('176.234.87.39',8888))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('waiting for connecting..')
        gevent.spawn(handler, conn)

def handler(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.send(time.ctime().encode())
    conn.close()
    print("hello world")
    print("agagagagag")

if __name__ == '__main__':
    main()
