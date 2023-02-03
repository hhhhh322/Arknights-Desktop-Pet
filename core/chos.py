import os
import sys
import shutil
import psutil
from json import load
import time
import pygame
from pygame.locals import *

def chos():
    # 查找插件
    datanames = os.listdir('./core/Valves')
    langfile = None
    # 定义展示方法
    def showing(iin):
        pa = './core/valves/' + iin + '/show.txt'
        with open(pa, 'r', encoding='utf-8') as t:
            te = t.read()
            print(te)
        t.close()
    # 语言
    with open('./settings.json', 'r', encoding='utf8') as f:
        a = load(f)
        text = a['settings']
        language = text[0]['language']
        loginsignup = text[1]['login&signup']
        chos = text[2]['chos']
        f.close()
    # 根据不同的设置加载不同的语言文件
    if language == 'zh-cn':
        langfile = './lang/zh-CN.json'
    if language == 'ru-cccp':
        langfile = './lang/ru-CCCP.json'
    with open(langfile, 'r', encoding='utf8') as tex:
        text = load(tex)
        texts = text["chos"]
    print(texts[11]["welcom"])
    print(r'          _____                    _____                    _____                    _____          ')
    print(r'         /\    \                  /\    \                  /\    \                  /\    \         ')
    print(r'        /::\    \                /::\____\                /::\    \                /::\____\        ')
    print(r'       /::::\    \              /:::/    /               /::::\    \              /:::/    /        ')
    print(r'      /::::::\    \            /:::/    /               /::::::\    \            /:::/   _/___')
    print(r'     /:::/\:::\    \          /:::/    /               /:::/\:::\    \          /:::/   /\    \     ')
    print(r'    /:::/__\:::\    \        /:::/____/               /:::/  \:::\    \        /:::/   /::\____\    ')
    print(r'   /::::\   \:::\    \      /::::\    \              /:::/    \:::\    \      /:::/   /:::/    /    ')
    print(r'  /::::::\   \:::\    \    /::::::\____\________    /:::/    / \:::\    \    /:::/   /:::/   _/___  ')
    print(r' /:::/\:::\   \:::\    \  /:::/\:::::::::::\    \  /:::/    /   \:::\ ___\  /:::/___/:::/   /\    \ ')
    print(r'/:::/  \:::\   \:::\____\/:::/  |:::::::::::\____\/:::/____/     \:::|    ||:::|   /:::/   /::\____\ ')
    print(r'\::/    \:::\  /:::/    /\::/   |::|~~~|~~~~~     \:::\    \     /:::|____||:::|__/:::/   /:::/    /')
    print(r' \/____/ \:::\/:::/    /  \/____|::|   |           \:::\    \   /:::/    /  \:::\/:::/   /:::/    / ')
    print(r'          \::::::/    /         |::|   |            \:::\    \ /:::/    /    \::::::/   /:::/    /  ')
    print(r'           \::::/    /          |::|   |             \:::\    /:::/    /      \::::/___/:::/    /   ')
    print(r'           /:::/    /           |::|   |              \:::\  /:::/    /        \:::\__/:::/    /    ')
    print(r'          /:::/    /            |::|   |               \:::\/:::/    /          \::::::::/    /     ')
    print(r'         /:::/    /             |::|   |                \::::::/    /            \::::::/    /      ')
    print(r'        /:::/    /              \::|   |                 \::::/    /              \::::/    /       ')
    print(r'        \::/    /                \:|   |                  \::/____/                \::/____/        ')
    print(r'         \/____/                  \|___|                   ~~                       ~~              ')
    print('                                                                                                     ')
    print(texts[0]["tel1"])
    while True:
        ask = input('AKDW>')
        if ask == 'show':
            datanames = os.listdir('./core/Valves')
            print(texts[1]["available"])
            c = 0
            for i in datanames:
                print(i.ljust(15) + str(c))
                c += 1
            print('_____________________')
        elif ask == 'help':
            print(texts[2]["help"])
        elif ask == 'exit':
            sys.exit(0)
        elif ask == 'chos':
            sdcard = False
            count = 0
            # 查看卡带是否插入
            old_path = psutil.disk_partitions()# 获取盘符
            for i in range(0, len(old_path)):
                path = old_path[count][1]
                try:
                    files = os.listdir(path)
                    if '__init__.APC' in files:
                        sdcard = True
                        a = open(path + '__init__.APC', 'r')
                        data = load(a)
                        print(texts[12]["SD_Card"] + data["name"])
                        chosask = input(texts[12]["SD_Card1"])
                        if chosask == 'y':
                            os.system(path + 'main.bat')
                            break
                        else:
                            datanames = os.listdir('./core/Valves')
                            print(texts[3]["chostel"])
                            print(texts[1]["available"])
                            c = 0
                            for i in datanames:
                                print(i.ljust(15) + str(c))
                                c += 1
                            print(str(data["name"]).ljust(15) + 'SD_Card')
                            print('_____________________\n')
                            while True:
                                ask1 = input('choose>')
                                if ask1 != 'exit':
                                    if ask1 == 'SD_Card':
                                        os.system(path + 'main.bat')
                                    else:
                                        try:
                                            int(ask1)
                                        except:
                                            print(texts[4]["choslooptel"])
                                            continue
                                        if int(ask1) > c or int(ask1) < 0:
                                            print(texts[4]["choslooptel1"])
                                        else:
                                            p = datanames[int(ask1)]
                                            os.system('python ./core/Valves/' + p + '/main.py')
                                else:
                                    break
                    else:
                        count += 1
                except:
                    print('None')
                    count += 1
                    continue
            if sdcard == False:
                datanames = os.listdir('./core/Valves')
                print(texts[3]["chostel"])
                print(texts[1]["available"])
                c = 0
                for i in datanames:
                    print(i.ljust(15) + str(c))
                    c += 1
                print('_____________________\n')
                while True:
                    ask1 = input('choose>')
                    if ask1 != 'exit':
                        try:
                            int(ask1)
                        except:
                            print(texts[4]["choslooptel"])
                            continue
                        if int(ask1) > c or int(ask1) < 0:
                            print(texts[4]["choslooptel1"])
                        else:
                            p = datanames[int(ask1)]
                            os.system('python ./core/Valves/' + p + '/main.py')
                    else:
                        break
        elif 'show ' in ask and ask.index('s') == 0 and ask.index(' ') == 4:
            datanames = os.listdir('./core/Valves')
            try:
                aaa = int(ask.replace('show ', ''))
                b = datanames[aaa]
                showing(b)
            except:
                aa = ask.replace('show ', '')
                showing(aa)
        elif 'remove ' in ask and ask.index('r') == 0 and ask.index(' ') == 6:
            datanames = os.listdir('./core/Valves')
            try:
                aas = int(ask.replace('remove ', ''))
                if aas <= len(datanames):
                    bs = datanames[aas]
                    aks = input(texts[5]["removep"] + str(bs) + texts[5]["removep1"] + str(aas) + texts[5]["removep2"])
                    if aks == 'y' or 'г':
                        path = './core/Valves/' + str(bs)
                        shutil.rmtree(path)
                        print(texts[6]["removed"])
                    else:
                        print(texts[7]["cancel"])
                else:
                    print(texts[9]["unknownum"])
                    continue
            except:
                bs = ask.replace('remove ', '')
                if bs in datanames:
                    aas = datanames.index(bs)
                    aks = input(texts[5]["removep"] + str(bs) + texts[5]["removep1"] + str(aas) + texts[5]["removep2"])
                    if aks == 'y' or 'г':
                        path = './core/Valves/' + str(bs)
                        shutil.rmtree(path)
                        print(texts[6]["removed"])
                    else:
                        print(texts[7]["cancel"])
                else:
                    print(texts[8]["unknowpak"])
                    continue
        else:
            print(texts[10]["unknowcom"])

def chosUI():
    pygame.init()
    screen = pygame.display.set_mode((800, 450))
    background = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\chosback.png').convert()
    page = 1
    # count = len(os.listdir('./core/Valves'))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.display.update()
