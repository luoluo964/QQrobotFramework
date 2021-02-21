# coding=utf-8
from handle.msg_handle import get_message_type,get_number,get_raw_message,get_user_id
from special_function.study import study_info
from special_function.logging_tool import logging_put
from special_function.help_msg import *
from special_function.web_api_use import translate_api,number_information_api,wallpaper_api,head_picture_api

def command_study_handle(message):
    if len(get_raw_message(message).split(' '))==3:
        new_quest=get_raw_message(message).split(' ')[1]
        new_reply=get_raw_message(message).split(' ')[2]
        if study_info(new_quest,new_reply):
            logging_put("用户"+str(get_user_id(message))+"教我新内容："+new_quest+"--"+new_reply)
            return '学习成功，收获新知识[CQ:face,id=63]'
        else:
            return '学习失败'
    else:
        return '命令格式有误，发送“帮助”获得更多信息'

def command_help_handle():
    #显示帮助信息
    return private_chat_help()

def command_translate_handle(message):
    if len(get_raw_message(message).split(' '))>=2:
        content=""
        for i in range(len(get_raw_message(message).split(' '))):
            if i==0:
                continue
            content+=" "+get_raw_message(message).split(' ')[i]
        return translate_api(content)
    else:
        return '命令格式有误，发送“帮助”获得更多信息'

#手机号码信息
def command_number_information_handle(message):
    if len(get_raw_message(message).split(' '))==2:
        content=get_raw_message(message).split(' ')[1]
        return number_information_api(content)
    else:
        return '命令格式有误，发送“帮助”获得更多信息'

def command_wallpaper_handle():
    #显示帮助信息
    return wallpaper_api()

def command_head_picture_handle(message):
    if len(get_raw_message(message).split(' '))==2:
        type=get_raw_message(message).split(' ')[1]
        return head_picture_api(type)
    else:
        return '命令格式有误，发送“帮助”获得更多信息'