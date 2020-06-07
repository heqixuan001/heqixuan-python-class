import tkinter
import random
import time
a = tkinter.Tk()
a.title("抽奖助手")
a.geometry('600x300')

def hello():
    for i in range(1,4):
        rd = random.randint(1,12)
        b = tkinter.Tk()
        b.title("wyk is fucking")
        b.geometry('400x100')
        tkinter.Label(b,text = "wyk is fucking",bg = 'yellow').pack()
        if(rd%3 == 1):
            tkinter.Label(b,text = "余阳傻逼",bg='red').pack()
        elif(rd%3 == 2):
            tkinter.Label(b,text = "ppf傻逼",bg='red').pack()
        elif (rd%3 == 0):
            tkinter.Label(b,text = "xzy傻逼",bg='red').pack()
        time.sleep(1)
tkinter.Label(a,text = "hey").pack()
tkinter.Button(a,text = "look me",command = hello).pack()
a.mainloop()
