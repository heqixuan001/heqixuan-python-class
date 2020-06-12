import pyautogui as gui
import tkinter as tk

a = tk.Tk()
a.geometry('400x400')


def enter():
    gui.hotkey('enter')


def writer(a):
    gui.typewrite(message="!")


def hello():
    gui.hotkey('ctrl', 'alt', 'z')
    for i in range(1000):
        writer("!")
        enter()


tk.Label(a, text="把发送改为enter", bg='green').pack()
tk.Label(a, text="请打开qq联系人", bg='yellow').pack()
tk.Button(a, text="点我发送1000条信息", command=hello, bg='red').pack()


a.mainloop()
