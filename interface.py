"""
author : bjq
email : 2773487083@qq.com
env : python3.6
系统界面
"""
def primary_interface():
    print("╭-------------------╮")
    print("|\t\t1.登录\t\t|")
    print("|\t\t2.注册\t\t|")
    print("|\t\t3.退出\t\t|")
    print("╰-------------------╯")
    while True:
        num = input("请选择:")
        if num == "1":
            pass

def login_interface():
    pass

def register_interface():
    pass

if __name__ == '__main__':
    primary_interface()