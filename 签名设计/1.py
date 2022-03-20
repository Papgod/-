#导入tkinter库
import tkinter as tk
from tkinter import ttk

#创建tk子窗口
window=tk.Tk()
#tk窗口子标题
window.title('签名展示')
#子窗口大小
window.geometry('300x450')

#创建tk窗口
root = tk.Tk()
#设置标题
root.title('签名生成')
#设置床口大小不可变
root.resizable(0,0)
#设置窗口大小
root.geometry('650x500')

#读取cbox
def showMsg(*args):
    print(cbox.get())
    name = entry.get()
    if cbox.get() == '个性签':
            a = tk.Label(window,text = name,font = '隶书').pack()
    elif cbox.get() == '连笔签':
            b = tk.Label(window,text = name,font = '腾祥伯当草书').pack()
    elif cbox.get() == '潇洒签':
            c = tk.Label(window,text = name,font = '方正舒体').pack()
       


#创建文本框对象
entry = tk.Entry(root)
entry.place(x = 0,y = 40)     

#创建cbox对象
cbox = ttk.Combobox(root,width=26)
cbox['values'] = ['请选择签名样式','个性签','连笔签','潇洒签']
cbox.place(x=0,y=99)
#设置默认列表项
cbox.current(0)
#设置下拉列表的只读模式
cbox['state'] = 'readonly'
cbox.bind('<<ComboboxSelected>>',showMsg)

#创建提示标签
py = '欢迎使用签名设计系统，请先输入您的名字然后在选择所需的风格，您的签名将放置在窗口最上面,并且只支持汉字和英文'
a = tk.Label(root,text = py,bg = 'red',fg = 'black').pack()

#创建窗口主循环
root.mainloop()
window.mainloop()
