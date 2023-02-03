import tkinter
from PIL import ImageTk, Image
import tkinter.messagebox
from json import load
import os

class memoc():
    def __init__(self):
        self.path = os.getcwd()
        with open('D:\AKDWPythonCMD\settings.json', encoding='utf-8') as f:
            text = load(f)
            self.background = text['settings'][4]['memobackground']

    def adb(self):
        global a, b
        a = todo.get()
        b = more.get()
        c = a + '    ' + b
        for i in butonnamelist:
            if butonlist[i]["text"] == '':
                butonlist[i]["text"] = c
                todo.delete(0, "end")
                more.delete(0, "end")
                break

    def addw(self):
        add = tkinter.Toplevel()
        add.geometry("300x200")
        add.title("Add")
        add.resizable(width=False, height=False)
        tkinter.Label(add, text="需要做的事：").place(x=10, y=45)
        global todo
        todo = tkinter.Entry(add, width=40)
        todo.place(x=10, y=70)
        tkinter.Label(add, text="备注(时间等)：").place(x=10, y=90)
        global more
        more = tkinter.Entry(add, width=40)
        more.place(x=10, y=110)
        tkinter.Button(add, text='添加', command=self.adb).place(x=145, y=140)
        tkinter.Button(add, text='取消', command=add.destroy).place(x=95, y=140)
        add.mainloop()

    def white(self,button):
        if button in butonlist.keys():
            butonlist[button]["text"] = ''

    def memomain(self):
        global butonlist, a1b, a2b, a3b, a4b, a5b, a6b, a7b, a8b, a9b, a10b, a11b, a12b, butonnamelist
        memo = tkinter.Tk()
        memo.geometry("290x400")
        memo.title("AKDW TODO")
        memo.resizable(width=False, height=False)
        memo.attributes("-alpha", 0.85)
        img = Image.open('./memo/' + self.background + '.png')
        photo = ImageTk.PhotoImage(img)
        back = tkinter.Label(memo, image=photo)
        back.place(x=-2, y=0)
        bimgb = 1
        if self.background == "Red":
            addb = "./memo/add3.png"
            bimg = Image.open(addb)
            bimgb = ImageTk.PhotoImage(bimg)
        if self.background == "Kalsits":
            addb = "./memo/add2.png"
            bimg = Image.open(addb)
            bimgb = ImageTk.PhotoImage(bimg)
        if self.background == "Amiya":
            addb = "./memo/add1.png"
            bimg = Image.open(addb)
            bimgb = ImageTk.PhotoImage(bimg)
        addbton = tkinter.Button(memo, image=bimgb, bd=0, command=self.addw)
        addbton.place(x=0, y=2, width=32, height=32)
        y = 40
        butonnamelist = ['a1b', 'a2b', 'a3b', 'a4b', 'a5b', 'a6b', 'a7b', 'a8b', 'a9b', 'a10b', 'a11b', 'a12b']
        butonlist = {}
        for i in butonnamelist:
            name = str(i)
            i = tkinter.Button(memo, command=lambda button=i: self.white(button), bd=0)
            i.place(x=3, y=y)
            y += 30
            v = {name: i}
            butonlist.update(v)
        memo.mainloop()