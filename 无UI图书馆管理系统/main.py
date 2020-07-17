import pymysql
from base import get_connection,query,query2,user_insert,book_insert,stu_delete,book_delete,user_modify
from menu import display_menu,menu1,menu2,A,B,get_choice
import operator
from prettytable import PrettyTable
import pandas as pd

name_list = []  # 存储读者信息字典，读者信息用字典存，再用列表存储字典
book_list = []  

# 检查id是否重复或者有误
def check_id(new_id):
    flag = True
    while flag:
        # 先检查是不是纯数字再去考虑是否重复的事情，如果不是纯数字直接pass
        if new_id.isdigit():
            for i in range(len(name_list)):
                if name_list[i]['id'] == new_id:
                    new_id = check_id(input("您输入的借阅卡号码重复，请重新输入："))
            flag = False
        else:
            new_id = input("您输入的借阅卡有误，请重新输入：")
    return new_id

def check_bid(new_bid):
    flag = True
    while flag:
        # 先检查是不是纯数字再去考虑是否重复的事情，如果不是纯数字直接pass
        if new_bid.isdigit():
            for i in range(len(book_list)):
                if book_list[i]['bid'] == new_bid:
                    new_bid = check_bid(input("您输入的图书id重复，请重新输入："))
            flag = False
        else:
            new_bid = input("您输入的图书id有误，请重新输入：")
    return new_bid 
 
# 添加学生信息 返回学生信息字典
def add_name():
    new_info = {}
    new_id = check_id(input("请输入id："))
    new_info['id'] = new_id
    new_name = input("请输入用户名：")
    new_info['admin'] = new_name
    new_password = input("请输入密码：")
    new_info['password'] = new_password
    new_role = input("请输入权限（管理员为1，普通用户为0）：")
    new_info['role'] = new_role
    new_email = input("请输入邮箱：")
    new_info['email'] = new_email
    name_list.append(new_info)
    # 将新学生信息添加到数据库中
    user_insert(new_info)
    print("添加成功！")

# 添加图书信息 返回图书信息字典
def add_book():
    new_binfo = {}
    new_bid = check_bid(input("请输入图书编号："))
    new_binfo['bid'] = new_bid
    new_book = input("请输入书名：")
    new_binfo['name'] = new_book
    new_author = input("请输入作者：")
    new_binfo['author'] = new_author
    new_press = input("请输入出版社：")
    new_binfo['press'] = new_press
    new_count = input("请输入数量：")
    new_binfo['count'] = new_count
    book_list.append(new_binfo)
    # 将新图书信息添加到数据库中
    book_insert(new_binfo)
    print("添加成功！")  
 
# 查询所有读者信息  --是从数据库中查询信息的
def find_all():
    print("=" * 30)
    global name_list
    name_list = query()
    O=pd.DataFrame(name_list)
    Q=PrettyTable()
    Q.add_column('id',O['id'].values)
    Q.add_column('admin',O['admin'].values)
    Q.add_column('password',O['password'].values)
    Q.add_column('role',O['role'].values)
    Q.add_column('email',O['email'].values)
    print(Q)
    print("=" * 30)

# 查询所有图书信息  --是从数据库中查询信息的
def find_allbook():
    print("=" * 30)
    global book_list
    book_list = query2()
    O=pd.DataFrame(book_list)
    Q=PrettyTable()
    Q.add_column('bid',O['bid'].values)
    Q.add_column('name',O['name'].values)
    Q.add_column('author',O['author'].values)
    Q.add_column('press',O['press'].values)
    Q.add_column('count',O['count'].values)
    print(Q)
    print("=" * 30) 
 
# 删除学生信息
def del_name():
    del_id_is = input("请输入要删除的读者id：")
    flag = False
    index = 0
    for i in range(len(name_list)):
        if name_list[i]['id'] == del_id_is:
            flag = True
            index = i
            break
    if flag:
        name_list.pop(index)
        stu_delete(del_id_is)
        print("删除成功！")
    else:
        print("读者未找到！请检查id输入是否有误！")

def del_book():
    del_id_is = input("请输入要借出的图书编号：")
    flag = False
    index = 0
    for i in range(len(book_list)):
        if book_list[i]['id'] == del_id_is:
            flag = True
            index = i
            break
    if flag:
        book_list.pop(index)
        book_delete(del_id_is)
        print("借出成功！")
    else:
        print("图书未找到！请检查编号输入是否有误！")   
 
# 名字修改细节函数
def choice_of_name(index):
    while True:
        choice = input("请输入要修改读者的(1.用户名 2.密码 3.邮箱 4.权限 5.全部修改)：")
        if choice == '5':
            """
                要做到内存中的数据与数据库中数据同时修改的话，我做的是先修改本地的数据，
                再对数据库中的数据做修改
            """
            new_name = input("请输入新的用户名：")
            name_list[index]['admin'] = new_name
            new_password = check_password(input("请输入密码："))
            name_list[index]['password'] = new_password
            new_email = input("请输入邮箱：")
            name_list[index]['email'] = new_email
            new_role = input("请输入权限：")
            name_list[index]['role'] = new_role          
            stu_modify(name_list[index])
            break
        elif choice == '1':
            new_name = input("请输入新的用户名：")
            name_list[index]['name'] = new_name
            stu_modify(name_list[index])
            break
        elif choice == '2':
            new_password = input("请输入密码：")
            name_list[index]['password'] = new_password
            stu_modify(name_list[index])
            break
        elif choice == '3':
            new_email = input("请输入email：")
            name_list[index]['email'] = new_email
            stu_modify(name_list[index])
            break
        elif choice =='4':
            new_role = input("请输入权限：")
            name_list[index]['role'] = new_role          
            stu_modify(name_list[index])            
        else:
            print("输入有误，请重新输入！")
  
# 修改学生信息
def re_name():
    id_is = input("请输入要修改的读者id：")
    flag = False
    index = 0
    # 先找到要修改的学生的下标
    for i in range(len(name_list)):
        if name_list[i]['id'] == id_is:
            flag = True
            index = i
            break
    if flag:
        choice_of_name(index)
        print("修改成功！")
    else:
        print("修改失败，读者信息未找到！") 
 
# 查询单个学生信息 --并不是从数据库中查询的，还是从内存中查询的
def find_name():
    find_id_is = input("请输入要查询的读者id：")
    flag = False
    index = 0
    for i in range(len(name_list)):
        if name_list[i]['id'] == find_id_is:
            flag = True
            index = i
            break
    if flag:
        print("读者查询到，读者信息为：")
        
        print(name_list[index]['id'], name_list[index]['admin'], name_list[index]['password'], name_list[index]['email'])
    else:
        print("读者未找到！")

#查询图书信息
def find_book():
    find_id_is = input("请输入要查询的图书书名：")
    flag = False
    index = 0
    for i in range(len(book_list)):
        if book_list[i]['name'] == find_id_is:
            flag = True
            index = i
            break
    if flag:     
        print("图书查询到，图书信息为：")
        print("=" * 30)           
        print("bid——name—————————press—————author—count")
        print(book_list[index]['bid'], book_list[index]['name'], book_list[index]['author'], book_list[index]['press'],book_list[index]['count'])
        print("=" * 30) 
    else:
        print("图书未找到！")  

#借书
def borrowbook():
    connection = get_connection()
    cur = connection.cursor()    
    name=str(input('请输入要借的图书书名：'))
    sql="""select * from book where (name = %s) """
    flag=cur.execute(sql,[name])
    connection.commit()
    if flag==1:
        sql="""select * from book where count = %s"""
        connection.commit()
        result=cur.fetchone()[4]
        if result!=0:
            print("成功借出")
            sql="""update book set count = count - 1 """
            cur.execute(sql)
            connection.commit()
    else:
        print("图书借光或者未找到图书")

def backbook():
    connection = get_connection()
    cur = connection.cursor()    
    name=str(input('请输入要归还的图书书名：'))
    sql="""select * from book where (name = %s) """
    flag=cur.execute(sql,[name])
    connection.commit()
    if flag==1:
        print("成功归还")
        sql="""update book set count = count + 1 """
        cur.execute(sql)
        connection.commit()
    else:
        print("没有该图书")
 
# 初始化函数，从数据库中查询到的赋值给name_list
def name_init():
    try:
        global name_list
        name_list = query()
        print("成功获取数据库中数据！")
    except Exception as e:
        raise e

def book_init():
    try:
        global book_list
        book_list = query2()
        print("成功获取数据库中数据！")
    except Exception as e:
        raise e  
 
#新书上架
def newbook():
    newbook_list= (sorted(book_list, key=lambda book_list:book_list['bid'],reverse=True))
    df=pd.DataFrame(newbook_list)
    tb = PrettyTable()
    tb.add_column('bid', df['bid'].values)
    tb.add_column('name', df['name'].values)
    tb.add_column('author', df['author'].values)
    tb.add_column('press', df['press'].values)
    tb.add_column('count', df['count'].values)
    print(tb)

#登录注册
def login():
    connection = get_connection()
    cur = connection.cursor() 
    pd =int(input('1.登录\n2.注册\n3.退出\n'))
#登陆
    if pd == 1:
        print('**************开始登陆************')
        id = str(input("请输入账号："))
        password = str(input("请输入密码："))

    #数据库表中查询是否含有该账号和密码
        sql = """select * from user where  (id = %s) and (password = %s) """
        flag = cur.execute(sql,[id,password])
        connection.commit()
        if flag == 1:
            print("登陆成功")
            #connection.commit()        
            sql = """select * from user where (role = %s) """
            connection.commit()            
            if cur.fetchone()[3] != 0: 
                print("管理员账户")
                menu1()
                key = get_choice()
                if key=='1':
                    A()
                    key = get_choice()
                    if key=='1':
                        add_name()
                    elif key=='2':
                        del_name()
                    elif key=='3':
                        re_name()
                    elif key=='4':
                        find_name()
                    elif key=='5':
                        find_all()
                elif key=='2':
                    B()
                    key = get_choice()
                    if key=='1':
                        del_book()
                    elif key=='2':
                        add_book()
                    elif key=='3':
                        find_book()
                    elif key=='4':
                        find_allbook()
                    elif key=='6':
                        exit_name = False
                    else:
                        print("请输入正确的数值！")   
                elif key=='3':
                    exit_name = False
                else:
                    print("请输入正确的数值！")    
            else:
                print("普通账户")
                menu2()
                key = get_choice()
                if key=='1':
                    borrowbook()
                elif key=='2':
                    backbook()
                elif key=='3':
                    find_book()
                elif key=='4':
                    find_allbook()
                elif key=='5':
                    exit_name = False
                else:
                    print("请输入正确的数值！")                       
        #登陆成功，显示用户信息
        else:
            print("账号或密码错误")
        connection.close()

    elif pd == 2:
        print('**************开始注册************')
        id = str(input('请输入id：'))
        admin=str(input('请输入用户名：'))
        password = str(input('请输入密码：'))
        email=str(input('请输入邮箱：'))
        role=0

    # 判断id是否已被注册
        sql = """select * from user where id = %s"""
        flag = cur.execute(sql, [id])
        connection.commit()
        if flag == 1:
            print("id已存在，请重新注册")
        else:
            sql = """insert into user(id,admin,password,role,email) values (%s,%s,%s,%s,%s)"""
            cur.execute(sql, [id,admin, password,role,email])
            connection.commit()
            print("注册成功")
    else:
        print("注册失败")

def main():
    name_init()
    book_init()
    exit_name = True
    while exit_name:
        display_menu()
        key = get_choice()
        if key == '1':
            login()
        elif key == '2':
            newbook()
        elif key == '3':
            print('敬请期待')
        elif key == '4':
            exit_name = False
        else:
            print("请输入正确的数值！")  
main()