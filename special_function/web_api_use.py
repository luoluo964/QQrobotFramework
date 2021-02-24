# coding=utf-8
import requests
import json
import random

headers = {
    'User-Agent':'马赛克'
}


#--------------------------------------------------------------------------
#接口一

#通过一个字符串数组，随机返回其中一个字符串元素
def random_str(array):
    temp=random.randint(0,len(array)-1)
    return array[temp]

#翻译接口
def translate_api(content):
    # 带参数的get请求
    resp=requests.get(url='https://api.66mz8.com/api/translation.php', params={'info': content},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return resp_dict["fanyi"]
    else:
        return random_str(["[CQ:face,id=103]我不会！","百度一下，你就知道"])

#手机号码信息接口
def number_information_api(content):
    # 带参数的get请求
    resp=requests.get(url='https://api.66mz8.com/api/phone.php', params={'tel': content},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "归属地："+resp_dict["local"]+"\n运行商："+resp_dict["operate"]
    else:
        return "唯一的信息就是：号码是"+content

#高清壁纸接口
def wallpaper_api():
    type=random_str(["美女","二次元","风景","呆萌酱"])  
    # 带参数的get请求
    resp=requests.get(url="https://api.66mz8.com/api/rand.acg.php", params={'type':type,'format': 'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["pic_url"]+",type=show,id=40004]"
    else:
        return "没什么好看的，走开！"

#头像接口
def head_picture_api(type):
    if type!="女" and type!="男" and type!="动漫":
        return '头像类型只能是“女”或者“男”或者“动漫”'
    # 带参数的get请求
    resp=requests.get(url='https://api.66mz8.com/api/rand.portrait.php', params={'type': type,'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["pic_url"]+"]"
    else:
        return "建议纯黑"

#色图(暗语)
def sex_picture_api():
    # 带参数的get请求
    resp=requests.get(url='https://api.66mz8.com/api/rand.tbimg.php', params={'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["pic_url"]+"]"
    else:
        return random_str(["[CQ:face,id=169]","已报警","呵，男人"])

#百度收录量查询
def baidu_record_api(domain):
    resp=requests.get(url='https://api.66mz8.com/api/baidu.entry.php', params={'domain':domain},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "域名:"+resp_dict['domain']+"\n收录量："+str(resp_dict['data'])
    else:
        return "这是正经网站？"


#金山词霸，每日英语
def gold_hill_english_api():
    resp=requests.get(url='https://api.66mz8.com/api/iciba.php', params={'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        result_dict={"note":resp_dict['note'],"content":resp_dict['content'],"img_url":resp_dict['img_url']}
        return result_dict
    else:
        return ""


#每日必应壁纸
def biying_wallpaper_api():
    resp=requests.get(url='https://api.66mz8.com/api/bing.php', params={'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return resp_dict["title"]+"\n"+"[CQ:image,file="+resp_dict["img_url"]+"]"
    else:
        return "有什么地方出错了~"

#网易云随机音乐
def random_music_api():
    resp=requests.get(url='https://api.66mz8.com/api/rand.music.163.php', params={'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:music,type=custom,audio="+resp_dict["music_url"]+",title="+resp_dict["name"]+"]"
    else:
        return "请听这首无声之曲"    
    return

#每日美女
def sex_picture():
    type=random_str(["美女","性感","制服"])  
    resp=requests.get(url='https://api.66mz8.com/api/rand.img.php', params={'format':'json','type':type},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["pic_url"]+"]"
    else:
        return "每次扫黄都有你"    
    return

#获取QQ头像
def get_qq_headpic_api(qq):
    resp=requests.get(url='https://api.66mz8.com/api/qq.logo.php', params={"qq":qq,'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["qlogo"]+"]"
    else:
        return "该用户的QQ头像是透明的"    
    return

#骚话
def fuck_work_api():
    resp=requests.get(url='https://api.66mz8.com/api/sweet.php', params={'format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return resp_dict['sweet']
    else:
        return "今天不说骚话"    
    return

#壁纸竖屏图片
def random_wallpaper_api():
    resp=requests.get(url='https://api.66mz8.com/api/rand.img.php', params={'type':'壁纸','format':'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["pic_url"]+"]"
    else:
        return "哼，不给你看"    
    return    


#--------------------------------------------------------------------------
token="马赛克"

def feeling_a_word_api():
    resp=requests.get(url='https://v2.alapi.cn/api/hitokoto', params={'token':token},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return resp_dict['data']['hitokoto']+"\n    ————"+resp_dict['data']['from']
    else:
        return random_str(["[CQ:face,id=75]","人静了","睡觉吧[CQ:face,id=63]"])


def news_api():
    type=["baidu","weibo","zhihu"]
    resp=requests.get(url='https://v2.alapi.cn/api/tophub/get', params={'token':token,"type":type},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        title=resp_dict["data"]["name"]
        main_content=resp_dict["data"]["list"]
        content=title+"\n"
        for index in range(5):
            content+="[CQ:share,url="+main_content[index]["link"]+",title="+main_content[index]["title"]+"]\n"+main_content[index]["title"]+"\n"
            content.replace('#','%23')
        return content
    else:
        return random_str(["[CQ:face,id=217]我不关心时事","最大的新闻就是没有新闻"])

#微博热搜
def weibo_hot_api():
    resp=requests.get(url='https://v2.alapi.cn/api/new/wbtop', params={'token':token,"num":5},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        main_content=resp_dict["data"]
        content=""
        for index in range(5):
            content+=main_content[index]["hot_word"]+main_content[index]["url"]+"\n"
            content.replace('#','%23')
        return content
    else:
        return "这年代还有人用微博？[CQ:face,id=217]"



#情话（给莹莹专用）
def love_word_api():
    resp=requests.get(url='https://v2.alapi.cn/api/qinghua', params={'token':token,"format":"json"},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        content=resp_dict["data"]["content"]
        qq_head=get_qq_headpic_api("964939451")
        return content+"[CQ:face,id=63]\n"+qq_head
    else:
        return "没有情话不代表没有爱"


#------------------------------------------------------
#接口三：https://www.tianapi.com/
key='马赛克'


#早安励志语
def morning_word_api():
    resp=requests.get(url='http://api.tianapi.com/txapi/zaoan/index', params={'key':key},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        content=resp_dict["newslist"][0]["content"]
        return content
    else:
        return "励什么志，你这辈子完蛋了"

#生活小窍门
def life_skill_api():
    resp=requests.get(url='http://api.tianapi.com/txapi/qiaomen/index', params={'key':key},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        content=resp_dict["newslist"][0]["content"]
        return content
    else:
        return "用绳子把自己吊起来，你就成仙了"




















