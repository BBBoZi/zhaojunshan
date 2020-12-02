# -*- coding:utf-8 -*-
import pymysql

db = pymysql.connect('172.0.0.1','root','root','avIdol')

cursor = db.cursor()

sql = """create table beautyGirls (
   name char(20) not null,
   age int)"""
cursor.execute(sql)

sql = "insert into beautyGirls(name, age) values ('Mrs.cang', 18)"

try:
    cursor.execute(sql)
    db.commit() #数据更新
except:
    db.rollback()

db.close()

#删除数据
sql = "delete from beautyGirls where age = '%d'" % (18)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

#将csv 中的内容插入到 MySQL 中

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('xsb.csv')

# 当engine连接的时候我们就插入数据
engine = create_engine('mysql://root@localhost/xsb?charset=utf8')
with engine.connect() as conn, conn.begin():
    df.to_sql('xsb', conn, if_exists='replace')