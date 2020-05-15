'''
时间：2020年5月15日 14:30:45
作者：LF
邮箱：jksj27250@gmail.com
主题：
    1.TCP Socket通信
内容：
    1.Socket 客户端
'''

import socket
import sys

def client_udp():
    BUFSIZE = 1024
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        msg = input(">>").strip()
        ip_port = ("127.0.0.1",9999)
        client_socket.sendto(msg.encode("utf-8"),ip_port)

        data, server_addr = client_socket.recvfrom(BUFSIZE)
        print("客户端 Reform：",data,server_addr)

    client_socket.close()

if __name__ == "__main__":
    client_udp()


