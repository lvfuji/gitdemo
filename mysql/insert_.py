import pymysql

db = pymysql.connect("localhost","root","123456")
cursor = db.cursor()
cursor.execute("create database user;")
cursor.execute("use user;")
cursor.execute("create table client(id int,name varchar(20),\
    passwd char(20),time varchar(30),friend varchar(10000));")
db.commit()
cursor.close()
db.close()