# coding=utf-8
#对于 通知事件 的处理
from handle.msg_handle import get_notice_type
from socket_operate.client  import  send_msg
import random

def friend_recall_handle(message):
    if random.randint(1,2)==1:
        msg_dict={ 
            "msg_type":"private", 
            "number":str(message['user_id']), 
            "msg":"和个机器人聊天还撤回？" 
        }    
        send_msg(msg_dict)
    return 

def group_recall_handle(message):
    if random.randint(1,2)==1:
        msg_dict={ 
            "msg_type":"group", 
            "number":str(message['group_id']), 
            "msg":"这个人说要请大家吃饭" 
        }
        send_msg(msg_dict) 
    return 

def group_admin_handle(message):
    if random.randint(1,3)==1:
        msg_dict={ 
            "msg_type":"group", 
            "number":str(message['group_id']), 
            "msg":"新官上任~" 
        }
        send_msg(msg_dict) 
    return 

def group_increase_handle(message):
    msg_dict={ 
        "msg_type":"group", 
        "number":str(message['group_id']), 
        "msg":"" 
    }
    temp=random.randint(1,3)
    if temp==1:
        send_msg("老规矩，先爆照")
    elif temp==2:
        send_msg("小姐姐你好呀[CQ:face,id=108]")
    return

def notice_handle(message):
    if get_notice_type(message)=='friend_recall':
        friend_recall_handle(message)
    elif get_notice_type(message)=='group_recall':
        group_recall_handle(message)
    elif get_notice_type(message)=='group_admin':
        group_admin_handle(message)
    elif get_notice_type(message)=='group_increase':
        group_increase_handle(message)
    return 0