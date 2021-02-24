# coding=utf-8
#对于 消息事件 的处理import
from socket_operate.client  import send_msg
from handle.command_handle import command_study_handle,command_broadcast_handle,command_no_sub_handle,command_sub_handle,command_feeling_a_word_handle,command_news_handle,command_help_handle,command_baidu_record_handle,command_translate_handle,command_head_picture_handle,command_number_information_handle,command_wallpaper_handle,command_sex_picture_handle
from handle.msg_handle import get_raw_message,set_raw_message,get_number,get_user_id,get_message_type
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
    elif command=="#广播":
        reply=command_broadcast_handle(message)
    elif command=="#帮助":
        reply=command_help_handle(get_message_type(message))
    elif command=="翻译":   
        reply=command_translate_handle(message)
    elif command=="号码信息":   
        reply=command_number_information_handle(message)
    elif command=="壁纸" or command=="高清壁纸":
        reply=command_wallpaper_handle()
    elif command=="头像":   
        reply=command_head_picture_handle(message)
    elif command=="来点色图":   
        reply=command_sex_picture_handle()
    elif command=="百度收录域名查询":   
        reply=command_baidu_record_handle(message)
    elif command=="夜深了":   
        reply=command_feeling_a_word_handle()
    elif command=="新闻":
        reply=command_news_handle()
    elif command=="#订阅":
        if len(get_raw_message(message).split(' '))==2:
            content=get_raw_message(message).split(' ')[1]
            if content=="每日英语":
                reply=command_sub_handle("famousremark",message)
            elif content=="每日必应壁纸":
                reply=command_sub_handle("subwallpaper",message)
            elif content=="网易云每日推荐":
                reply=command_sub_handle("submusic",message)
            elif content=="每日微博热搜":
                reply=command_sub_handle("subweibohot",message)
            elif content=="每日色图":
                reply=command_sub_handle("subsexpic",message)
            elif content=="每日生活小窍门":
                reply=command_sub_handle("sublifeskill",message)
            elif content=="考研倒计时":
                reply=command_sub_handle("subkaoyan",message)
            else:
                reply="频道不存在"
        else:
            reply="请指定频道"
    elif command=="#取消订阅":
        if len(get_raw_message(message).split(' '))==2:
            content=get_raw_message(message).split(' ')[1]
            if content=="每日英语":
                reply=command_no_sub_handle("famousremark",message)
            elif content=="每日必应壁纸":
                reply=command_no_sub_handle("subwallpaper",message)
            elif content=="网易云每日推荐":
                reply=command_no_sub_handle("submusic",message)
            elif content=="每日微博热搜":
                reply=command_no_sub_handle("subweibohot",message)
            elif content=="每日色图":
                reply=command_no_sub_handle("subsexpic",message)
            elif content=="每日生活小窍门":
                reply=command_no_sub_handle("sublifeskill",message)
            elif content=="考研倒计时":
                reply=command_no_sub_handle("subkaoyan",message)
            else:
                reply="频道不存在"
        else:
            reply="请指定频道"        
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

    if general_detect!='':
        msg_dict["msg"]=general_detect
    elif db_detect!='':
        msg_dict["msg"]=db_detect
    else:
        logging_put("私聊中用户请求没有对应的信息："+str(get_user_id(message))+"-"+get_raw_message(message))
        msg_dict["msg"]=private_msg_error()


    send_msg(msg_dict)
    return 

#---------------------------------------------------------------
#是否at了机器人
def at_robot(message):
    
    if get_raw_message(message).split(' ')[0]=="[CQ:at,qq=1750133059]":
        return True
    return False


#群聊信息的普通检测
def group_msg_general_detection(message):

    reply=''
    #处理有at的指令
    if at_robot(message):
        #回复消息的前缀（at信息）
        prefix="[CQ:at,qq="+str(get_user_id(message))+"]"

        #方便还原message
        ori=get_raw_message(message)
        #更新原数据的原始信息
        set_raw_message(message,get_raw_message(message).split(' ',1)[1])
        
        #得到特殊指令
        command=get_raw_message(message).split(' ')[0]
        if command=="#帮助":
            reply=prefix+command_help_handle(get_message_type(message))
        elif command=="翻译":   
            reply=prefix+command_translate_handle(message)
        elif command=="号码信息":   
            reply=prefix+command_number_information_handle(message)
        elif command=="壁纸" or command=="高清壁纸":
            reply=prefix+command_wallpaper_handle()
        elif command=="头像":   
            reply=prefix+command_head_picture_handle(message)
        elif command=="来点色图":   
            reply=prefix+command_sex_picture_handle()
        elif command=="百度收录域名查询":   
            reply=prefix+command_baidu_record_handle(message)
        elif command=="夜深了":   
            reply=prefix+command_feeling_a_word_handle()
        elif command=="新闻":
            reply=prefix+command_news_handle()
        elif command=="#订阅":
            if len(get_raw_message(message).split(' '))==2:
                content=get_raw_message(message).split(' ')[1]
                if content=="每日英语":
                    reply=command_sub_handle("famousremark",message)
                elif content=="每日必应壁纸":
                    reply=command_sub_handle("subwallpaper",message)
                elif content=="网易云每日推荐":
                    reply=command_sub_handle("submusic",message)
                elif content=="每日微博热搜":
                    reply=command_sub_handle("subweibohot",message)
                elif content=="每日色图":
                    reply=command_sub_handle("subsexpic",message)
                elif content=="每日生活小窍门":
                    reply=command_sub_handle("sublifeskill",message)
                elif content=="考研倒计时":
                    reply=command_sub_handle("subkaoyan",message)
                else:
                    reply="频道不存在"
            else:
                reply="请指定频道"
        elif command=="#取消订阅":
            if len(get_raw_message(message).split(' '))==2:
                if content=="每日英语":
                    reply=command_no_sub_handle("famousremark",message)
                elif content=="每日必应壁纸":
                    reply=command_no_sub_handle("subwallpaper",message)
                elif content=="网易云每日推荐":
                    reply=command_no_sub_handle("submusic",message)
                elif content=="每日微博热搜":
                    reply=command_no_sub_handle("subweibohot",message)
                elif content=="每日色图":
                    reply=command_no_sub_handle("subsexpic",message)
                elif content=="每日生活小窍门":
                    reply=command_no_sub_handle("sublifeskill",message)
                elif content=="考研倒计时":
                    reply=command_no_sub_handle("subkaoyan",message)
                else:
                    reply="频道不存在"
            else:
                reply="请指定频道"  
        #还原消息        
        set_raw_message(message,ori)           
    else:
        #没有@机器人，则有五分之一的检测关键字
        command=get_raw_message(message).split(' ')[0]
        #回复消息的前缀（at信息）
        prefix="[CQ:at,qq="+str(get_user_id(message))+"]"
        if command=="#帮助":
            reply=command_help_handle(get_message_type(message))
        elif command=="夜深了":
            reply=command_feeling_a_word_handle()
        elif command=="色图" or command=="来点色图": 
            reply=prefix+"满足你，"+command_sex_picture_handle()
    return reply


#群聊信息的数据库检测（通过数据库来找对应的回复）
def group_msg_db_detection(message):
    reply=''
    prefix="[CQ:at,qq="+str(get_user_id(message))+"]"
    if at_robot(message):
        #方便还原message
        ori=get_raw_message(message)
        #更新原数据的原始信息
        set_raw_message(message,get_raw_message(message).split(' ',1)[1])
        reply=get_reply(get_raw_message(message))
        if reply!='':
            reply=prefix+reply
        #还原消息        
        set_raw_message(message,ori)   
    else: 
        reply=get_reply(get_raw_message(message))
    return reply


#群聊信息的错误处理
def group_msg_error(message):
    if at_robot(message):
        rand = random.randint(1,5)
        prefix="[CQ:at,qq="+str(get_user_id(message))+"]"
        msg="超出我的知识上限"
        if rand == 1:
            msg = prefix+"啥意思咧？"
        elif rand == 5:
            msg = prefix+"群里有人知道怎么回答ta吗？"
        elif rand == 2:
            msg = prefix+"听不懂，不会答[CQ:face,id=22]"
        elif rand == 3:
            msg = prefix+"？？？"
        elif rand == 4:
            msg = prefix+"听不懂~"
    else:
        rand = random.randint(1,2)
        prefix="[CQ:at,qq="+str(get_user_id(message))+"]"
        msg="超出我的知识上限"
        if rand == 1:
            msg = "消息太复杂"
        elif rand == 2:
            msg = prefix+"回你一下，省得你尴尬~"           

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

    if general_detect!='':
        msg_dict["msg"]=general_detect
    elif db_detect!='':
        msg_dict["msg"]=db_detect
    else:
        logging_put("群聊中用户请求没有对应的信息："+str(get_user_id(message))+"-"+get_raw_message(message))
        msg_dict["msg"]=group_msg_error(message)
    #没有at，则有四分之一的概率回复消息；at了则一定回复
    if at_robot(message):
        send_msg(msg_dict)
    else:
        if 1==random.randint(1,12):
            send_msg(msg_dict)
    return 

#---------------------------------------------------------------

def message_handle(message):
    logging_put("收到消息"+get_raw_message(message)+"来自"+str(get_number(message)))
    if get_message_type(message)=='private':
        private_msg_handle(message)
    elif get_message_type(message)=='group':
        group_msg_handle(message)
    return 0
