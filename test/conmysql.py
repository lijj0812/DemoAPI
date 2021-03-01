#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 10:39
# @Author  : Gavin

import pymysql
#打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", db="mysql", charset='utf8')
#使用cursor获取操作游标
cursor = db.cursor()
#执行sql
cursor.execute('DROP TABLE IF EXISTS login_user')
#
tablename1="emp"
sql = 'create table login_user(id INT,grant_type CHAR(10),username varchar(22),password varchar(22))'
#
try:
    cursor.execute(sql)
    db.commit()
except:
    print('表 %s 已存在' %tablename1)
    db.rollback()
#关闭数据库连接
db.close()
