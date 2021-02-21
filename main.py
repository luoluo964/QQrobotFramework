# coding=utf-8
import  socket_operate.server
import  handle.main_handle
from special_function.logging_tool import logging_put
import socket

def main():
    while 1:
        #使用try、except语句保证程序不会因部分错误退出。
        all_message = socket_operate.server.rev_msg()
        try:
            handle.main_handle.main_handle(all_message)
        except BaseException as e:
            logging_put(e)
            print(e)
            continue
    
if (__name__ == "__main__"):
    main()  