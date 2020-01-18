"""
author : bjq
email : 2773487083@qq.com
env : python3.6
dict 数据处理
"""

import pymysql


class Database:
    def __init__(self, database):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database=database,
                                  charset='utf8')

        # 生成游标对象 (操作数据库,执行sql语句,获取结果)
        self.cur = self.db.cursor()

    # 关闭游标和数据库连接
    def close(self):
        self.cur.close()
        self.db.close()

    # 验证注册
    def register(self, name, passwd):
        sql = "select name from user where name='%s'" % (name)
        self.cur.execute(sql)
        # 如果查到内容返回False
        if self.cur.fetchone():
            return False
        # 插入数据
        sql = "insert into user (name, passwd) values (%s, %s)"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 验证登录
    def login(self, name, passwd):
        sql = "select name from user where name = %s and passwd = %s"
        self.cur.execute(sql, [name, passwd])
        if self.cur.fetchone():
            return True
        else:
            return False

    # 查询单词
    def find(self, word):
        # 查询单词
        sql = "select mean from words where word = %s"
        self.cur.execute(sql, [word])
        return self.cur.fetchone()

    # 添加历史记录
    def insert_history(self, name, word):
        # 插入历史记录
        sql = "insert into hist (name, word) values (%s, %s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    # 查询历史记录
    def history(self, name):
        sql = "select word,time from hist where name=%s order by time desc limit 10"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()


if __name__ == '__main__':
    db = Database("dict")
    data = db.history("bjq")
    for i in data:
        print("%s %s" % (i[0], i[1]))
