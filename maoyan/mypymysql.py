import pymysql
import logging
import sys


# 获取logger的实例
logger = logging.getLogger("myPymysql")
# 指定logger的输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# 文件日志，终端日志对象
file_handler = logging.FileHandler("myPymysql.log")
# 文件日志按照指定的格式来写
file_handler.setFormatter(formatter)
# 可以设置日志的级别
logger.setLevel(logging.DEBUG)
# 把文件日志，终端日志对象添加到日志处理器logger中
logger.addHandler(file_handler)


class DBHelper(object):
    def __init__(self, host="127.0.0.1",
                 user="root", pwd="123456",
                 db="testdb", port=3306,
                 charset="utf8"):
        self.host = host
        self.user = user
        self.port = port
        self.password = pwd
        self.db = db
        self.charset = charset
        self.conn = None
        self.cur = None

    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user,
                                        password=self.password, port=self.port, db=self.db,
                                        charset=self.charset)
        except:
            logger.error("conn Error")
            print("conn Error")
            return False
        self.cur = self.conn.cursor()
        return True

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True

    def execute(self, sql, params=None):
        if self.connectDatabase() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                # 这里的操作可以进行批量化
                self.conn.commit()
        except:
            logger.error("execute"+sql)
            logger.error("execute"+params)
        return True

    def fetchCount(self, sql, params=None):
        if self.connectDatabase() == False:
            return -1
        self.execute(sql,params)
        return self.cur.fetchone()[0]



if __name__ == "__main__":
    dbhelper = DBHelper()
    # print(dbhelper.connectDatabase())
    # title = "英雄本色"
    # actor = "张国荣"
    # time = "2018-12-05"
    # sql = "insert into testdb.maoyan(title,actor,time) values (%s,%s,%s);"
    # params = (title, actor, time)
    # result = dbhelper.execute(sql, params)
    # if result == True:
    #     print("Ok")
    # else:
    #     print("Fail")

    print(dbhelper.close())

# 不用的时候，将日志的hanlder移除
# 否则会常驻内存
logger.removeHandler(file_handler)
