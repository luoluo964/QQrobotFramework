# coding=utf-8
import pymysql

from special_function.logging_tool import logging_put

host='10.0.0.3'
port=3306
user='user'
password='18135165419bW'
database='qqrobot'


#增加信息：往数据库中增加quest和reply
def addInfo(quest,reply):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="insert into words(id,quest,reply) VALUES(NULL,%s,%s)"
    db.begin()       #开启事务
    try:
        #执行sql语句
        cursor.execute(sql,[quest,reply])
        #提交事务
        db.commit()
    except pymysql.Error as e:
        logging_put(e)
        db.rollback()   #报错，则回滚
        return False
    db.close()
    return True

#查找信息，通过quest，查找reply
def findInfo(quest):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="select * from words WHERE quest=%s"
    db.begin() #开启事务
    #接收查找结果
    res=None
    try:
        #执行sql语句 (第二个参数即把占位符解释)
        cursor.execute(sql,quest)
        res=cursor.fetchall()
        db.commit() #提交事务
    except pymysql.Error as e:
        logging_put(e)
        db.rollback() #报错，则回滚
    db.close()

    #将查询结果（元组）返回
    return res







