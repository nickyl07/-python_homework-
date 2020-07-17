def display_menu():
    print("-" * 30)
    print("   图书馆管理系统  v8.8  ")
    print("1.登录/注册")
    print("2.新书上架")
    print("3.热书推荐")
    print("4.退出系统")
    print("-" * 30)
 
def menu1():
    print("-" * 30) 
    print("   管理员入口  ")
    print("1、读者管理") 
    print("2、图书管理")
    print("3、退出系统")        
    print("-" * 30)

def A():
    print("-" * 30)
    print("  读者管理  ")  
    print("1.添加读者信息")
    print("2.删除读者信息")
    print("3.修改读者信息")
    print("4.查询单个读者信息")
    print("5.查询所有读者信息")
    print("6.退出系统")
    print("-" * 30)
def B():
    print("-" * 30)
    print("  图书管理  ")  
    print("1.删除图书")#删除
    print("2.添加图书")#添加
    print("3.查询图书信息")
    print("4.查询所有图书信息")
    print("6.退出系统")
    print("-" * 30) 

def menu2():
    print("-" * 30) 
    print("   读者入口  ")
    print("1.借书登记")#删除
    print("2.还书登记")#添加
    print("3.查询图书信息")
    print("4.查询所有图书信息")
    print("5.退出系统")
    print("-" * 30) 

def get_choice():
    selected_key = input("请输入选择的序号：")
    return selected_key