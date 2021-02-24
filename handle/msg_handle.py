# coding=utf-8
#该文件主要是对主文件中得到的字典中得到关键数据的方法

#获取上报类型：message、notice、request
def get_post_type(msg):
    return msg['post_type']

#获取信息类型 群聊/私聊 group/private
def get_message_type(msg):
    return msg['message_type']

#获取群号/私聊qq号
def get_number(msg):
    if get_message_type(msg) == 'group':
        return msg['group_id']
    elif get_message_type(msg) == 'private':
        return msg['user_id']

# 获取信息发送者的QQ号
def get_user_id(msg):
    return msg['user_id']

#获取发送的信息
def get_raw_message(msg):
    return msg['raw_message']

#改变发送的信息
def set_raw_message(msg,new_info):
    msg['raw_message']=new_info


#得到通知类型
def get_notice_type(msg):
    return msg['notice_type']



