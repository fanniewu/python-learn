import  tkinter
from tkinter import Tk, Label, Button, Entry

#创建主窗口
win = Tk()
win.title("学习")
win.geometry("500x500+300+100")

#进入消息循环

# Label
# anchor: 位置: N, NE, E, SE, S, SW, W, NW, CENTER
label = Label(win, text="I am learning tkinter!", bg="yellow", font=("宋体", 15), anchor=tkinter.W, width=30, height=1)
label.pack()



# Entry
# textvariable: 绑定文本变量
info = tkinter.Variable()
entry = Entry(win, textvariable=info)
entry.pack()

def func1():
    inputtext = info.get()
    #inputtext = entry.get()
    # entry.set()不能使用
    print(inputtext)
    info.set("info.set()")
# Button
button1 = Button(win, text="OK", width=10, height=1, command=func1)
button1.pack()



#程序运行起来
win.mainloop()
