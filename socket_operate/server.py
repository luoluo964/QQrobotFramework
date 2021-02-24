# coding=utf-8
#在5701端口的角度上，我们是接收消息的服务端

import socket
import json

from special_function.logging_tool import logging_put
 

##定义socket类型，网络通信，TCP
ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#套接字绑定的IP与端口
ListenSocket.bind(('10.0.0.3', 5701))
#开始TCP监听
ListenSocket.listen(100)

# 构造响应数据
response_start_line = "HTTP/1.1 200 OK\r\n"
response_headers = "Server: received\r\n"
response_body = "<h1>Python HTTP Test</h1>"
response = response_start_line + response_headers + "\r\n" + response_body
 
#转json定位有效信息
def json_to_info(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="}":
            #解码 JSON 数据。返回 Python 字段的数据类型
            return json.loads(msg[i:])
    return None
 
#需要循环执行，返回值为json格式
def rev_msg():
    #接受TCP连接，并返回新的套接字与IP地址
    conn, addr = ListenSocket.accept() 
    logging_put(addr)

    #接收数据解码（接收到的是string形式的json）
    data = conn.recv(10240).decode(encoding='utf-8')

    #json格式转dict格式
    rev_dict=json_to_info(data)
    conn.sendall(response.encode())

    conn.close()
    return rev_dict
