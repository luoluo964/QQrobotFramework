# QQrobotFramework

## 这是什么？
这是一个QQ机器人的程序，但是它不是一个独立程序，是一个基于go-cqhttp的程序，故要结合go-cqhttp来一起使用。

## 使用思路
先在你的服务器上安装好go-cqhttp，弄好配置文件，监听指定5700端口，消息上报指定5701端口，然后再整理我的这个程序，监听在5701端口。
运行起来两个程序后，当QQ收到消息，就会通过cq上报给5701，然后我的程序就会收到上报的json数据，然后分析json数据即可。

## 需要环境
建议python3.9，mysql使用8.0，另外需要用pip安装requests、schedule、pymysql这些库。

## 有没有教程
我的这两篇文章记录了基本的起步，会很好的帮助到你。<br/>
[搭建QQ机器人](https://is-hash.com/myqqrobot)<br/>
[搭建QQ机器人2](https://is-hash.com/myqqrobot2/)<br/>
程序中敏感数据我都用“马赛克”代替了，请自行根据情况替换

## 最后
如果真能对你起到一些帮助，那麻烦给个star了，谢谢谢谢！


![alt 本来这里有张美图的，现在可能没了~](https://pbs.twimg.com/media/ErVhiL9VEAAXIIO.jpg)
