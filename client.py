"""
Author: Hmily
Github: https://github.com/ihmily
Date: 2022-06-30 18:25:27
Copyright (c) 2022 by Hmily, All Rights Reserved.
Function: Multi person chat room
"""

# 客户端
import socket
import threading
import time
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Treeview
from stickers import *
from login import *
from register import *

'''
参数：
    sock：定义一个实例化socket对象
    server：传递的服务器IP和端口
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 使用udp传输方式
server = ('127.0.0.1', 9999)


class ChatClient():
    def __init__(self, name, scr1, scr2, fri_list, obj_emoji):
        self.name = name
        self.scr1 = scr1
        self.scr2 = scr2
        self.fri_list = fri_list
        self.obj_emoji = obj_emoji

    def toSend(self, *args):
        self.msg = self.scr2.get(1.0, 'end').strip()
        self.send(self.msg)
        if self.msg != '':
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.scr1.configure(state=NORMAL)
            self.scr1.insert("end", "{} {}:\n".format(self.name, now_time), 'green')
            self.scr1.insert("end", self.msg + '' + '\n')
            self.scr1.see(END)
            self.scr2.delete('1.0', 'end')
            self.scr1.config(state=DISABLED)
            print(f'{self.name}：成功发送消息', self.msg.strip())
            return "break"

    def toPrivateSend(self, *args):
        self.msg = self.scr2.get(1.0, 'end').strip()
        self.scr2.delete('1.0', 'end')
        send_type, send_file = self.private_send(self.msg)
        if self.msg != '' and self.fri_list.selection() != ():
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.scr1.configure(state=NORMAL)
            tar_name = self.fri_list.selection()[0]
            print('私聊用户名称:', tar_name)
            self.scr1.insert("end", "{} {}:\n".format(self.name, now_time), 'green')
            if send_type == 'text':
                self.scr1.insert("end", f'{self.msg}')
                self.scr1.insert("end", f'  |私聊{tar_name}\n', 'zise')
                self.scr1.see(END)
                self.scr2.delete('1.0', 'end')
                self.scr1.config(state=DISABLED)
                print(f'{self.name}：成功发送消息', self.msg, '[私聊]')
            else:
                self.scr1.insert("end", f'{send_file} 文件正在发送中，等待对方接收', 'shengzise')
                self.scr1.insert("end", f' |目标:{tar_name}\n', 'zise')
                self.scr1.see(END)
                print(f'{self.name}：成功发送文件', send_file, '[私聊]')

    def Get_File(self, filename):
        fpath, tempfilename = os.path.split(filename)
        fname, extension = os.path.splitext(tempfilename)
        return fpath, fname, extension, tempfilename

    def send_file(self, fileType, fileName, filePath):
        message = {}
        message["chat_type"] = "private"
        message["message_type"] = "ask-file"
        message["file_type"] = fileType
        message["file_name"] = fileName
        message["send_user"] = self.name
        message["recv_user"] = self.fri_list.selection()[0]
        message["content"] = filePath
        jsondata = json.dumps(message, ensure_ascii=False)
        sock.sendto(jsondata.encode('utf-8'), server)

    def cut_data(self, fhead, data):
        for i in range(fhead // 1024 + 1):
            time.sleep(0.0000000001)  # 防止数据发送太快，服务器来不及接收出错
            if 1024 * (i + 1) > fhead:  # 是否到最后
                sock.sendto(data[1024 * i:], server)  # 最后一次剩下的数据传给对方
                print('第' + str(i + 1) + '次发送文件数据')
            else:
                sock.sendto(data[1024 * i:1024 * (i + 1)], server)
                print('第' + str(i + 1) + '次发送文件数据')

    def succ_recv(self, filename, sourcename):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.scr1.configure(state=NORMAL)
        self.scr1.insert("end", "{} {}:\n".format(self.name, now_time), 'green')
        self.scr1.insert("end", f'你已成功接收 {filename}文件', 'shengzise')
        self.scr1.insert("end", f' |来源:{sourcename}\n', 'zise')
        self.scr1.see(END)
        self.scr1.config(state=DISABLED)

    def succ_send(self, recv_user, filename):

        self.scr1.configure(state=NORMAL)
        self.scr1.insert("end", f'{filename}', 'shengzise')
        self.scr1.insert("end", f' |已成功发送给{recv_user}\n', 'zise')
        self.scr1.see(END)
        self.scr1.config(state=DISABLED)
        print(f'{self.name}：{filename}--文件成功发送文件给', recv_user)

    def send(self, msg):

        if msg != '':
            message = {}
            message["chat_type"] = "normal"
            message["message_type"] = "text"
            message["send_user"] = self.name
            message["content"] = msg.strip()
            jsondata = json.dumps(message, ensure_ascii=False)
            sock.sendto(jsondata.encode('utf-8'), server)

    def private_send(self, msg):
        fpath, fname, extension, tempfilename = self.Get_File(msg)  # 判断是路径还是信息
        # print(extension)
        if self.fri_list.selection() == ():
            messagebox.showwarning(title='提示', message='你没有选择发送对象！')

        elif str(extension) in ('.py', '.doc', '.txt', '.docx'):  # 文件
            self.send_file('normal-file', tempfilename, msg)
            return 'normal-file', tempfilename

        elif str(extension) in ('.jpg', '.png'):
            self.send_file('image', tempfilename, msg)
            return 'image', tempfilename

        elif str(extension) in ('.avi', '.mp4'):
            self.send_file('video', tempfilename, msg)
            return 'video', tempfilename

        else:
            message = {}
            message["chat_type"] = "private"
            message["message_type"] = "text"
            message["send_user"] = self.name
            message["recv_user"] = self.fri_list.selection()[0]
            message["content"] = msg.strip()
            jsondata = json.dumps(message, ensure_ascii=False)
            sock.sendto(jsondata.encode('utf-8'), server)
            return 'text', ''

    def recv(self):
        message = {}
        message["message_type"] = "init_message"
        message["content"] = self.name
        json_str = json.dumps(message, ensure_ascii=False)
        sock.sendto(json_str.encode('utf-8'), server)
        while True:
            data = sock.recv(1024)
            source = data.decode('utf-8')
            json_data = json.loads(data.decode('utf-8'))
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.scr1.configure(state=NORMAL)
            if json_data['message_type'] == "init_message":
                self.scr1.insert("end", f'欢迎{json_data["content"]}加入聊天室' + '\n', 'red')
                print(json_data["online_user"])
                user_list = eval(json_data["online_user"])
                for user in user_list:
                    if str(user) not in self.fri_list.get_children() and str(user) != self.name:  # 如果不在列表中
                        self.fri_list.insert('', 2, str(user), text=str(user).center(24), values=("1"), tags='其他用户')
                print(json_data["content"] + '进入了聊天室...')

            elif json_data['message_type'] == "leave_message":
                self.scr1.insert("end", f'{json_data["content"]}离开了聊天室...' + '\n', 'red')
                if json_data["content"] in self.fri_list.get_children():
                    self.fri_list.delete(json_data["content"])
                print(json_data["content"] + '离开了聊天室...')

            elif json_data['chat_type'] == "normal":
                if json_data['message_type'] == "text":
                    self.scr1.insert("end", "{} {}:\n".format(json_data['send_user'], now_time), 'green')
                    self.scr1.insert("end", json_data['content'] + '\n')

                elif json_data['message_type'] == "stickers":
                    self.scr1.configure(state=NORMAL)
                    self.scr1.insert("end", "{} {}:\n".format(json_data['send_user'], now_time), 'green')
                    dics = self.obj_emoji.dics
                    if json_data['content'] in dics:
                        mes = json_data['content']
                        self.scr1.image_create(END, image=dics[mes])
                        self.scr1.insert("end", '\n', 'zise')
                        self.scr1.see(END)
                    self.scr1.config(state=DISABLED)
                    print(f'收到{json_data["send_user"]}发的表情包：', json_data['content'])

            elif json_data['chat_type'] == "private":
                if json_data['message_type'] == "text":
                    self.scr1.insert("end", "{} {}:\n".format(json_data['send_user'], now_time), 'green')
                    self.scr1.insert("end", json_data['content'])
                    self.scr1.insert("end", f'  |私聊消息\n', 'zise')
                    print(f'[私聊]收到{json_data["send_user"]}的消息：', json_data['content'])

                elif json_data['message_type'] == "stickers":

                    self.scr1.configure(state=NORMAL)
                    self.scr1.insert("end", "{} {}:\n".format(json_data['send_user'], now_time), 'green')
                    dics = self.obj_emoji.dics
                    if json_data['content'] in dics:
                        mes = json_data['content']
                        self.scr1.image_create(END, image=dics[mes])
                        self.scr1.insert("end", f'  |私聊消息\n', 'zise')
                        self.scr1.see(END)
                    self.scr1.config(state=DISABLED)
                    print(f'[私聊]收到{json_data["send_user"]}发的表情包：', json_data['content'])

                elif json_data['message_type'] == "ask-file":
                    fileType = json_data["file_type"]
                    self.scr1.configure(state=NORMAL)
                    self.scr1.insert("end", "{} {}:\n".format(json_data["send_user"], now_time), 'green')
                    self.scr1.insert("end", f'正在向你发送一个{fileType}文件...\n', 'shengzise')
                    self.scr1.see(END)
                    self.scr1.config(state=DISABLED)

                    flag = messagebox.askyesno(title='提示',
                                               message=f'{json_data["send_user"]}向你发送了一个{fileType}\n你是否要接收和保存？')
                    if flag:
                        json_data['message_type'] = "isRecv"
                        json_data['isRecv'] = "true"
                        jsondata = json.dumps(json_data, ensure_ascii=False)
                        sock.sendto(jsondata.encode('utf-8'), server)

                    else:
                        json_data['message_type'] = "isRecv"
                        json_data['isRecv'] = "false"
                        jsondata = json.dumps(json_data, ensure_ascii=False)
                        sock.sendto(jsondata.encode('utf-8'), server)
                        self.scr1.configure(state=NORMAL)
                        self.scr1.insert("end", "{} {}:\n".format(self.name, now_time), 'green')
                        self.scr1.insert("end", f'你已拒绝接收{fileType}', 'shengzise')
                        self.scr1.insert("end", f' |来源:{json_data["send_user"]}\n', 'zise')
                        self.scr1.see(END)
                        self.scr1.config(state=DISABLED)

                elif json_data['message_type'] == "isRecv":
                    if json_data['isRecv'] == "true":
                        if json_data["file_type"] == 'normal-file':
                            f = open(json_data["content"], 'rb')  # r方式读到str格式数据，rb方式读到bytes型。若是rb格式，下面sendto就不需要encode
                            data = f.read()
                            fhead = len(data)
                            print('文件大小:', fhead)

                            message = {}
                            message["chat_type"] = "private"
                            message["message_type"] = "file-data"
                            message["file_length"] = str(fhead)
                            message["file_name"] = json_data["file_name"]
                            message["send_user"] = json_data["send_user"]
                            message["recv_user"] = json_data["recv_user"]
                            message["content"] = ''
                            jsondata = json.dumps(message, ensure_ascii=False)
                            sock.sendto(jsondata.encode('utf-8'), server)

                            print('开始发送文件数据...')
                            self.cut_data(fhead, data)
                            print('文件数据已成功发送到服务器！')
                            f.close()
                    else:
                        self.scr1.insert("end", "{} {}:\n".format(json_data["send_user"], now_time), 'green')
                        self.scr1.insert("end", f"对方拒绝接收你发的{json_data['file_name']}文件\n", 'chengse')
                        self.scr1.see(END)

                elif json_data['message_type'] == "file-data":
                    print('正在接收文件')
                    filename = json_data['file_name']
                    data_size = int(json_data['file_length'])
                    print('文件大小为' + str(data_size))
                    recvd_size = 0
                    data_total = b''
                    j = 0
                    while not recvd_size == data_size:
                        j = j + 1
                        if data_size - recvd_size > 1024:
                            data, addr = sock.recvfrom(1024)
                            recvd_size += len(data)
                            print('第' + str(j) + '次收到文件数据')
                        else:  # 最后一片
                            data, addr = sock.recvfrom(1024)
                            recvd_size = data_size
                            print('第' + str(j) + '次收到文件数据')
                        data_total += data

                    f = open(filename, 'wb')  # 收到的数据是bytes型，可以直接用wb写入，不用Decode。若用的是w方式，要对接收数据decode后写入
                    f.write(data_total)
                    f.close()
                    print(filename, '文件接收完成！')
                    self.succ_recv(filename, json_data["send_user"])
                    message = {}
                    message["chat_type"] = "private"
                    message["message_type"] = "Recv_msg"
                    message["Recv_msg"] = "true"
                    message["file_length"] = json_data['file_length']
                    message["file_name"] = json_data["file_name"]
                    message["send_user"] = json_data["recv_user"]
                    message["recv_user"] = json_data["send_user"]
                    jsondata = json.dumps(message, ensure_ascii=False)
                    sock.sendto(jsondata.encode('utf-8'), server)

                elif json_data['message_type'] == "Recv_msg":
                    if json_data['Recv_msg'] == "true":
                        recv_user = json_data['recv_user']
                        filename = json_data['file_name']
                        self.succ_send(recv_user, filename)


class ChatUI():
    def __init__(self, root):
        self.root = root

    def JieShu(self):
        flag = messagebox.askokcancel(title='提示', message='你确定要退出聊天室吗？')
        # s.sendto(f":{name} 已退出聊天室...".encode('utf-8'),server)
        if flag:
            message = {}
            message["message_type"] = "leave_message"
            message["content"] = self.name
            jsondata = json.dumps(message, ensure_ascii=False)
            sock.sendto(jsondata.encode('utf-8'), server)
            sys.exit(0)

    def openfile(self):
        r = askopenfilename(title='打开文件', filetypes=[('All File', '*.*'), ('文本文件', '.txt'), ('python', '*.py *.pyw')])
        self.scr2.insert(INSERT, r)

    def chat(self, usename):
        self.name = usename
        self.root.title('聊天室--用户名:' + self.name)
        sw = self.root.winfo_screenwidth()  # 计算水平距离
        sh = self.root.winfo_screenheight()  # 计算垂直距离
        w = 1120  # 宽
        h = 720  # 高
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.root.geometry("%dx%d+%d+%d" % (w, h, (x + 160), y))
        self.root.iconbitmap(r'images/icon/chat.ico')  # 设置左上角窗口图标

        self.root.resizable(0, 0)  # 窗口设置为不可放大缩小
        # 告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # 获取屏幕的缩放因子
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # 设置程序缩放
        self.root.tk.call('tk', 'scaling', ScaleFactor / 75)

        self.root.resizable(1, 1)  # 窗口设置为不可放大缩小
        self.scr1 = scrolledtext.ScrolledText(self.root, height=18, font=('黑体', 13))
        self.scr1.tag_config('green', foreground='#008C00', font=('微软雅黑', 10))  # 设置组件字体颜色
        self.scr1.tag_config('red', foreground='red')
        self.scr1.tag_config('zise', foreground='#aaaaff')
        self.scr1.tag_config('shengzise', foreground='#9d4cff')
        self.scr1.tag_config('chengse', foreground='#ff7f27')

        # 创建树形列表
        self.fri_list = Treeview(self.root, height=30, show="tree")
        self.fri_list.insert('', 0, 'online_user', text='在线用户'.center(10, '-'), values=("1"), tags='在线用户')
        if self.name not in self.fri_list.get_children():  # 如果不在列表中
            self.fri_list.insert('', 1, 'me', text=self.name.center(24), values=("1"), tags='自己')  # 自己在列表中颜色为红色
        self.fri_list.grid(row=1, column=2, rowspan=7, sticky=N)
        self.fri_list.tag_configure('在线用户', foreground='#aa5500', font=('黑体', 13))  # 设置组件字体颜色
        self.fri_list.tag_configure('自己', foreground='red', font=('微软雅黑', 10))  # 设置组件字体颜色
        self.fri_list.tag_configure('其他用户', font=('微软雅黑', 10))  # 设置组件字体颜色

        self.scr1.grid(row=1, column=1)
        l0 = Label(self.root, text='')
        l0.grid(row=2)
        l1 = Label(self.root, text='下框输入你要的发送的内容：')
        l1.grid(row=3, column=1)
        self.scr2 = scrolledtext.ScrolledText(self.root, height=6, font=('黑体', 13))
        self.scr2.grid(row=4, column=1)
        l2 = Label(self.root, text='')
        l2.grid(row=5)
        tf = Frame(self.root)
        tf.grid(row=6, column=1)

        obj_emoji = Emoji(self.root, self.send_mark)
        chat = ChatClient(self.name, self.scr1, self.scr2, self.fri_list, obj_emoji)

        b0 = Button(tf, text=' 表情包 ', command=obj_emoji.express)
        b0.grid(row=1, column=0, padx=20)
        b1 = Button(tf, text=' 群发 ', command=chat.toSend)
        b1.grid(row=1, column=1, padx=20)
        b4 = Button(tf, text=' 私聊 ', command=chat.toPrivateSend)
        b4.grid(row=1, column=2, padx=20)
        b2 = Button(tf, text=' 传文件 ', command=self.openfile)
        b2.grid(row=1, column=3, padx=20, pady=20)
        b3 = Button(tf, text=' 发邮件 ', command='')
        b3.grid(row=1, column=4, padx=20)
        b4 = Button(tf, text=' 开启FTP ', command='')
        b4.grid(row=1, column=5, padx=20)
        b5 = Button(tf, text=' 登录FTP ', command='')
        b5.grid(row=1, column=6, padx=20)
        b6 = Button(tf, text=' 退出 ', command=self.JieShu)
        b6.grid(row=1, column=7, padx=20)

        tr = threading.Thread(target=chat.recv, args=(),
                              daemon=True)
        # daemon=True 表示创建的子线程守护主线程，主线程退出子线程直接销毁
        tr.start()
        self.root.protocol("WM_DELETE_WINDOW", self.JieShu)

    def send_mark(self, exp, dics):
        stick_code = exp
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.scr1.configure(state=NORMAL)
        self.scr1.insert("end", "{} {}:\n".format(self.name, now_time), 'green')
        message = {}
        message["message_type"] = "stickers"
        message["send_user"] = self.name
        message["content"] = stick_code

        if self.fri_list.selection() != () and self.fri_list.selection()[0] != 'me':
            message["chat_type"] = "private"
            message["recv_user"] = self.fri_list.selection()[0]
            jsondata = json.dumps(message, ensure_ascii=False)
            sock.sendto(jsondata.encode('utf-8'), server)
            self.scr1.image_create(END, image=dics[stick_code])
            self.scr1.insert("end", f'  |私聊{self.fri_list.selection()[0]}\n', 'zise')
            print(f'表情消息:{stick_code}发送成功！[私聊{self.fri_list.selection()[0]}]')
        else:
            message["chat_type"] = "normal"
            jsondata = json.dumps(message, ensure_ascii=False)
            sock.sendto(jsondata.encode('utf-8'), server)
            self.scr1.image_create(END, image=dics[stick_code])
            print(f'表情消息:{stick_code}发送成功！')
            self.scr1.insert(END, '\n')
        self.scr1.see(END)
        self.scr1.config(state=DISABLED)


if __name__ == '__main__':
    root = Tk()
    Main = ChatUI(root)
    Login(Register, Main.chat, root)
    root.mainloop()
