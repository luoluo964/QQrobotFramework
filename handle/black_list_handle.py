# coding=utf-8
import handle.msg_handle as pick
from socket_operate.client  import send_msg
from mysql.operate_blacklist import add_number,del_number,exist_number
from special_function.logging_tool import logging_put



#黑名单记得要将自己的账号给加进去


def check_pass(message):
    if pick.get_post_type(message)=="message":  
        if pick.get_message_type(message)=="private":
            command=pick.get_raw_message(message).split(" ")[0]
            number=str(pick.get_number(message))
            msg_dict={ 
                "msg_type":"private", 
                "number":pick.get_number(message), 
                "msg":"" 
            }
            #消息来源在黑名单中，则只识别是不是“#开机”
            if exist_number(number):
                #当前发消息者面前，我们是关机的
                if command=="#开机":
                    logging_put(number+"开启了我，执行者："+str(pick.get_user_id(message)))
                    #从黑名单中移除该number
                    del_number(number)
                    msg_dict['msg']="我们又见面了"
                    send_msg(msg_dict)
                #这次消息都不予通过
                return False
            else:
                #当前发消息者面前，我们是开机的
                if command=="#关机":
                    logging_put(number+"关闭了我，执行者："+str(pick.get_user_id(message)))
                    #向黑名单中加人该number
                    add_number(number)
                    msg_dict['msg']="使用“#开机”就可以再次开启我"
                    send_msg(msg_dict)
                    return False
                elif command=="#开机":
                    msg_dict['msg']="我现在就是开机状态[CQ:face,id=22]"
                    send_msg(msg_dict)
                    return False
                else:
                    return True
        elif pick.get_message_type(message)=="group":
            if pick.get_raw_message(message).split(' ')[0]=="[CQ:at,qq=1750133059]":
                #方便还原message
                ori=pick.get_raw_message(message)
                #更新原数据的原始信息
                pick.set_raw_message(message,pick.get_raw_message(message).split(' ',1)[1])

                command=pick.get_raw_message(message).split(" ")[0]
                number=str(pick.get_number(message))
                msg_dict={ 
                    "msg_type":"group", 
                    "number":pick.get_number(message), 
                    "msg":"" 
                }
                #消息来源在黑名单中，则只识别是不是“#开机”
                if exist_number(number):
                    #当前发消息者面前，我们是关机的
                    if command=="#开机":
                        logging_put(number+"开启了我，执行者："+str(pick.get_user_id(message)))
                        #从黑名单中移除该number
                        del_number(number)
                        msg_dict['msg']="我们又见面了"
                        send_msg(msg_dict)
                    #这次消息都不予通过
                    return False
                else:
                    #当前发消息者面前，我们是开机的
                    if command=="#关机":
                        logging_put(number+"关闭了我，执行者："+str(pick.get_user_id(message)))
                        #向黑名单中加人该number
                        add_number(number)
                        msg_dict['msg']="使用“#开机”就可以再次开启我"
                        send_msg(msg_dict)
                        return False
                    elif command=="#开机":
                        msg_dict['msg']="我现在就是开机状态[CQ:face,id=22]"
                        send_msg(msg_dict)
                        return False
                    else:
                        #还原消息        
                        pick.set_raw_message(message,ori)        
                        return True            
            else:
                if exist_number(number):
                    return False
                else:
                    return True
    elif pick.get_post_type(message)=="notice" or pick.get_post_type(message)=="request":
        try:
            user_id=message['user_id']
        except BaseException as e:
            #如果user_id都没有，则直接拦截      
            return False
        #再尝试得到群号
        try:
            group_id=message['group_id']
        except BaseException as e:
            #有user_id，没有群id   
            if exist_number(message['user_id']):
                return False
            else:
                return True
        #有群id
        if exist_number(message['group_id']):
            return False
        else:
            return True
    else:
        #三大消息以外应该是心跳消息，通行
        return True 












