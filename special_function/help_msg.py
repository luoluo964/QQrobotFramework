# coding=utf-8
#这里有的符号要进行url转码  
# | %7C
# ' %27
# 换行 %0a
# 空格 %20
def private_chat_help():
    content="[CQ:face,id=63][CQ:face,id=63][CQ:face,id=63]%20专有命令：%0a"
    content+="1-调教：%27#学习%20[目标语]%20[自动回复语]%27%20%0a"
    content+="2-翻译：%27翻译%20[待翻译内容]%27%20%0a"
    content+="3-手机号码信息：%27号码信息%20[手机号码]%27%20%0a"
    content+="4-壁纸：%27壁纸%7C高清壁纸%27%20%0a"
    content+="5-头像推荐：%27头像%20[女%7C男%7C动漫]%27%20%0a"

    return content  


