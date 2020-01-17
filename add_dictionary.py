"""
author : bjq
email : 2773487083@qq.com
env : python3.6
字典添加到words表中
"""
import pymysql

db = pymysql.connect(host="127.0.0.1",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
cur = db.cursor()

args_list = []
with open("./dict.txt", "r") as file:
    while True:
        data = file.readline()
        if not data:
            break
        data = data.split(" ", 1)
        data[1] = data[1].strip()
        data = tuple(data)
        args_list.append(data)

sql = "insert into words (word, mean) values (%s, %s)"
try:
    cur.executemany(sql, args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
