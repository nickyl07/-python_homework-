import pymysql
# 获取数据库连接的方法
def get_connection():
    connection = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
    return connection 
 
# 初始化的时候从数据库中查询学生信息
def query():
    connection = get_connection()
    # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
    cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
    # 写sql语句
    sql = "select * from user"
    try:
        cur.execute(sql)
        students = cur.fetchall()
        """
            此处判断很重要，如果数据库中没有记录，则会结果是一个空的元组类型，
            如果有记录，则结果是list类型，所以可以根据类型来判断数据库是否为空，
            如果不是就返回一个空列表。
        """
        if type(students) == list:
            return students
        else:
            return []
    except Exception as e:
        raise e
    finally:
        connection.close()  # 关闭连接

def query2():
    connection = get_connection()
    # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
    cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
    # 写sql语句
    sql = "select * from book"
    try:
        cur.execute(sql)
        students = cur.fetchall()
        """
            此处判断很重要，如果数据库中没有记录，则会结果是一个空的元组类型，
            如果有记录，则结果是list类型，所以可以根据类型来判断数据库是否为空，
            如果不是就返回一个空列表。
        """
        if type(students) == list:
            return students
        else:
            return []
    except Exception as e:
        raise e
    finally:
        connection.close()  # 关闭连接  

# 添加用户 -- 直接添加到数据库里面
def user_insert(user):
    connection = get_connection()
    # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
    cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
    # 写sql语句
    sql = "insert into user(id,admin,password,role,email) values('%s','%s','%s','%s','%s')"
    sid = user['id']
    admin = user['admin']
    password = user['password']
    role = user['role']
    email=user['email']
    try:
        cur.execute(sql % (sid,admin,password,role,email))
        connection.commit()
    except Exception as e:
        # 错误回滚
        connection.rollback()
        raise e
    finally:
        connection.close()  # 关闭连接

def book_insert(book):
    connection = get_connection()
    # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
    cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
    # 写sql语句
    sql = "insert into book(bid,name,author,press,count) values('%s','%s','%s','%s','%s')"
    bid = book['bid']
    name = book['name']
    press = book['author']
    author = book['press']
    count = book['count']
    try:
        cur.execute(sql % (bid,name,author,press,count))
        connection.commit()
    except Exception as e:
        # 错误回滚
        connection.rollback()
        raise e
    finally:
        connection.close()  # 关闭连接  
 
# 删除学生 --直接从数据库里面删除
def stu_delete(sid):
    connection = get_connection()
    cur = connection.cursor()
    sql = "delete from user where id = '%s'"
    try:
        cur.execute(sql % sid)
        connection.commit()
    except Exception as e:
        # 错误回滚
        connection.rollback()
        raise e
    finally:
        connection.close()  # 关闭连接

def book_delete(bid):
    connection = get_connection()
    cur = connection.cursor()
    sql = "delete from book where bid = '%s'"
    try:
        cur.execute(sql % bid)
        connection.commit()
    except Exception as e:
        # 错误回滚
        connection.rollback()
        raise e
    finally:
        connection.close()  # 关闭连接  
 
# 修改学生信息
def user_modify(user):
    connection = get_connection()
    cur = connection.cursor()
    sid = user['id']
    admin = user['admin']
    password = user['password']
    role = user['role']
    email=user['email']
    sql = "update user set admin='%s',password='%s',role='%s',email='%s' where id='%s'"
    try:
        cur.execute(sql % (admin, password, role, email,sid))
        connection.commit()
    except Exception as e:
        # 错误回滚
        connection.rollback()
        raise e
    finally:
        connection.close()  # 关闭连接