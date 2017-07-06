#mkdir_folder for every day 

import time,os

basename= str(input('please input your name:'))

#default
if not basename.strip():
    basename= 'hlt'

basePath = 'G:\\work\\'

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
        
    os.popen("explorer.exe" + " " + dayPath)
    os.popen("exit")
        
def main():
    mkdir_folder()


if __name__ == '__main__':
    main()
