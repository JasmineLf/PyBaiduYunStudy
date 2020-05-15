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

def server_tcp():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    server_socket.bind((host,port))
    server_socket.listen(5)
    while True:
        client_socket,addr = server_socket.accept()
        print("连接成功：%s"%str(addr))
        mag = "2020年5月15日" + "\r\n"
        client_socket.send(mag.encode('utf-8'))
        client_socket.close()

if __name__ == '__main__':
    server_tcp()
