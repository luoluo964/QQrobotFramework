# coding=utf-8
#这里有的符号要进行url转码  
# | %7C
# ' %27
# 换行 %0a
# 空格 %20
def private_chat_help():
    content="[CQ:face,id=63][CQ:face,id=63][CQ:face,id=63]%20专有指令：%0a%0a"
    content+="1-调教：%27#学习%20[目标语]%20[自动回复语]%27%20%0a"
    content+="2-翻译：%27翻译%20[待翻译内容]%27%20%0a"
    content+="3-手机号码信息：%27号码信息%20[手机号码]%27%20%0a"
    content+="4-壁纸：%27壁纸%7C高清壁纸%27%20%0a"
    content+="5-头像推荐：%27头像%20[女%7C男%7C动漫]%27%20%0a"
    content+="6-新闻：%27新闻%27%20%0a"
    content+="%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日英语]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日必应壁纸]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[网易云每日推荐]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日微博热搜]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日生活小窍门]%27%20%0a"
    content+="[CQ:face,id=203]将%27#订阅%27换成%27#取消订阅%27，即可取消相应订阅%0a"
    content+="%0a"
    content+="%20关闭机器人：%27#关机%27%20%0a"
    content+="更多指令和订阅请自行触发[CQ:face,id=21]"

    return content  

def group_chat_help():
    content="[CQ:face,id=63][CQ:face,id=63][CQ:face,id=63]%20专有指令：%0a"
    content+="1-翻译：%27翻译%20[待翻译内容]%27%20%0a"
    content+="2-手机号码信息：%27号码信息%20[手机号码]%27%20%0a"
    content+="3-壁纸：%27壁纸%7C高清壁纸%27%20%0a"
    content+="4-头像推荐：%27头像%20[女%7C男%7C动漫]%27%20%0a"
    content+="5-新闻：%27新闻%27%20%0a"
    content+="%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日英语]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日必应壁纸]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[网易云每日推荐]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日微博热搜]%27%20%0a"
    content+="[CQ:face,id=69]订阅频道：%27#订阅%20[每日生活小窍门]%27%20%0a"
    content+="[CQ:face,id=203]将%27#订阅%27换成%27#取消订阅%27，即可取消相应订阅%0a"
    content+="%0a"    
    content+="%20关闭机器人：%27#关机%27%20%0a"
    content+="更多指令和订阅请自行触发[CQ:face,id=21]"

    return content  


