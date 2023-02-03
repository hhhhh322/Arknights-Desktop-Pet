import sys
import _thread
import time
import tkinter
import pystray
from pystray import Icon as icon, Menu as menu, MenuItem as item
from threading import Thread
from PIL import Image,ImageDraw
from subprocess import Popen
from shutil import move
import os
from tkinter import filedialog
from memo import memoc
def cpu():
    global d, x
    if d % 2 != 0:
        a = os.getcwd()
        b = os.path.abspath(os.path.join(a, os.pardir))
        b1 = os.path.abspath(os.path.join(b, os.pardir))
        c = a + '\data\CPUs\TrafficMonitor.exe'
        Popen(c)
        d += 1
    elif d % 2 == 0:
        os.system('taskkill /f /t /im ' + 'TrafficMonitor.exe')

def FileClean():
    pictrue = '图片'
    video = '视频'
    pys = 'py文件'
    compress = '压缩包zips'
    sound = '音频'
    mirror = '镜像'
    path = None
    wi = tkinter.Tk()
    wi.geometry('500x150')
    wi.title('文件整理')
    text = tkinter.Label(wi, text='使用方法：在输入框中输入要整理的文件夹路径或通过预览查找，不指定则视为整理桌面。')
    text.place(x=10, y=0)
    inp = tkinter.Entry(wi, width=50)
    inp.place(x='25', y='40')

    def seebutton():
        inp.select_clear()
        pathh = filedialog.askdirectory()
        inp.insert(0, pathh)

    def okbuton():
        path = inp.get()
        for file in os.listdir(path):
            # 分割文件的后缀名
            ext = os.path.splitext(file)[1]
            ext = ext[1:]

            # 判断是否存在该目录
            if ext != 'lnk':
                if not os.path.isdir(f"{path}/{ext}"):
                    os.mkdir(f"{path}/{ext}")
                # 将文件放到对应目录下
                source_path = f"{path}/{file}"
                target_path = f"{path}/{ext}/{file}"
                move(source_path, target_path)
            else:
                pass

    see = tkinter.Button(wi, width=10, command=seebutton)
    see.place(x='380', y='40')
    ok = tkinter.Button(wi, width=10, command=okbuton)
    ok.pack()
    wi.mainloop()

def memos():
    memo = memoc()
    memo.memomain()

def stray(Functions):
    def defstray(names,functions):
        list = []
        img = Image.open('image.png')
        if len(names) == len(functions):
            for i in range(len(names)):
                x=item(names[i], functions[i])
                list.append(x)
        menu=tuple(list)
        icon = pystray.Icon("name", img, "AKDW", menu)
        icon.run()
    try:
        _thread.start_new_thread(defstray, (Functions[0],Functions[1]))
    except:
        print('stray error')
def exit2():
        os.system('taskkill /f /t /im ' + 'TrafficMonitor.exe')
        os.system('taskkill /f /t /im ' + 'python.exe')





