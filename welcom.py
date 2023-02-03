import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import configparser
import os

confpath = str(os.getcwd() + '\sur_Cod.ini')
conf = configparser.ConfigParser()
conf.read(confpath, encoding="utf-8")
items = conf.items('usrcod')
print(confpath)
def btonc():
    anserchek1 = anser1.get()
    anserchek2 = anser2.get()
    anserchek3 = anser3.get()
    anserchek = (anserchek1+'-'+anserchek2 + '-'+anserchek3)
    for i in items:
        if str(i[1]) == str(anserchek):
            print('ok')
            #os.system('')
            break
        else:
            tkinter.messagebox.showerror(title='error', message='你的登录码错误！')

win = tkinter.Tk()#创建窗体

win.geometry("500x300")#窗口大小
win.title("AKDW V0.0.1")#窗口命名
win.resizable(width=False,height=False)#窗口变形
img_open = Image.open('./data/UI/BACKGROUND/loginbak.png')

#背景
img_png = ImageTk.PhotoImage(img_open)
label_img = tkinter.Label(win, image=img_png)
label_img.pack()

#文字和按钮
anser1 = tkinter.Entry(win, bg="grey", width=10)
anser1.place(x=123, y=120)
anser2 = tkinter.Entry(win, bg="grey", width=10)
anser2.place(x=223, y=120)
anser3 = tkinter.Entry(win, bg="grey", width=10)
anser3.place(x=323, y=120)
bton = tkinter.PhotoImage(file = './data/UI/YESNO/bulebutton.png')
tkinter.Button(win, text="登记", font=20, command=btonc, bd=0, image=bton, compound = "center", foreground='white').place(x=205, y=180)

win.mainloop()#进入消息循环