import re
import tkinter
def SoapSystem(screen, text: str = '', txtsize: int = 8, autoset: int = 9):
    screen.update()
    h = screen.winfo_height()
    t_y = int(h) / 3
    ott_y = t_y - 8
    ant_y = int(h) / 4 - 8
    print(len(text))
    if len(text) < 26:
        tkinter.Label(screen, text=text, fg='white', bg='black', font=("黑体", txtsize)).place(x=4, y=t_y)
    elif txtsize>=8 and len(text)==26:
        print(len(text))
        txt = re.findall(r'.{17}', text)
        ottext = text.replace(txt[0], '')
        tkinter.Label(screen, text=txt[0], fg='white', bg='black', font=("黑体", txtsize)).place(x=4, y=ott_y)
        tkinter.Label(screen, text=ottext, fg='white', bg='black', font=("黑体", txtsize)).place(x=4, y=ott_y + 15)
    else:
        if len(text) > 78:
            raise ValueError('字数过多，不超过68字too much word,less than 68')
        else:
            txt = re.findall(r'.{26}', text)
            ottext = text.replace(txt[0], '')
            if len(ottext) > 26:
                if txtsize >= 10:
                    txtsize = autoset
                    antxt = re.findall(r'.{26}', ottext)
                    antext = ottext.replace(antxt[0], '')
                    screen.geometry("330x70")
                    tkinter.Label(screen, text=txt[0], fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ant_y)
                    tkinter.Label(screen, text=antxt[0], fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ant_y + 15)
                    tkinter.Label(screen, text=antext, fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ant_y + 30)
                if 0 < txtsize < 10:
                    antxt = re.findall(r'.{26}', ottext)
                    antext = ottext.replace(antxt[0], '')
                    screen.geometry("330x70")
                    tkinter.Label(screen, text=txt[0], fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ant_y)
                    tkinter.Label(screen, text=antxt[0], fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ant_y + 15)
                    tkinter.Label(screen, text=antext, fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ant_y + 30)
                elif txtsize <= 0:
                    raise ValueError('字体不能小于等于零。The font can`t be 0 or less than 0')
            else:
                screen.geometry("330x70")
                tkinter.Label(screen, text=txt[0], fg='white', bg='black', font=("黑体", txtsize)).place(x=4, y=ott_y)
                tkinter.Label(screen, text=ottext, fg='white', bg='black', font=("黑体", txtsize)).place(x=4,y=ott_y + 15)