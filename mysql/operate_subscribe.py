# coding=utf-8
#订阅

import pymysql

from special_function.logging_tool import logging_put
from mysql.connect_info import *


#增加账号：往数据库中增加订阅号
def add_number(table,number):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="insert into "+table+"(id,num) VALUES(NULL,%s)"
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

def exist_number(table,number):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="select * from " +table+" WHERE num=%s"
    db.begin() #开启事务
    #接收查找结果
    res=()
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
    if len(res)>0:
        return True
    else:
        return False


def get_numbers(table):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="select * from "+table
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


def del_number(table,number):
    #连接数据库
    db=pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    #创建一个游标
    cursor=db.cursor()

    #sql语句
    sql="delete from "+table+" where num=%s"
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













