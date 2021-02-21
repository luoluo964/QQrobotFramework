# coding=utf-8
#可用接口文档：https://api.66mz8.com/docs-translation.html
#可用接口文档：https://alapi.cn/doc/show/32.html
import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

#翻译接口
def translate_api(content):
    # 带参数的get请求
    resp=requests.get(url='https://api.66mz8.com/api/translation.php', params={'info': content},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return resp_dict["fanyi"]
    else:
        return "[CQ:face,id=103]我不会！"

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
    # 带参数的get请求
    resp=requests.get(url="https://api.66mz8.com/api/bing.php", params={'format': 'json'},headers=headers)      
    resp_dict=json.loads(resp.text)
    if resp_dict["code"]==200:
        return "[CQ:image,file="+resp_dict["img_url"]+",type=show,id=40004]"
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
        return "[CQ:image,file="+resp_dict["pic_url"]+",type=show,id=40002]"
    else:
        return "建议纯黑"












