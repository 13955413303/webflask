

import pymysql

def insert_info(name,age):
    # 连接database
    conn = pymysql.connect(host="localhost",user="root",password="123456",database="flask_test",charset="utf8")
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 定义要执行的SQL语句
    # sql = """
    # CREATE TABLE info (
    # name CHAR(10) NOT NULL UNIQUE,
    # age TINYINT NOT NULL
    # )ENGINE=innodb DEFAULT CHARSET=utf8;
    # """
    sql = """
    INSERT INTO info (name,age) VALUES('%s',%s);
    """
    # 执行SQL语句
    print(sql%(name,age))
    cursor.execute(sql%(name,age))
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.commit()
    conn.close()

def select_info(name):
    # 连接database
    conn = pymysql.connect(host="localhost",user="root",password="123456",database="flask_test",charset="utf8")
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = " select * from {} where name = '{}';".format('info',name)
    # 执行SQL语句
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.commit()
    conn.close()
    return result

