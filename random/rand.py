import head
import tkinter
import tkinter.messagebox
a = tkinter.Tk()
a.title("randing")

button = tkinter.Button(a, text="start", commend=head.helloCallBack())
button.pack()
lable = tkinter.Label(a, "the rand", "pink")
lable.pack()
a.mainloop()
