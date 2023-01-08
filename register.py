import random
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from need_module import sys

class Register(object):
    def __init__(self, Login,Chat,master=None):
        self.root = master  # 定义内部变量root
        self.root.title('注册窗口')
        self.Login=Login
        self.Chat=Chat

        # 设置窗口居中
        sw = self.root.winfo_screenwidth()  # 计算水平距离
        sh = self.root.winfo_screenheight()  # 计算垂直距离
        w = 690  # 宽
        h = 520  # 高
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.root.geometry("%dx%d+%d+%d" % (w, h, (x + 160), y))
        self.root.iconbitmap(r'images/icon/register.ico')  # 设置左上角窗口图标
        self.root.resizable(0, 0)  # 窗口设置为不可放大缩小
        # # 告诉操作系统使用程序自身的dpi适配
        # ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # # 获取屏幕的缩放因子
        # ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # # 设置程序缩放
        # self.root.tk.call('tk', 'scaling', ScaleFactor / 75)
        self.creatregister()

    def creatregister(self):
        self.fr2 = Frame(self.root)
        self.fr2.pack()
        self.fr1 = Frame(self.root)
        self.fr1.pack(pady=10)

        self.benner_list = ['images/benner/banner-1.jpg', 'images/benner/banner-2.jpg', 'images/benner/banner-3.jpg',
                            'images/benner/banner-4.jpg', 'images/benner/banner-5.jpg', 'images/benner/banner-6.jpg', ]
        self.benner_img = random.choice(self.benner_list)  # 随机一张背景图

        # 图片大小：690x300
        self.pic = Image.open(self.benner_img)
        self.register_benner = ImageTk.PhotoImage(self.pic)

        # 标签 图片
        self.imgLabel = Label(self.fr2, image=self.register_benner)
        self.imgLabel.pack()

        # 标签 用户和密码
        self.label_usr = Label(self.fr1, text="用户名：")
        self.label_usr.grid(row=0, column=0)
        self.label_pwd = Label(self.fr1, text="密  码：")
        self.label_pwd.grid(row=1, column=0, pady=5)
        self.label_repwd = Label(self.fr1, text="确认密码：")
        self.label_repwd.grid(row=2, column=0)

        # 文本框 用户名
        self.var_usr_name = StringVar()
        self.entry_name = Entry(self.fr1, textvariable=self.var_usr_name)
        self.entry_name.grid(row=0, column=1)
        self.entry_name.focus_set()  # 获得焦点
        self.docheck1 = self.entry_name.register(self.usercheck)  # 自带验证功能，usercheck自定义函数
        self.entry_name.config(validate='all', validatecommand=(self.docheck1, '%P'))

        # 文本框 密码
        self.var_usr_pwd = StringVar()
        self.entry_pwd = Entry(self.fr1, textvariable=self.var_usr_pwd, show="*")
        self.entry_pwd.grid(row=1, column=1)
        self.docheck2 = self.entry_pwd.register(self.passwordcheck)
        self.entry_pwd.config(validate='all', validatecommand=(self.docheck2, '%d', '%S'))
        # 文本框 确认密码
        self.var_usr_repwd = StringVar()
        self.entry_repwd = Entry(self.fr1, textvariable=self.var_usr_repwd, show="*")
        self.entry_repwd.grid(row=2, column=1)

        self.fr3 = Frame(self.root)
        self.fr3.pack()
        # 登录
        self.root.bind('<Return>', self.reg)  # 绑定回车键
        self.bt_register = Button(self.fr3, text=" 注册 ", command=lambda: self.reg())
        self.bt_register.grid(row=1, column=1, pady=5, padx=35)
        # self.la = Label(self.fr3, width=5)
        # self.la.grid(row=0, column=0)
        self.bt_quit = Button(self.fr3, text=" 退出 ", command=sys.exit)
        self.bt_quit.grid(row=1, column=2)

        # # 底部标签
        self.fr4 = Frame(self.root)
        self.fr4.pack(side='bottom')

        self.bt_register = Button(self.fr4, text=" 返回登录", relief=FLAT, bg='#f0f0f0', command=self.register_win_close)
        self.bt_register.pack(side='left', anchor='s')
        self.la2 = Label(self.fr4, width=150)
        self.la2.pack()
        self.tsLabel2 = Label(self.fr4, text="用户注册界面 by LGH ", fg="red")
        self.tsLabel2.pack(side='right', anchor='s', pady=5)

    def register_win_close(self):
        self.fr1.destroy()
        self.fr2.destroy()
        self.fr3.destroy()
        self.fr4.destroy()  # 登录界面卸载
        self.Login(Register,self.Chat,self.root)  # 密码对，就把主窗体模块的界面加载

    def usercheck(self, what):
        if len(what) > 8:
            self.la2.config(text='用户名不能超过8个字符', fg='red')
            return False
        return True

    def passwordcheck(self, why, what):
        if why == '1':
            if what not in '0123456789':
                self.la2.config(text='密码只能是数字', fg='red')
                return False
        return True

    def reg(self, *args):

        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        usr_repwd = self.var_usr_repwd.get()

        if usr_name == '' or usr_pwd == '' or usr_repwd == '':
            messagebox.showwarning(title='提示', message="用户名密码不能为空")

        else:
            # 如果文件不存在，会自动在当前目录创建：
            conn = sqlite3.connect('yonghu.db')
            # 创建一个Cursor：
            cursor = conn.cursor()
            # 执行一条SQL语句，创建user表：
            cursor.execute('create table if not exists user(username varchar(20),password varchar(20))')

            # 查询用户名是否存在
            cursor.execute('select username from user')
            values = cursor.fetchall()
            userList = []
            for i in values:
                # print(i[0])
                userList.append(i[0])

            if usr_name in userList:
                messagebox.showwarning('提示', '用户名已存在！')
            else:
                if usr_pwd == usr_repwd:
                    # 插入数据
                    cursor.execute("insert into user (username,password) values (?,?)", (usr_name, usr_repwd))
                    if (messagebox.showinfo('提示', '注册成功！')):
                        self.root.unbind('<Return>')  # 解绑回车键事件
                        self.register_win_close()
                else:
                    messagebox.showerror('提示', '两次输入的密码不一致！')

            # 关闭Cursor:
            cursor.close()
            # 提交事务：
            conn.commit()
            # 关闭Connection：
            conn.close()
            # 下面返回字符串break使回车绑定事件只触发绑定的方法而不进行默认的换行操作
        return 'break'
