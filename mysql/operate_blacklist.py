# coding=utf-8
import pymysql

from special_function.logging_tool import logging_put
from mysql.connect_info import *

#增加账号：往数据库中增加黑名单
def add_number(number):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="insert into blacklist(id,num) VALUES(NULL,%s)"
    db.begin()       #开启事务
    try:
        #执行sql语句
        cursor.execute(sql,number)
        #提交事务
        db.commit()
    except pymysql.Error as e:
        logging_put(e)
        db.rollback()   #报错，则回滚
        return False
    db.close()
    return True

#查找账号，验证黑名单中是否有number
def exist_number(number):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="select * from blacklist WHERE num=%s"
    db.begin() #开启事务
    #接收查找结果
    res=None
    try:
        #执行sql语句 (第二个参数即把占位符解释)
        cursor.execute(sql,number)
        res=cursor.fetchall()
        db.commit() #提交事务
    except pymysql.Error as e:
        logging_put(e)
        db.rollback() #报错，则回滚
    db.close()

    #将查询结果（元组）返回
    if res:
        return True
    else:
        return False


#删除账号
def del_number(number):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="delete from blacklist where num=%s"
    db.begin() #开启事务
    try:
        #执行sql语句
        cursor.execute(sql,number)
        db.commit() #提交事务
    except pymysql.Error as e:
        logging_put(e)
        db.rollback()   #报错，则回滚
        return False
    db.close()
    return True

#得到黑名单
def get_blacklist():
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="select * from blacklist"
    db.begin() #开启事务
    #接收查找结果
    res=None
    try:
        #执行sql语句 (第二个参数即把占位符解释)
        cursor.execute(sql)
        res=cursor.fetchall()
        db.commit() #提交事务
    except pymysql.Error as e:
        logging_put(e)
        db.rollback() #报错，则回滚
    db.close()

    result=[]
    for item in res:
        result.append(item[1])
    return result

