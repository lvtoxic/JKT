# coding=utf-8

import pymysql

#查询
def connMySQL():
    try:
        conn = pymysql.connect(host='132.232.53.142 ', user='lw', password='123456', db='mysql')
    except Exception as e:
        print(e.args)
    else:
        cur = conn.cursor()
        sql = 'select * from test_user'
        params = (1,)
        #单个查询
        # cur.execute(sql, params)
        # data = cur.fetchone()
        # print(data)
        cur.execute('select * from test_user')
        data=cur.fetchall()
        #多条查询
        # for item in data:
        #     print(item)
        db=[item for item in data]
        print(db)
    finally:
        cur.close()
        conn.close()

# connMySQL()

#插入
def insertMySQL():
    try:
        conn = pymysql.connect(host='132.232.53.142 ', user='lw', password='123456', db='mysql')
    except Exception as e:
        print(e.args)
    else:
        cur = conn.cursor()
        #单条语句插入
        # sql = 'insert into test_user values(%s,%s,%s,%s)'
        # params=(3,'C',18,'xian')
        #批量插入
        sql = 'insert into test_user values(%s,%s,%s,%s)'
        params=[(4,'D',18,'nanjing'),(5,'E',20,'shanghai')]
        cur.executemany(sql,params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

# insertMySQL()


#删除
def deleteMySQL():
    try:
        conn = pymysql.connect(host='132.232.53.142 ', user='lw', password='123456', db='mysql')
    except Exception as e:
        print(e.args)
    else:
        cur = conn.cursor()
        #单条删除
        sql = 'delete from test_user where id=%s'
        params=(2,)
        #批量插入
        # sql = 'insert into test_user values(%s,%s,%s,%s)'
        # params=[(4,'D',18,'nanjing'),(5,'E',20,'shanghai')]
        cur.executemany(sql,params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

# deleteMySQL()


class MySqlHelper:
    def conn(self):
        con=pymysql.connect(host='132.232.53.142 ', user='lw', password='123456', db='mysql')
        return con

    def get_one(self,sql,params):
        cur=self.conn().cursor()
        data=cur.execute(sql,params)
        result=cur.fetchone()
        return result

def checkValid(username,password):
    opera=MySqlHelper
    sql='select * from login where username=%s and password=%s'
    params=(username,password)
    return opera.get_one(sql=sql,params=params)

def info():
    username=input('输入:\n')
    password=input('密码:\n')
    result=checkValid(username,password)
    if result:
        print('成功'.format(username))
    else:
        print('错误')


info()



