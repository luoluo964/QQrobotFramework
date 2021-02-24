# coding=utf-8
#订阅

import schedule
import json
import requests

from mysql.operate_subscribe import add_number,del_number,get_numbers
from mysql.operate_blacklist import get_blacklist
import subscribe.subscribe_content as ss_content

from special_function.logging_tool import logging_put

from socket_operate.client  import send_msg

#得到一些信息的请求地址
ip="马赛克"
#检查得到好友数组（方便我们排查一个账号是好友还是群组）
def get_friends_array():
    #确保连接及时断开
    headers = {'Connection': 'close'}
    friends_result=requests.get(url='http://'+ip+':5700/get_friend_list',headers=headers)
    friends_dict=json.loads(friends_result.text)
    friends_array=[]
    for item in friends_dict['data']:
        friends_array.append(str(item['user_id']))

    return friends_array

#检查得到群组数组（方便我们排查一个账号是好友还是群组）
def get_groups_array():
    #确保连接及时断开
    headers = {'Connection': 'close'}
    groups_result=requests.get(url='http://'+ip+':5700/get_group_list',headers=headers)

    groups_dict=json.loads(groups_result.text)
    groups_array=[]
    for item in groups_dict['data']:
        groups_array.append(str(item['group_id'])) 

    return groups_array

def send_subscribe(msg_type,num,subscribe):
    logging_put("给账号"+str(num)+"发送"+subscribe+"的订阅")

    msg_dict={ 
        "msg_type":msg_type, 
        "number":num, 
        "msg":""
    }
    #订阅内容分发
    if subscribe=='famousremark':
        msg_dict["msg"]=ss_content.famousremark_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【每日英语】订阅频道出现问题[CQ:face,id=37]"
    elif subscribe=="subwallpaper":
        msg_dict["msg"]=ss_content.wallpaper_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【每日必应壁纸】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"
    elif subscribe=="submusic":
        msg_dict["msg"]=ss_content.random_music_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【网易云每日推荐】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"
    elif subscribe=="subsexpic":
        msg_dict["msg"]=ss_content.sex_picture_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【每日美女】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"
    elif subscribe=="subweibohot":     
        msg_dict["msg"]=ss_content.weibo_hot_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【每日微博热搜】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"  
    elif subscribe=="sublifeskill":
        msg_dict["msg"]=ss_content.life_skill_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【每日生活小窍门】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"  
    elif subscribe=="subkaoyan":
        msg_dict["msg"]=ss_content.kaoyan_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【考研倒计时】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"  
    elif subscribe=="love_word":
        msg_dict["msg"]=ss_content.love_word_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【每日情话】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"  
    elif subscribe=="fuck_word":
        msg_dict["msg"]=ss_content.fuck_word_sub()
        if msg_dict["msg"]=="":
            msg_dict["msg"]="【周三骚话】订阅频道出现问题[CQ:face,id=37]，请联系蝙蝠侠"      

    send_msg(msg_dict)
    return

#处理订阅
def subscribe_handle(subscribe):
    #得到订阅账号
    numbers=get_numbers(subscribe)
    #得到好友列表账号数组
    friends=get_friends_array()
    groups=get_groups_array()
    #得到黑名单
    blacklist=get_blacklist()
    for num in numbers:
        if not num in blacklist:
            if num in friends:
                #该账号是私聊好友
                send_subscribe("private",num,subscribe)
            elif num in groups:
                #该账号是群号
                send_subscribe("group",num,subscribe)
            else:
                #可能这个账号把我删了，那么我也不必存着这个账号，从数据库中删了它
                del_number(subscribe,num)
                return 0
    return 0



#金山词霸英语名言+励志图片
def famousremark_subscribe():
    subscribe_handle("famousremark")

#必应壁纸订阅
def wallpaper_subscribe():
    subscribe_handle("subwallpaper")

#网易云随机音乐订阅
def random_music_subscribe():
    subscribe_handle("submusic")

#美女图片订阅
def sex_picture_subscribe():
    subscribe_handle("subsexpic")

#微博热搜订阅
def weibo_hot_subscribe():
    subscribe_handle("subweibohot")

#生活小技巧
def life_skill_subscribe():
    subscribe_handle("sublifeskill")

#考研倒计时
def kaoyan_subscribe():
    subscribe_handle("subkaoyan")


#莫斯科比北京早5个小时（但是放在服务器后推送是和北京时间一样的，神奇）
schedule.every().day.at("08:00").do(famousremark_subscribe)
schedule.every().day.at("11:00").do(wallpaper_subscribe)
schedule.every().day.at("13:00").do(random_music_subscribe) 
schedule.every().day.at("17:00").do(sex_picture_subscribe)    
schedule.every().day.at("09:30").do(weibo_hot_subscribe)   
schedule.every().day.at("10:00").do(life_skill_subscribe)    
schedule.every().day.at("05:30").do(kaoyan_subscribe)   



#-------------------------------------------------------------------
#特别订阅
def special_sub(nums,subtitle):
    #得到好友列表账号数组
    friends=get_friends_array()
    groups=get_groups_array()
    #得到黑名单
    blacklist=get_blacklist()   
    for num in nums:
        if not num in blacklist:
            if num in friends:
                send_subscribe("private",num,subtitle)
            elif num in groups:
                send_subscribe("group",num,subtitle)
            else:
                #该账号将我删了，没得聊，直接返回
                return 0
    return 0

#情话
def love_word_subscribe():
    special_sub(["马赛克"],"love_word")

#骚话
def fuck_word_subscribe():
    special_sub(["马赛克","马赛克"],"fuck_word")


#特别订阅-给特别的人
schedule.every().day.at("06:10").do(love_word_subscribe)    
schedule.every().wednesday.at("08:15").do(fuck_word_subscribe) 

def check_subscribe():
    schedule.run_pending()   
    return 0










