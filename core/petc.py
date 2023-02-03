import pygame
from pygame.locals import *
import time
import os
import sys
import win32api,win32con,win32gui
import _thread
from threading import Timer
import tkinter
import requests
from json import load
from tkinter import messagebox
from random import randint
import FavorabilitySystem as FavorabilitySystem
import SoapSystem

def weather():
    global weathert,temperlow

    beijing = 'http://t.weather.sojson.com/api/weather/city/101010100'
    shanghai = 'http://t.weather.sojson.com/api/weather/city/101020100'
    guangzhou = 'http://t.weather.sojson.com/api/weather/city/101280101'
    shengzheng = 'http://t.weather.sojson.com/api/weather/city/101280601'
    dongguan = 'http://t.weather.sojson.com/api/weather/city/101281601'

    with open('./settings.json', 'r', encoding='utf8') as f:
        a = load(f)
        text = a['settings']
        weatherplace = text[3]['wetherplace']
        f.close()
    try:
        if weatherplace == 'dongguan':
            response = requests.get(dongguan)
            d = response.json()
            if (d['status'] == 200):
                temperlow = str(d["data"]["forecast"][0]["low"])
                temperlow = temperlow.replace("低温", '')
                temperlow = int(temperlow.replace("℃", ''))
                weathert = str(d["data"]["forecast"][1]["type"])
        if weatherplace == 'shengzheng':
            response = requests.get(shengzheng)
            d = response.json()
            if (d['status'] == 200):
                temperlow = str(d["data"]["forecast"][0]["low"])
                temperlow = int(temperlow.replace("低温", ''))
                weathert = str(d["data"]["forecast"][1]["type"])
        if weatherplace == 'guangzhou':
            response = requests.get(guangzhou)
            d = response.json()
            if (d['status'] == 200):
                temperlow = str(d["data"]["forecast"][0]["low"])
                temperlow = int(temperlow.replace("低温", ''))
                weathert = str(d["data"]["forecast"][1]["type"])
        if weatherplace == 'shanghai':
            response = requests.get(shanghai)
            d = response.json()
            if (d['status'] == 200):
                temperlow = str(d["data"]["forecast"][0]["low"])
                temperlow = int(temperlow.replace("低温", ''))
                weathert = str(d["data"]["forecast"][1]["type"])
        if weatherplace == 'beijing':
            response = requests.get(beijing)
            d = response.json()
            if (d['status'] == 200):
                temperlow = str(d["data"]["forecast"][0]["low"])
                temperlow = int(temperlow.replace("低温", ''))
                weathert = str(d["data"]["forecast"][1]["type"])
    except:
        messagebox.showerror(title='error', message='你尚未连接WLAN')

class pet():
    def __init__(self):
        self.idle = True
        self.sleep = False
        self.sit = False
        self.interact = False
        self.move = False
        self.special= False
        self.run = True
        self.x = 0
        self.y = 0
        self.fileclin = 0
        self.randomtalk = 0  # 随机语音初始值   Random speech initial value
        self.exit1 = 0
        self.sits = 0
        self.sleps = 0
        self.LEFT = 'left'
        self.RIGHT = 'right'
        self.f = 0
        self.F=self.RIGHT
        mode=''
        self.ClikC=0
    def name(self,name):
        self.Name=name
        self.F_Value=FavorabilitySystem.ChekPoint(self.Name)
    def ltrans(self,winx,winy):
        global hwnd, trans,Sx,Sy,X,Y
        trans = (0, 0, 4)  # 窗口透明的必要条件 A requirement for window transparency
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*trans), 0, win32con.LWA_COLORKEY)
        Sx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴 Get the screen resolution X axis
        Sy = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获取屏幕分辨率Y轴 Get the screen resolution Y axis
        X = Sx - winx
        Y = Sy - winy
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, X, Y-50, 0, 0, win32con.SWP_NOSIZE)
    def Soap(self,text,x):
        def SoapThread():
            defaultsize = '240x70'
            othersize = '330x70'
            i = 20
            wind = tkinter.Tk()
            wind.geometry(defaultsize + '+' + str(X + x) + '+' + str(Y - 130))
            wind.configure(bg='#000000')
            wind.attributes("-alpha", 0.8)  # 设置窗体透明度
            wind.resizable(False, False)
            wind.overrideredirect(True)
            SoapSystem.SoapSystem(wind, text, txtsize=10)
            t2 = Timer(5, wind.destroy)
            t2.start()
            wind.mainloop()

        try:
            _thread.start_new_thread(SoapThread, ())
        except:
            print('Soap Error')
    def move(self,f):
        if f != 0:
            self.x += f
            if f<0:
                self.move=self.LEFT
            elif f>0:
                self.move=self.RIGHT
        elif f==0:
            self.move=False

    def moving(self):
        if self.F == self.RIGHT:
            self.x += 1
        if self.F == self.LEFT:
            self.x -= 1
    def back(self):
        global f,ta
        ta = time.strftime('%S')
        self.y = 0
        self.idle = False
        f = 3
        if self.F == self.RIGHT and f == 3:
            self.F = self.LEFT
            self.x += 30
            self.idle = True
            f = 2
        if self.F == self.LEFT and f == 3:
            self.F = self.RIGHT
            self.x -= 30
            self.idle = True
            f = 2
    def STOP(self):
        self.y = 0
        if self.move == False:
            self.idle = True
            self.interact = False
            self.sit = False
    def setsits(self):
        global sits
        sits = 0
    def Animate(self, args):
        self.Anirelax = args[0]
        self.Aniinteract = args[1]
        self.Anisit = args[2]
        self.Anisleep = args[3]
        self.Animove = args[4]
        if args[5] == None:
            self.special=None
        else:
            self.Anispecial=args[5]
            self.Anilspecial=args[11]
        self.Anilsit = args[6]
        self.Anilsleep = args[7]
        self.Anilrelax = args[8]
        self.Anilinteract = args[9]
        self.Anilmove = args[10]

    def Audio(self, Audios):
        self.stouch1 = Audios[0]
        self.stouch2 = Audios[1]
        self.stouch3 = Audios[2]
        self.stouch4 = Audios[3]
        self.stouch5 = Audios[4]
        self.sosleeps = Audios[5]
        self.sourain = Audios[6]
        self.soucold = Audios[7]
        self.sounhot = Audios[8]
    def init(self,size:list):
        global win
        pygame.init()  # Pygame初始化 Pygame initialization
        pygame.mixer.init()
        win = pygame.display.set_mode((int(size[0]),int(size[1])),NOFRAME)  # 窗口和窗口无边框 Window and leave the window borderless
        self.ltrans(int(size[0]),int(size[1]))
        self.setsits()
    def default_main(self, interactstop, sittime):
        sits = 0
        clock = pygame.time.Clock()
        while self.run:
            timeg = int(time.strftime('%H'))
            time.sleep(0.00999999)  # 减少CUP占用 Reduce CUP occupancy
            randomsit = 0
            randommove = 0
            randomsit = randint(0, 3999)
            randommove = randint(0, 4000)
            time.sleep(0.00999999)
            win.fill(trans)  # 背景透明 Make the background transparent
            Sit_Event = pygame.USEREVENT + 1
            Exit_Event = pygame.USEREVENT + 1
            xp, yp = pygame.mouse.get_pos()
            if self.exit1 == 1:
                exitevent = pygame.event.Event(Exit_Event)
                pygame.event.post(exitevent)
            if randommove == 173:
                self.idle = False
                self.move = True
            if timeg == 2:
                self.idle = True
                self.sleep = False
            if randomsit == 79:
                self.sit = True
                sits = 1
                t = Timer(0.001, self.setsits)
                t.start()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_LCTRL] and key_pressed[K_LSHIFT]:
                pygame.quit()
                pygame.mixer.quit()
                _thread.exit()
                os.system('taskkill /f /t /im ' + 'TrafficMonitor.exe')
                #os.system('taskkill /f /t /im ' + 'python.exe')
                self.idle = False
                self.sleep = False
                self.sit = False
                self.interact = False
                self.move = False
                self.run = False
                sys.exit(0)
            if key_pressed[K_m]:
                self.move = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.mixer.quit()
                    sys.exit()
                # 信赖触摸 Trust touch
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.interact == False and self.sleep == False and xp >=int(self.x) and xp <= int(self.x)+185 and event.button == 1:
                        self.idle = False
                        self.interact = True
                        t = Timer(float(interactstop), self.STOP)  # 动画延时停止 Let the animation stall to stop
                        t.start()
                        self.ClikC+=1
                        # 随机语音 Random voice
                        randomtalk = randint(1, 9)
                        if randomtalk == 1 and self.stouch1!=None:
                            self.stouch1.play()
                            self.Soap('我会定期为你进行理学检查，记录你的生命征象与意识状态，其他人没有这个权限。任何人想对你进行进一步的检查，你都有权拒绝，明白吗？',0)
                            self.randomtalk = -1
                        if randomtalk == 2 or randomtalk == 6 and self.stouch2 != None:
                            self.stouch2.play()
                            self.Soap('越是强大，越是脆弱，这就是万物的道理。', 0)
                            randomtalk = -1
                        if randomtalk == 3 or randomtalk == 7 and self.stouch3 != None:
                            self.stouch3.play()
                            self.Soap('你在做什么？', 0)
                            self.randomtalk = -1
                        if randomtalk == 4 or randomtalk == 8 and self.stouch4 != None:
                            self.stouch4.play()
                            self.Soap('你似乎更加适应自己的工作和职责了，更像一个领导者了。', 0)
                            self.randomtalk = -1
                        if randomtalk == 5 or randomtalk == 9 and self.stouch5 != None:
                            self.stouch5.play()
                            self.Soap('现在，你只要做好行动计划。', 0)
                            self.randomtalk = -1
                        # 好感度增加
                        if self.F_Value != 200 and self.ClikC<=3 and self.randomtalk == -1:
                            self.F_Value += 1
                            FavorabilitySystem.ChekIn(self.Name,self.F_Value)
                            self.randomtalk=0
                if event.type == Exit_Event:
                    pygame.quit()
                    pygame.mixer.quit()
                    sys.exit()
                if event.type == Sit_Event:
                    self.sit = True
                    t = Timer(float(sittime), self.STOP)
                    t.start()
            # 保持待机动画 Keep the idle animated
            if self.sleep == False and self.sit == False and self.interact == False and self.move == False:
                self.idle = True
            if self.idle == True and self.sleep == False:
                if self.F == self.RIGHT:
                    self.Anirelax.play()
                    self.Anirelax.blit(win, (self.x, self.y))
                if self.F == self.LEFT:
                    self.Anilrelax.play()
                    self.Anilrelax.blit(win, (self.x, self.y))
            # 结束待机动画 Ends the standby animation
            if self.idle == False:
                self.Anirelax.stop()
                self.Anilrelax.stop()
            if sits == 1:
                t = Timer(sittime, self.STOP)
                t.start()
            if self.sit == True and self.sleep == False and self.move == False and self.interact == False:
                self.idle = False
                self.y = 10
                if self.F == self.RIGHT:
                    self.Anisit.play()
                    self.Anisit.blit(win, (int(self.x)+35, self.y))
                if self.F == self.LEFT:
                    self.Anilsit.play()
                    self.Anilsit.blit(win, (int(self.x) + 35, self.y))
            # interact动画触发 Interact animation triggered
            if self.interact == True:
                self.sit = False
                self.move = False
                self.idle = False  # 结束待机动画 Ends the standby animation
                if self.F == self.RIGHT:
                    self.Aniinteract.play()  # 播放interact动画 Play an interact animation
                    self.Aniinteract.blit(win, (self.x, self.y))
                if self.F == self.LEFT:
                    self.Anilinteract.play()
                    self.Anilinteract.blit(win, (self.x, self.y))
            # 结束interact动画 End the interact animation
            if self.interact == False:
                self.Aniinteract.stop()
                self.Anilinteract.stop()
            if timeg == 23 or timeg == 0 or timeg == 1:
                self.idle = False
                self.sit = False
                self.interact = False
                self.move = False
                self.sleep = True
            if timeg != 23 and timeg != 0 and timeg != 1 and timeg != 2 and timeg != 3 and timeg != 4:
                self.sleep = False
            if self.sleep == True:
                self.y = 100
                if self.F == self.RIGHT:
                    self.Anisleep.play()
                    self.Anisleep.blit(win, (self.x, self.y))
                if self.F == self.LEFT:
                    self.Anilsleep.play()
                    self.Anilsleep.blit(win, (self.x, self.y))
            if self.sleep == False:
                self.y = 0
                self.Anisleep.stop()
                self.Anilsleep.stop()
            if self.move == True:
                self.sit = False
                self.idle = False
                if self.F == self.RIGHT:
                    self.Animove.play()
                    self.Animove.blit(win, (self.x, self.y))
                if self.F == self.LEFT:
                    self.Anilmove.play()
                    self.Anilmove.blit(win, (self.x, self.y))
                self.moving()
            if self.move == False:
                self.Animove.stop()
                self.Anilmove.stop()
            if int(self.x) + 201 == 850 and self.move == True and self.F == self.RIGHT:
                if self.f != 2 and self.move == True:
                    t1 = Timer(10, self.back)
                    t1.start()
                self.move = False
            if int(self.x) == 55 and self.move == True and self.F == self.LEFT:
                tb = time.strftime('%S')
                t = 10
                if self.f != 2 and self.move == True:
                    if self.interact == True:
                        t+=2
                    t1 = Timer(t, self.back)
                    t1.start()
                if 0<int(tb)-int(ta)<t or 0<int(ta)-int(tb)<t:
                    self.back()
                self.move = False
                for i in range(0,9):
                    self.move = False
            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)
    def timeremind(self, remindtime):
        def timere_thread():
            while True:
                timeg1 = int(time.strftime('%H%M%S'))
                time.sleep(0.9)
                if timeg1 == int(remindtime) and self.F_Value >= 10:
                    self.sosleeps.play()  # 晚上提醒睡觉 Reminder to sleep at night
                    self.Soap('博士，根据你的身体状况，你需要休息了。', 0)
                    break
        try:
            _thread.start_new_thread(timere_thread, ())
        except:
            print('timer error')
    def weather(self, wtime, lowtime, drinktime):
        def weather_thread():
            while True:
                timeg1 = int(time.strftime('%H%M%S'))
                time.sleep(0.9)
                if timeg1 == int(wtime) and '雨' in weathert and self.F_Value>=10:
                    self.sourain.play()
                    self.Soap('博士，明天有雨，记得带伞', 0)
                    break
                if timeg1 == int(lowtime) and self.interact == False and temperlow <= 20 and self.F_Value>=10:
                    self.soucold.play()
                    self.Soap('博士，明天很冷，多穿点衣服', 0)
                    break
                if timeg1 == int(drinktime) and self.interact == False and temperlow >= 26 and self.F_Value>=10:
                    self.sounhot.play()
                    self.Soap('博士，天气很热，多喝水', 0)
                    break
        try:
            _thread.start_new_thread(weather_thread, ())
        except:
            print('weather error')
