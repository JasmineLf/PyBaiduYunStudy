'''
时间：2020年5月15日 14:30:45
作者：LF
邮箱：jksj27250@gmail.com
主题：
    1.TCP Socket通信
内容：
    1.Socket 服务器端
'''

import socket
import sys

def server_udp():
    BUFSIZE = 1024
    ip_port = ("127.0.0.1",9999)
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind(ip_port)
    while True:
        data,client_addr = server_socket.recvfrom(BUFSIZE)
        print("Server收到的数据",data)

        server_socket.sendto(data.upper(),client_addr)

    server_socket.close()

if __name__ == '__main__':
    server_udp()
