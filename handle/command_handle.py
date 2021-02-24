# coding=utf-8
from handle.msg_handle import get_message_type,get_number,get_raw_message,get_user_id
from special_function.study import study_info
from special_function.logging_tool import logging_put
from special_function.help_msg import *
from special_function.web_api_use import translate_api,news_api,number_information_api,feeling_a_word_api,wallpaper_api,head_picture_api,sex_picture_api,baidu_record_api
from mysql.operate_subscribe import add_number,del_number,get_numbers,exist_number

#--------------------------------------------------------------------
#机器学习
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
        return '命令格式有误，发送“#帮助”获得更多信息'

#--------------------------------------------------------------------
#访问接口
def command_help_handle(type):
    #显示帮助信息
    if type=="private":
        return private_chat_help()
    else:
        return group_chat_help()

def command_translate_handle(message):
    if len(get_raw_message(message).split(' '))>=2:
        content=""
        for i in range(len(get_raw_message(message).split(' '))):
            if i==0:
                continue
            content+=" "+get_raw_message(message).split(' ')[i]
        return translate_api(content)
    else:
        return '命令格式有误，发送“#帮助”获得更多信息'

#手机号码信息
def command_number_information_handle(message):
    if len(get_raw_message(message).split(' '))==2:
        content=get_raw_message(message).split(' ')[1]
        return number_information_api(content)
    else:
        return '命令格式有误，发送“#帮助”获得更多信息'

def command_wallpaper_handle():
    #显示帮助信息
    return wallpaper_api()

def command_head_picture_handle(message):
    if len(get_raw_message(message).split(' '))==2:
        type=get_raw_message(message).split(' ')[1]
        return head_picture_api(type)
    else:
        return '命令格式有误，发送“#帮助”获得更多信息'

def command_sex_picture_handle():
    return sex_picture_api()



def command_baidu_record_handle(message):
    if len(get_raw_message(message).split(' '))==2:
        domain=get_raw_message(message).split(' ')[1]
        return baidu_record_api(domain)
    else:
        return '命令格式有误，格式：百度收录域名查询 [域名地址]'


def command_feeling_a_word_handle():
    return feeling_a_word_api()

def command_news_handle():
    return news_api()



#--------------------------------------------------------------------
#订阅
def command_sub_handle(subtitle,msg):
    if exist_number(subtitle,str(get_number(msg))):
        return "已经订阅了[CQ:face,id=21]"

    if add_number(subtitle,str(get_number(msg))):
        return "订阅成功~[CQ:face,id=21]"
#取消请阅
def command_no_sub_handle(subtitle,msg):
    #用户已经订阅
    if exist_number(subtitle,str(get_number(msg))):
        if del_number(subtitle,str(get_number(msg))):
            return("退订成功")
        else:
            return("退订失败，舍不得你，除非你关我机[CQ:face,id=23]")
    else:
        return "不在订阅状态中"



#--------------------------------------------------------------------
#广播

from subscribe.subscribe_manage import get_friends_array,get_groups_array
from mysql.operate_blacklist import get_blacklist
from socket_operate.client import send_msg
import time

#管理员账号（有权利进行广播）
admin_number=["马赛克"]
#广播
def command_broadcast_handle(msg):
    if str(get_number(msg)) in admin_number:
        if len(get_raw_message(msg).split(' ',1))==2:
            main_msg=get_raw_message(msg).split(' ',1)[1]
            #得到好友和群组列表
            friends=get_friends_array()
            groups=get_groups_array()
            #得到黑名单
            blacklist=get_blacklist()
            for num in friends:
                if not num in blacklist:
                    #发送广播内容
                    msg_dict={ 
                        "msg_type":"private", 
                        "number":num, 
                        "msg":"" 
                    }
                    #防止广播信息闭合
                    main_msg.replace('"','&quot;')        
                    main_msg.replace("'",'&apos;')                                        

                    msg_dict['msg']="[CQ:face,id=72]广播通知："+main_msg
                    send_msg(msg_dict)
            for num in groups:
                if not num in blacklist:
                    #发送广播内容
                    msg_dict={ 
                        "msg_type":"group", 
                        "number":num,  
                        "msg":"" 
                    }
                    #防止广播信息闭合
                    main_msg.replace('"','&quot;')        
                    main_msg.replace("'",'&apos;')                                     
                    
                    msg_dict['msg']="[CQ:face,id=72]广播通知："+main_msg
                    send_msg(msg_dict)                
            return '广播成功[CQ:face,id=63]'
        else:
            return '请指明想要广播的内容'
    else:
        return '你没有权利让我广播'
 




