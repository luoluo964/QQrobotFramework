# coding=utf-8
#对于 消息事件 的处理
from socket_operate.client  import send_msg
from handle.command_handle import command_study_handle,command_help_handle,command_translate_handle,command_head_picture_handle,command_number_information_handle,command_wallpaper_handle
from handle.msg_handle import get_raw_message,get_number,get_user_id,get_message_type
from special_function.logging_tool import logging_put
from special_function.study import get_reply,random

#---------------------------------------------------------------
#私聊信息的普通检测
def private_msg_general_detection(message):
    reply=''
    #得到特殊指令
    command=get_raw_message(message).split(' ')[0]
    if command=="#学习":
        reply=command_study_handle(message)
    elif command=="帮助":
        reply=command_help_handle()
    elif command=="翻译":   
        reply=command_translate_handle(message)
    elif command=="号码信息":   
        reply=command_number_information_handle(message)
    elif command=="壁纸" or command=="高清壁纸":
        reply=command_wallpaper_handle()
    elif command=="头像":   
        reply=command_head_picture_handle(message)

    # elif command==""
    return reply

#私聊信息的数据库检测（通过数据库来找对应的回复）
def private_msg_db_detection(message):
    reply=''
    reply=get_reply(get_raw_message(message))
    return reply

#私聊信息的错误处理
def private_msg_error():
    rand = random.randint(1,4)
    msg="超出我的知识上限"
    if rand == 1:
        msg = "消息太复杂"
    elif rand == 2:
        msg = "学识浅薄，我不会答[CQ:face,id=96]"
    elif rand == 3:
        msg = "啊？"
    elif rand == 4:
        msg = "听不懂~"
    return msg

#私聊消息处理
def private_msg_handle(message):
    msg_dict={ 
        "msg_type":"private", 
        "number":get_number(message), 
        "msg":"我听不懂" 
    }
    #检测
    general_detect=private_msg_general_detection(message)
    db_detect=private_msg_db_detection(message)

    no_reply=False
    if general_detect!='':
        print("特殊命令找到内容")
        msg_dict["msg"]=general_detect
    elif db_detect!='':
        print("数据库找到内容")
        msg_dict["msg"]=db_detect
    else:
        print("不会回复")
        no_reply=True
        logging_put("私聊中用户请求没有对应的信息："+str(get_user_id(message))+"-"+get_raw_message(message))
        msg_dict["msg"]=private_msg_error()

    print("待发送消息体")
    print(msg_dict)

    #若没有对应消息，则有四分之一的概率不会回复
    if no_reply:
        if random.randint(1,4)!=1:
            send_msg(msg_dict)
    else:  
        send_msg(msg_dict)
    return 

#---------------------------------------------------------------
#群聊信息的普通检测
def group_msg_general_detection(message):
    reply=''
    return reply

#群聊信息的数据库检测（通过数据库来找对应的回复）
def group_msg_db_detection(message):
    reply=''
    reply=get_reply(get_raw_message(message))
    return reply

#群聊信息的错误处理
def group_msg_error():
    rand = random.randint(1,5)
    msg="超出我的知识上限"
    if rand == 1:
        msg = "消息太复杂"
    elif rand == 5:
        msg = "群里有人知道怎么回答ta吗？"
    elif rand == 2:
        msg = "江湖险恶，我不会答"
    elif rand == 3:
        msg = "啊？"
    elif rand == 4:
        msg = "听不懂~"
    return msg

#群聊消息处理
def group_msg_handle(message):
    msg_dict={ 
        "msg_type":"group", 
        "number":get_number(message), 
        "msg":"我听不懂" 
    }
    #检测
    general_detect=group_msg_general_detection(message)
    db_detect=group_msg_db_detection(message)
    no_reply=False
    if general_detect!='':
        msg_dict["msg"]=general_detect
    elif db_detect!='':
        msg_dict["msg"]=db_detect
    else:
        no_reply=True
        logging_put("群聊中用户请求没有对应的信息："+get_user_id(message)+"-"+get_raw_message(message))
        msg_dict["msg"]=group_msg_error()
    #若没有对应消息，则有四分之一的概率不会回复
    if no_reply:
        if random.randint(1,4)!=1:
            send_msg(msg_dict)
    else:  
        send_msg(msg_dict)
    return 

#---------------------------------------------------------------

def message_handle(message):
    if get_message_type(message)=='private':
        private_msg_handle(message)
    elif get_message_type(message)=='group':
        group_msg_handle(message)
    return 0
