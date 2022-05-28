#导入tkinter库
import tkinter as tk
from tkinter import END, ttk

#创建存储字典(空)
dic = {
        'python王者归来':'0000001','安徒生童话':'0000002',
        'HTML+CSS3王者归来':'0000003','世界之最':'0000004',
        '数学之美':'0000005','三体':'0000006'
       }

#创建tk窗口
root = tk.Tk()
root.title('所有图书')
root.resizable(0,0)
root.geometry('1000x500')
root.iconbitmap('SIGNL.ico')

#创建树图
tree = ttk.Treeview(root,columns=('books'))
tree.pack()
# 定义列
tree["columns"] = ('书名','书号')
#定义表头
tree.heading('#0',text='书号')
tree.heading('#1',text='书名')

#创建提示标签
label_1 = tk.Label(root,text='书号:')
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

#创建插入函数
def insert():
    #获取文本框类容
    a = entry1.get()
    b = entry2.get()
    #创建插入方法
    tree.insert('',index = END,text=a,values=b)
    #将插入的类容传入到字典中
    dic[a] = b  

'''#将字典类容传入到treeview里'''
for key in dic.keys():
    tree.insert('',index = END,text=dic[key],values=key)

#创建插入按钮
button_1 = ttk.Button(root,text='插入',command=insert)
button_1.place(x=0,y=750)
button_1.pack()

#创建主循环
root.mainloop()