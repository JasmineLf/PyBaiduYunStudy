'''
时间：2020年5月15日 14:30:45
作者：LF
邮箱：jksj27250@gmail.com
主题：
    1.TCP Socket通信
内容：
    1.Socket 客户端
'''

import  socket
import  sys

def client_tcp():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    post = 9999
    client_socket.connect((host,post))
    msg = client_socket.recv(1024)
    client_socket.close()
    print(msg.decode('utf-8'))

if __name__ == "__main__":
    client_tcp()