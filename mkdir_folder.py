#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a mkdir_folder'

__author__ = 'Moustache'

import time,os
from tkinter import *
import tkinter.messagebox as messagebox

#basename= str(input('please input your name:'))
#basename = ' '
#basePath = ' '
underline = '_'
chinese = 'chinese'
english = 'english'

#default
#if not basename.strip():
 #   basename= 'hlt'

#basePath = 'G:\\work\\' #folder path

#创建文件函数


class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        #名字输入提示
        self.nameTip = Label(self, text = "请输入你的名字：", fg = "red", bg = 'yellow').pack()

        # 名字输入
        self.name = StringVar()
        self.name.set("hlt")  # 设置默认用户名
        self.nameInput = Entry(self, textvariable=self.name).pack()

        #路径输入提示
        self.pathTip = Label(self, text="请输入你的路径：", fg="red", bg="yellow").pack()

        # 路径输入
        self.path = StringVar()
        self.path.set("G:\\work\\")  # 设置默认保存路径
        self.pathInput = Entry(self, textvariable=self.path).pack()

        #确认
        self.confirmButton = Button(self, text='确定', fg = "green", command= self.varGet, bg = "yellow").pack()
        
    #获取输入函数
    def varGet(self):
        name = self.name.get()
        basename = name

        path = self.path.get()
        basePath = path
        thisYear = str(time.localtime()[0])
        thisMonth = str(time.localtime()[1])
        thisDay = time.strftime("%Y%m%d", time.localtime())

        yearPath = basePath + thisYear
        # monthPath = basePath + thisYear + '\\' +thisMonth
        monthPath = yearPath + '\\' + thisMonth

        # dayPath = basePath + thisYear + '\\' +thisMonth + '\\' + basename+thisDay
        dayPath = monthPath + '\\' + basename + underline + thisDay + underline + chinese
        englishPath = monthPath + '\\' + basename + underline + thisDay + underline + english

        #try:
        if not os.path.exists(basePath):
            os.mkdir(basePath)
        if not os.path.exists(yearPath):
            os.mkdir(yearPath)
        if not os.path.exists(monthPath):
            os.mkdir(monthPath)
        if not os.path.exists(dayPath):
            os.mkdir(dayPath)
        if not os.path.exists(englishPath):
            os.mkdir(englishPath)

        #except Exception as e:
            #print('exception:', e)
            #print('Failed to create folder,Please enter the correct folder name!')
        #else:
            # messagebox.showinfo('Successfully' , "Successfully created the folder!!")
            # open the folder
        os.popen("explorer.exe" + " " + dayPath)
        os.popen("exit")

        #print('END')





    #def mkdir_folder(self):


        #self.okLabel = Label(self, text="Successfully ", fg="green")
        #self.okLabel.pack()

    def Successfully(self):
        self.okButton = Button(self, text = "Successfully ", fg = "green")
        self.okButton.pack(side = "bottom")

def main():
    
    #实例化对象
    app = Application()
    #设置窗口标题
    app.master.title('Mkdir_folder')
    #主消息循环
    app.mainloop()

    
    

if __name__ == '__main__':
    main()
