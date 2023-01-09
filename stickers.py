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
        self.dics = {}
        self.bb_list=[]

        self.stickers_code=['[aa**]','[bb**]','[cc**]','[dd**]','[ee**]','[ff**]','[gg**]','[hh**]','[ii**]','[jj**]','[kk**]','[ll**]',
                       '[mm**]','[nn**]','[oo**]','[pp**]','[qq**]','[rr**]','[ss**]','[tt**]','[uu**]','[vv**]',
                       '[ww**]','[xx**]','[yy**]','[zz**]','[aaa**]','[bbb**]']
        print(len(self.stickers_code))
        for index,code in enumerate(self.stickers_code):
            self.dics[code]=self.pic_list[index]
            self.bb_list.append(f"self.bb{index+1}")
        print(self.bb_list)
        print(len(self.bb_list))
    def emoji_img(self):

        emoji_path = 'images/emoji/'
        filelist = os.listdir(emoji_path)  # 该方法列出path路径下的文件和文件夹列表
        # print(filelist)
        self.pic_list=[]
        for i in range(0,28):
            self.pic_list.append(ImageTk.PhotoImage(file=emoji_path + filelist[i]))


    def express(self):
        # 如果ee标记为0，则弹出表情包，否则销毁表情包
        if self.ee == 0:
            self.ee = 1  # 把标记置为1，用于下次点击按钮时销毁表情
            # 设置表情图按钮及相应的事件处理实例方法
            self.buttom_list=[]
            x = 40
            y = 366
            for i in range(0,28):
                self.buttom_list.append(Button(self.root, command=eval(self.bb_list[i]), image=self.pic_list[i], relief=FLAT, bd=0))
                self.buttom_list[i].place(x=x, y=y)
                print(f"self.b1.place(x={x}, y={y})")
                if (i+1)%7==0 and i!=0:
                    y -= 36
                    x = 40
                else:
                    x += 36

        else:
            # 标记ee为0则销毁所有表情按钮
            self.ee = 0
            for i in range(0,28):
                self.buttom_list[i].destroy()

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
        # # 发送完摧毁所有表情包
        # for i in range(0, 28):
        #     self.buttom_list[i].destroy()
        # self.ee = 0  # 把标记置为0