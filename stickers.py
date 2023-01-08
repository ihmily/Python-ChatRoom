from tkinter import *
from PIL import ImageTk  # 导入处理图像模块
from need_module import os


class Emoji(object):
    def __init__(self,root,send_mark):
        self.root=root
        self.emoji_img()
        self.send_mark=send_mark
        self.ee = 0
        # 用字典将标记与表情图片一一对应, 用于后面接收标记判断表情贴图
        self.dics = {'[aa**]': self.p1, '[bb**]': self.p2, '[cc**]': self.p3, '[dd**]': self.p4, '[ee**]': self.p5,
                     '[ff**]': self.p6,'[gg**]': self.p7, '[hh**]': self.p8,'[ii**]': self.p9, '[jj**]': self.p10,
                     '[kk**]': self.p11,'[ll**]': self.p12,'[mm**]': self.p13,'[nn**]': self.p14,'[oo**]': self.p15,
                     '[pp**]': self.p16,'[qq**]': self.p17,'[rr**]': self.p18,'[ss**]': self.p19,'[tt**]': self.p20,
                     '[uu**]': self.p21,'[vv**]': self.p22,'[ww**]': self.p23,'[xx**]': self.p24
                     ,'[yy**]': self.p25,'[zz**]': self.p26,'[aaa**]': self.p27,'[bbb**]': self.p28}



    def emoji_img(self):

        emoji_path = 'images/emoji/'
        filelist = os.listdir(emoji_path)  # 该方法列出path路径下的文件和文件夹列表
        # print(filelist)

        self.p1 = ImageTk.PhotoImage(file=emoji_path + filelist[0])
        self.p2 = ImageTk.PhotoImage(file=emoji_path + filelist[1])
        self.p3 = ImageTk.PhotoImage(file=emoji_path + filelist[2])
        self.p4 = ImageTk.PhotoImage(file=emoji_path + filelist[3])
        self.p5 = ImageTk.PhotoImage(file=emoji_path + filelist[4])
        self.p6 = ImageTk.PhotoImage(file=emoji_path + filelist[5])
        self.p7 = ImageTk.PhotoImage(file=emoji_path + filelist[6])
        self.p8 = ImageTk.PhotoImage(file=emoji_path + filelist[7])
        self.p9 = ImageTk.PhotoImage(file=emoji_path + filelist[8])
        self.p10 = ImageTk.PhotoImage(file=emoji_path + filelist[9])
        self.p11 = ImageTk.PhotoImage(file=emoji_path + filelist[10])
        self.p12 = ImageTk.PhotoImage(file=emoji_path + filelist[11])
        self.p13 = ImageTk.PhotoImage(file=emoji_path + filelist[12])
        self.p14 = ImageTk.PhotoImage(file=emoji_path + filelist[13])
        self.p15 = ImageTk.PhotoImage(file=emoji_path + filelist[14])
        self.p16 = ImageTk.PhotoImage(file=emoji_path + filelist[15])
        self.p17 = ImageTk.PhotoImage(file=emoji_path + filelist[16])
        self.p18 = ImageTk.PhotoImage(file=emoji_path + filelist[17])
        self.p19 = ImageTk.PhotoImage(file=emoji_path + filelist[18])
        self.p20 = ImageTk.PhotoImage(file=emoji_path + filelist[19])
        self.p21 = ImageTk.PhotoImage(file=emoji_path + filelist[20])
        self.p22 = ImageTk.PhotoImage(file=emoji_path + filelist[21])
        self.p23 = ImageTk.PhotoImage(file=emoji_path + filelist[22])
        self.p24 = ImageTk.PhotoImage(file=emoji_path + filelist[23])
        self.p25 = ImageTk.PhotoImage(file=emoji_path + filelist[24])
        self.p26 = ImageTk.PhotoImage(file=emoji_path + filelist[25])
        self.p27 = ImageTk.PhotoImage(file=emoji_path + filelist[26])
        self.p28 = ImageTk.PhotoImage(file=emoji_path + filelist[27])


    def express(self):
        # 如果ee标记为0，则弹出表情包，否则销毁表情包
        if self.ee == 0:
            self.ee = 1  # 把标记置为1，用于下次点击按钮时销毁表情
            # 设置表情图按钮及相应的事件处理实例方法
            self.b1 = Button(self.root, command=self.bb1, image=self.p1, relief=FLAT, bd=0)
            self.b2 = Button(self.root, command=self.bb2, image=self.p2, relief=FLAT, bd=0)
            self.b3 = Button(self.root, command=self.bb3, image=self.p3, relief=FLAT, bd=0)
            self.b4 = Button(self.root, command=self.bb4, image=self.p4, relief=FLAT, bd=0)
            self.b5 = Button(self.root, command=self.bb5, image=self.p5, relief=FLAT, bd=0)
            self.b6 = Button(self.root, command=self.bb6, image=self.p6, relief=FLAT, bd=0)
            self.b7 = Button(self.root, command=self.bb7, image=self.p7, relief=FLAT, bd=0)
            self.b8 = Button(self.root, command=self.bb8, image=self.p8, relief=FLAT, bd=0)
            self.b9 = Button(self.root, command=self.bb9, image=self.p9, relief=FLAT, bd=0)
            self.b10 = Button(self.root, command=self.bb10, image=self.p10, relief=FLAT, bd=0)
            self.b11 = Button(self.root, command=self.bb11, image=self.p11, relief=FLAT, bd=0)
            self.b12 = Button(self.root, command=self.bb12, image=self.p12, relief=FLAT, bd=0)
            self.b13 = Button(self.root, command=self.bb13, image=self.p13, relief=FLAT, bd=0)
            self.b14 = Button(self.root, command=self.bb14, image=self.p14, relief=FLAT, bd=0)
            self.b15 = Button(self.root, command=self.bb15, image=self.p15, relief=FLAT, bd=0)
            self.b16 = Button(self.root, command=self.bb16, image=self.p16, relief=FLAT, bd=0)
            self.b17 = Button(self.root, command=self.bb17, image=self.p17, relief=FLAT, bd=0)
            self.b18 = Button(self.root, command=self.bb18, image=self.p18, relief=FLAT, bd=0)
            self.b19 = Button(self.root, command=self.bb19, image=self.p19, relief=FLAT, bd=0)
            self.b20 = Button(self.root, command=self.bb20, image=self.p20, relief=FLAT, bd=0)
            self.b21 = Button(self.root, command=self.bb21, image=self.p21, relief=FLAT, bd=0)
            self.b22 = Button(self.root, command=self.bb22, image=self.p22, relief=FLAT, bd=0)
            self.b23 = Button(self.root, command=self.bb23, image=self.p23, relief=FLAT, bd=0)
            self.b24 = Button(self.root, command=self.bb24, image=self.p24, relief=FLAT, bd=0)
            self.b25 = Button(self.root, command=self.bb25, image=self.p25, relief=FLAT, bd=0)
            self.b26 = Button(self.root, command=self.bb26, image=self.p26, relief=FLAT, bd=0)
            self.b27 = Button(self.root, command=self.bb27, image=self.p27, relief=FLAT, bd=0)
            self.b28 = Button(self.root, command=self.bb28, image=self.p28, relief=FLAT, bd=0)
            # 设置表情包的位置
            self.b1.place(x=40, y=366)
            self.b2.place(x=76, y=366)
            self.b3.place(x=112, y=366)
            self.b4.place(x=148, y=366)
            self.b5.place(x=184, y=366)
            self.b6.place(x=220, y=366)
            self.b7.place(x=256, y=366)
            self.b8.place(x=40, y=330)
            self.b9.place(x=76, y=330)
            self.b10.place(x=112, y=330)
            self.b11.place(x=148, y=330)
            self.b12.place(x=184, y=330)
            self.b13.place(x=220, y=330)
            self.b14.place(x=256, y=330)
            self.b15.place(x=40, y=294)
            self.b16.place(x=76, y=294)
            self.b17.place(x=112, y=294)
            self.b18.place(x=148, y=294)
            self.b19.place(x=184, y=294)
            self.b20.place(x=220, y=294)
            self.b21.place(x=256, y=294)
            self.b22.place(x=40, y=258)
            self.b23.place(x=76, y=258)
            self.b24.place(x=112, y=258)
            self.b25.place(x=148, y=258)
            self.b26.place(x=184, y=258)
            self.b27.place(x=220, y=258)
            self.b28.place(x=256, y=258)
        else:
            # 标记ee为0则销毁所有表情按钮
            self.ee = 0
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b5.destroy()
            self.b6.destroy()
            self.b7.destroy()
            self.b8.destroy()
            self.b9.destroy()
            self.b10.destroy()
            self.b11.destroy()
            self.b12.destroy()
            self.b13.destroy()
            self.b14.destroy()
            self.b15.destroy()
            self.b16.destroy()
            self.b17.destroy()
            self.b18.destroy()
            self.b19.destroy()
            self.b20.destroy()
            self.b21.destroy()
            self.b22.destroy()
            self.b23.destroy()
            self.b24.destroy()
            self.b25.destroy()
            self.b26.destroy()
            self.b27.destroy()
            self.b28.destroy()

    # 所有表情按钮处理实例方法
    def bb1(self):
        self.mark('[aa**]')  # 调用实例方法，把参数传过去

    def bb2(self):
        self.mark('[bb**]')

    def bb3(self):
        self.mark('[cc**]')

    def bb4(self):
        self.mark('[dd**]')

    def bb5(self):
        self.mark('[ee**]')

    def bb6(self):
        self.mark('[ff**]')

    def bb7(self):
        self.mark('[gg**]')

    def bb8(self):
        self.mark('[hh**]')

    def bb9(self):
        self.mark('[ii**]')

    def bb10(self):
        self.mark('[jj**]')

    def bb11(self):
        self.mark('[kk**]')

    def bb12(self):
        self.mark('[ll**]')

    def bb13(self):
        self.mark('[mm**]')

    def bb14(self):
        self.mark('[nn**]')

    def bb15(self):
        self.mark('[oo**]')

    def bb16(self):
        self.mark('[pp**]')

    def bb17(self):
        self.mark('[qq**]')

    def bb18(self):
        self.mark('[rr**]')

    def bb19(self):
        self.mark('[ss**]')

    def bb20(self):
        self.mark('[tt**]')

    def bb21(self):
        self.mark('[uu**]')

    def bb22(self):
        self.mark('[vv**]')

    def bb23(self):
        self.mark('[ww**]')

    def bb24(self):
        self.mark('[xx**]')

    def bb25(self):
        self.mark('[yy**]')

    def bb26(self):
        self.mark('[zz**]')

    def bb27(self):
        self.mark('[aaa**]')

    def bb28(self):
        self.mark('[bbb**]')

    # 处理发送表情的实例方法
    def mark(self, exp):  # 参数是发的表情图标记, 发送后将按钮销毁
        self.send_mark(exp,self.dics)  # 函数回调把标记作为参数
        # 发送完摧毁所有表情包
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()
        self.b5.destroy()
        self.b6.destroy()
        self.b7.destroy()
        self.b8.destroy()
        self.b9.destroy()
        self.b10.destroy()
        self.b11.destroy()
        self.b12.destroy()
        self.b13.destroy()
        self.b14.destroy()
        self.b15.destroy()
        self.b16.destroy()
        self.b17.destroy()
        self.b18.destroy()
        self.b19.destroy()
        self.b20.destroy()
        self.b21.destroy()
        self.b22.destroy()
        self.b23.destroy()
        self.b24.destroy()
        self.b25.destroy()
        self.b26.destroy()
        self.b27.destroy()
        self.b28.destroy()
        self.ee = 0  # 把标记置为0