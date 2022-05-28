#导入tkinter库
import tkinter as tk
#导入os库
import os as o

#创建tkinter窗口
root = tk.Tk()
root.title('借阅图书主界面')   #设置窗口标题
root.geometry('290x200')      #设置窗口大小
root.resizable(0,0)           #设置窗口大小不可变

'''#创建跳转方法
#创建跳转到借阅图书界面方法
def jieyue():
    o.system('python 借阅图书')
#创建跳转到归还图书界面方法
def guihuan():
    o.system('python 归还图书')
'''
    
#创建跳转按钮
#创建跳转到借阅图书界面
button_1 = tk.Button(root,text='借阅图书')
button_1.pack()
button_1.place(x = 90,y = 0)

#创建跳转到归还图书界面
button_2 = tk.Button(root,text='归还图书')
button_2.place(x = 150,y = 0)

#创建主循环
root.mainloop()