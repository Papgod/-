#导入tkinter库
import tkinter as tk
#导入os库
import os as o

#创建tkinter窗口
root = tk.Tk()
root.title('借阅图书主界面')   #设置窗口标题
root.geometry('880x720')      #设置窗口大小
root.resizable(0,0)           #设置窗口大小不可变

#创建提示标签
label_1 = tk.Label(root,text='卡号:')
label_1.place(x = 0,y = 695)
label_1.pack()

#创建插入文本框
entry1 = tk.Entry(root)
entry1.place(x = 20,y = 695)
entry1.pack()

#创建提示标签
label_1 = tk.Label(root,text='书名:')
label_1.place(x = 0,y = 705)
label_1.pack()
#创建插入文本框
entry2 = tk.Entry(root)
entry2.place(x = 20,y = 705)
entry2.pack()

#创建主循环
root.mainloop()