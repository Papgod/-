#导入tkinter库
import tkinter as tk
from tkinter import messagebox
#导入os库
import os as o

#创建tkinter窗口
root = tk.Tk()
root.title('借阅图书主界面')   #设置窗口标题
root.geometry('100x100')      #设置窗口大小
root.resizable(0,0)           #设置窗口大小不可变

def jk():
    messagebox.showinfo(title='借阅成功',message='已归还')



#创建借阅按钮
button_2 = tk.Button(root,text='归还',command = jk)
button_2.place(x = 0,y = 0)

#创建主循环
root.mainloop()