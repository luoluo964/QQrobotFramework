# coding=utf-8
#该文件主要是对主文件中得到的接收消息进行处理的方法

import handle.msg_handle
    
import handle.message_handle
import handle.notice_handle
import handle.request_handle
import handle.black_list_handle as power
import subscribe.subscribe_manage as ss 

#事件类型出现异常
def default():
    print("心跳包")
    return 0



#将不同的事件分发给不同的情况
def main_handle(msg):
    #检查开关机指令（返回必须是pass才能通过）
    if not power.check_pass(msg):
        print("黑名单中的消息不予理睬~")
        return 0

    #消息订阅处理
    ss.check_subscribe()

    post_type = handle.msg_handle.get_post_type(msg)         # 获取上报类型
    if post_type=='message':  #消息事件
        handle.message_handle.message_handle(msg)
    elif post_type=='notice':   #通知事件
        handle.notice_handle.notice_handle(msg)
    elif post_type=='request':   #请求事件
        handle.request_handle.request_handle(msg)
    else:
        default()
    return 0
