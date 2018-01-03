#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a mkdir_folder'
# version ：1.0.1

__author__ = 'Moustache'

import time,os, sys
from tkinter import *
import tkinter.messagebox as messagebox

underline = '_'
chinese = 'chinese'
english = 'english'

#类
class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        #名字输入提示
        self.nameTip = Label(self, text = "请输入你的名字：", fg = "red", bg = 'yellow', font = ('Arial, 12')).pack()

        # 名字输入
        self.name = StringVar() #定义变量
        self.name.set("hlt")  # 设置默认用户名
        self.nameInput = Entry(self, textvariable=self.name).pack()

        #路径输入提示
        self.pathTip = Label(self, text="请输入你的路径：", fg="red", bg="yellow", font = ('Arial, 12')).pack()

        # 路径输入
        self.path = StringVar()
        self.path.set("G:\\work\\")  # 设置默认保存路径
        self.pathInput = Entry(self, textvariable=self.path).pack()

        #确认
        self.confirmButton = Button(self, text='确定', fg = "green", command= self.mkdirFloder, bg = "yellow", font = ('Arial, 12')).pack()
        
    #创建文件夹
    def mkdirFloder(self):
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

        try:
        # 创建文件函数
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
        except Exception as e:
            print('exception:', e)
            print('Failed to create folder,Please enter the correct folder name!')
        else:
             messagebox.showinfo('Successfully' , "Successfully created the folder!!")

        #open the folder
        os.popen("explorer.exe" + " " + monthPath)
        os.popen("exit")

def main():
    #实例化对象
    app = Application()
    #设置窗口标题
    app.master.title('Mkdir_folder')
    #设置主窗口大小
    app.master.geometry("400x120")
    #主消息循环
    app.mainloop()

if __name__ == '__main__':
    main()
