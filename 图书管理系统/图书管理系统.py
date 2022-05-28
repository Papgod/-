#导入tkinter库
import tkinter as tk
#导入json库
import json
#导入os库
import os

#创建方法
#创建所有图书方法
def everyBook():
    os.system('python 所有图书.py')
    
def jiehuan():
    os.system('python 借还图书主页.py')
    

#创建tk窗口
window = tk.Tk()    #创建母窗口
window.title('图书查询系统')    #窗口标题
window.resizable(0,0)    #设置窗口大小不可改变
window.geometry('1099x600')
window.iconbitmap("SIGNL.ico")

#创建软件介绍
label_bg = tk.Label( window,width=1099,height=1,text='欢迎使用本图书管理系统，提供进图书、查询图书、图书借阅等功能',bg='red')
label_bg.pack()

#创建跳转按钮
button_1 = tk.Button(window,text='所有图书',command=everyBook)
button_1.pack()

#创建跳转按钮
button_2 = tk.Button(window,text='借换图书',command = jiehuan)
button_2.pack()

#创建主循环
window.mainloop()