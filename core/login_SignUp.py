import configparser
from json import load,dumps
import os
import time
import sys
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import pygame_widgets
import core.Animation as Animation
import pygame
from threading import Timer
import threading

class login_signup():
    # 注册
    def signup(self):
        #读取登录码文件
        confpath = str(os.getcwd() + '\sur_Cod.ini')
        conf = configparser.ConfigParser()
        conf.read(confpath, encoding="utf-8")
        items = conf.items('usrcod')
        items1 = conf.items('usrnam')
        langfile = None
        #读取设置
        with open('./settings.json', 'r', encoding='utf8') as f:
            a = load(f)
            set = a['settings']
            language = set[0]['language']
            loginsignup = set[1]['login&signup']
            chos = set[2]['chos']
            f.close()
        # 获取语言设置
        if language == 'zh-cn':
            langfile = './lang/zh-CN.json'
        if language == 'ru-cccp':
            langfile = './lang/ru-CCCP.json'
        with open(langfile, 'r', encoding='utf8') as tex:
            text = load(tex)
            texts = text["signup"]
        print(texts[0]["sutel"])
        # 登录码拼接
        def coding(codefrst):
            codfrs = codefrst
            codsec = input(texts[1]["codsec"])
            for i1 in items1:
                if codsec == i1[1]:
                    print(texts[1]["error"])
                    while codsec == i1[1]:
                        codsec = input(texts[1]["codsec"])
                    break
            codtrd = time.strftime("%Y%m%d")
            cod = codfrs + '-' + codsec + '-' + codtrd
            print(texts[2]["cod"] + cod)
            for i in items:
                if i[1] == '':
                    conf.set("usrcod", i[0], cod)
                    a = int(i[0])
                    a += 1
                    conf.set("usrcod", str(a), '')
                    conf.write(open(confpath, "w"))
            for i1 in items1:
                if i1[1] == '':
                    a = int(i1[0])
                    a += 1
                    conf.set("usrnam", i1[0], codsec)
                    conf.set("usrnam", str(a), '')
                    conf.write(open(confpath, "w"))
                    self.login()
        ask1 = input(texts[1]["ask"])
        if ask1 == 'y':
            ask2 = input(texts[1]["ask1"])
            if ask2 == 'y':
                coding('C')
            if ask2 == 'n':
                coding('D')
        if ask1 == 'n':
            sys.exit(0)
    # 登录
    def login(self):
        path = os.getcwd()
        langfile = None
        with open('./settings.json', 'r', encoding='utf8') as f:
            a = load(f)
            text = a['settings']
            language = text[0]['language']
            loginsignup = text[1]['login&signup']
            chos = text[2]['chos']
            f.close()
        if language == 'zh-cn':
            langfile = './lang/zh-CN.json'
        if language == 'ru-cccp':
            langfile = './lang/ru-CCCP.json'
        with open(langfile, 'r', encoding='utf8') as tx:
            tex = load(tx)
            texts = tex["login"]
        confpath = str(path + '\sur_Cod.ini')
        conf = configparser.ConfigParser()
        conf.read(confpath, encoding="utf-8")
        items = conf.items('usrcod')
        items = conf.items('usrcod')
        anserchek = input(texts[0]["anserchek"])
        print(texts[1]["cheking"])
        # 保证登录码开头字母大写
        if anserchek.istitle() == True:
            pass
        if anserchek.istitle() == False:
            anserchek = str(anserchek.capitalize())
        for i in items:
            if str(i[1]) == str(anserchek):
                print(texts[2]["succesed"])
                a = True
                chos()
                break
            else:
                a = False
                print(texts[3]["failed"])
        if a == True:
            pass
        else:
            print(texts[3]["failed1"])
            c = input(texts[3]["failed2"])
            if c == 'y' or 'г':
                self.signup()
            else:
                self.login()
    def LoginUI(self):
        state = 'PleaseLogin'
        drawbox = False
        LoginWarning = 'stop'
        pygame.init()
        screen = pygame.display.set_mode((900, 450))
        loginscreen = pygame.display.set_mode((900, 450))
        conf = configparser.ConfigParser()
        conf.read('D:\AKDWPythonCMD\sur_Cod.ini', encoding="utf-8")
        items = conf.items('usrcod')
        loginback = pygame.image.load('./AFTERLOGIN/AFTERLOGIN0001.png').convert_alpha()
        img = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\YESNO\bulebutton.png')
        butonback = pygame.transform.scale(img, (120, 24))
        login_warning = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\LOGO\login_warning.png').convert_alpha()
        login_warning_text = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\TEXT\Warning_Text.png').convert_alpha()
        font = pygame.font.Font(r'D:\AKDWPythonCMD\data\Font\Novecentowide-Normal.ttf', 20)
        pygame.display.set_caption('AKDW')

        def To_Login():
            global state, drawbox
            Animation.AFTERCLICK.stop()
            state = 'Login'
            drawbox = True

        def buton():
            global state, textbox, LoginWarning

            def StopWarning():
                global LoginWarning, textbox, button
                textbox.setX(426)
                button.setX(480)
                LoginWarning = 'stop'

            no = 0
            anserchek = textbox.getText()
            if anserchek.istitle() == True:
                pass
            if anserchek.istitle() == False:
                anserchek = str(anserchek.capitalize())
            for i in items:
                if str(i[1]) == str(anserchek) and str(i[1]) != '':
                    state = 'AfterLogin'
                    break
                else:
                    no += 1
                    if no == len(items):
                        textbox.setText('')
                        t1 = Timer(0.375, StopWarning)
                        LoginWarning = 'play'
                        LoginWarning = 'stop'
                        LoginWarning = 'play'
                        t1.start()

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and state == 'PleaseLogin' and state != 'None':
                    state = 'AfterClick'
                    t0 = Timer(1.85, To_Login)
                    t0.start()
            if state == 'PleaseLogin':  # 16.7ms
                Animation.PLEASELOGIN.play()
                Animation.PLEASELOGIN.blit(screen)
            if state == 'AfterClick':
                Animation.PLEASELOGIN.stop()
                Animation.AFTERCLICK.play()
                Animation.AFTERCLICK.blit(screen)
            if state == 'Login':
                loginscreen.blit(loginback, (0, 0))
            if state == 'None':
                Animation.PLEASELOGIN.stop()
                Animation.AFTERCLICK.stop()
            if LoginWarning == 'play':
                textbox.setX(1000)
                button.setX(1000)
                loginscreen.blit(login_warning, (340, 90))
                loginscreen.blit(login_warning_text, (170, 220))
            if drawbox == True:
                textbox = TextBox(loginscreen, 426, 222, 220, 24, colour=(0, 0, 0), fontSize=20,
                                  textColour=(255, 255, 255),
                                  font=font)
                button = Button(loginscreen, 480, 265, 120, 24, text='Login', font=font, textColour=(255, 255, 255),
                                fontSize=15, margin=20, onClick=buton, image=butonback)
                drawbox = False
            if state == 'AfterLogin':
                drawbox = False
                textbox.setX(1000)
                button.setX(1000)
                Animation.AFTERLOGIN.play()
                Animation.AFTERLOGIN.blit(screen)
            pygame_widgets.update(events)
            pygame.display.flip()

    def welcom(self):
        login = login_signup()
        path = os.getcwd()
        confpath = str(path + '\sur_Cod.ini')
        conf = configparser.ConfigParser()
        conf.read(confpath, encoding="utf-8")
        items = conf.items('usrcod')
        items1 = conf.items('usrnam')
        langfile = None
        with open('./settings.json', 'r', encoding='utf8') as f:
            a = load(f)
            set = a['settings']
            language = set[0]['language']
            loginsignup = set[1]['login&signup']
            chos = set[2]['chos']
            f.close()
        if language == 'zh-cn':
            langfile = './lang/zh-CN.json'
        elif language == 'ru-cccp':
            langfile = './lang/ru-CCCP.json'
        with open(langfile, 'r', encoding='utf8') as tex:
            text = load(tex)
            texts = text["welcom"]
        if loginsignup == 'mix':
            UIAsk = input(texts[0]['UIAsk'])
            if UIAsk == 'y':
                os.system('python ' + path + r'\welcomUI.py')
                print(texts[1]["loging"])
                UIAsk = 'N'
            else:
                ask = input(texts[2]["ask"])
                if ask == 's':
                    login.signup()
                else:
                    login.login()
        elif loginsignup == 'UI':
            os.system('python ' + path + r'\welcomUI.py')
        elif loginsignup == 'CO':
            ask = input(texts[2]["ask"])
            if ask == 's':
                thread = threading.Thread(target=login.signup)
                thread.start()
                thread.join()
                login.login()
            else:
                login.login()
        else:
            print(texts[3]["error"])
            time.sleep(5)