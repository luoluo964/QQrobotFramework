# coding=utf-8
from mysql.operate import findInfo,addInfo
import random

#学习消息
def study_info(quest,reply):
    quest=quest.encode('utf-8')
    reply=reply.encode('utf-8')
    if len(quest)<90 and len(reply)<90:
        if addInfo(quest,reply):
            return True
    else:
        return False

#返回消息
def get_reply(quest):
    res=None
    #长度小于90才有必要查找
    if len(quest)<90:
        res=findInfo(quest)
    else:
        print("超过90的字符串不会存储在数据库中的")        
    #没有找到结果
    if not res:
        return ''
    #有结果（随机返回结果）
    index=random.randint(0,len(res)-1)
    return res[index][2]

