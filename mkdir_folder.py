#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a mkdir_folder'

__author__ = 'Moustache'

import time,os

basename= str(input('please input your name:'))

#default
if not basename.strip():
    basename= 'hlt'

basePath = 'G:\\work\\' #folder path
   
thisYear = str(time.localtime()[0])
thisMonth = str(time.localtime()[1])
thisDay = time.strftime("%Y%m%d", time.localtime())

yearPath = basePath + thisYear
#monthPath = basePath + thisYear + '\\' +thisMonth
monthPath = yearPath + '\\' + thisMonth

#dayPath = basePath + thisYear + '\\' +thisMonth + '\\' + basename+thisDay
dayPath = monthPath + '\\' + basename+thisDay

def mkdir_folder():
    if not os.path.exists(yearPath):    
        os.mkdir(yearPath)
    if not os.path.exists(monthPath):
        os.mkdir(monthPath)
    if not os.path.exists(dayPath):
        os.mkdir(dayPath)
        
    #open the folder   
    os.popen("explorer.exe" + " " + dayPath)
    os.popen("exit")
        
def main():    
    try:       
        mkdir_folder()
    except Exception as e:
        print('exception:', e)
        print('Failed to create folder,Please enter the correct folder name!')
    else:
        print('Successfully created the folder!!')
    print('END')
    

if __name__ == '__main__':
    main()
