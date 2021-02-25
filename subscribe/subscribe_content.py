# coding=utf-8
from special_function.web_api_use import morning_word_api,random_wallpaper_api,life_skill_api,fuck_work_api,love_word_api,gold_hill_english_api,sex_picture,weibo_hot_api,biying_wallpaper_api,random_music_api
from datetime import datetime

#每日励志订阅
def famousremark_sub():
    gold_hill=gold_hill_english_api()
    if gold_hill!="":
        gold_hill["content"].replace('"','&quot;')        
        gold_hill["content"].replace("'",'&apos;')     
        gold_hill["note"].replace('"','&quot;')        
        gold_hill["note"].replace("'",'&apos;')     


        return "[CQ:face,id=69]每日英语频道：\n"+gold_hill["content"]+"\n"+gold_hill["note"]+"\n"+"[CQ:image,file="+gold_hill["img_url"]+"]"
    return ""


def weibo_hot_sub():
    content=weibo_hot_api()
    if content!="" and content!="这年代还有人用微博？[CQ:face,id=217]":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return "[CQ:face,id=69]每日微博热搜频道：\n"+content
    return ""    

def sex_picture_sub():
    content=sex_picture()
    if content!="" and content!="每次扫黄都有你":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return "[CQ:face,id=69]每日色图频道：\n"+content
    return ""    

def random_music_sub():
    content=random_music_api()
    if content!="" and content!="请听这首无声之曲":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return "[CQ:face,id=69]网易云每日推荐频道：\n"+content
    return ""    

def wallpaper_sub():
    content=biying_wallpaper_api()
    if content!="" and content!="有什么地方出错了~":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return "[CQ:face,id=69]每日必应壁纸频道：\n"+content
    return ""   

def love_word_sub():
    content=love_word_api()
    if content!="" and content!="没有情话不代表没有爱":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return content
    return ""       

def fuck_word_sub():
    content=fuck_work_api()
    if content!="" and content!="今天不说骚话":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return content
    return ""    

def life_skill_sub():
    content=life_skill_api()
    if content!="" and content!="用绳子把自己吊起来，你就成仙了":
        content.replace('"','&quot;')        
        content.replace("'",'&apos;')  
        return "[CQ:face,id=69]每日生活小窍门频道：\n"+content
    return ""    

def kaoyan_sub():
    year = datetime.now().year
    #构造一个专将来的时间属
    future = datetime.strptime(str(year)+'-12-24 08:00:00','%Y-%m-%d %H:%M:%S')
    #当前时间
    now = datetime.now()
    #求时间差
    delta = future - now
    days=delta.days

    word=morning_word_api()
    picture=random_wallpaper_api()
    
    word.replace('"','&quot;')        
    word.replace("'",'&apos;') 
    picture.replace('"','&quot;')        
    picture.replace("'",'&apos;')  

    #有内容
    if word!="" and word!="励什么志，你这辈子完蛋了" and picture!="" and picture!="哼，不给你看":
        content="[CQ:face,id=69]考研倒计时：\n\n"+"距离"+str(year)+"年考研还有"+str(days)+"天\n\n"+word+"\n"+picture
        return content
    return ""    



