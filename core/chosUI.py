import pygame
from core.Button import Button
import sys
from MDF import MDF
import os
import re

def plus():
    global drawing
    if drawing == 3:
        drawing=1
    else:
        drawing+=1
def reduction():
    global drawing
    if drawing == 1:
        drawing=3
    else:
        drawing-=1
def func(path):
    print(path)
def Deploy(path):
    pygame.quit()
    pa=os.listdir(path)
    for i in pa:
        if '.json'in i:
            JsonFile = i
            break
    Json_Path=path+'\\'+ JsonFile
    MDF.run(Json_Path,JsonFile.replace('.json',''))
def back_func():
    global scence
    scence='chos'
def show(path):
    global scence,VP,tl,DeployButton
    scence='show'
    vp_path = path+'\VP.png'
    VP = pygame.image.load(vp_path).convert_alpha()
    font = pygame.font.SysFont('microsoftyahei', 14)
    deploybutton = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\DeployButton.png').convert_alpha()
    DeployButton = Button(screen, deploybutton, lambda path=path:Deploy(path), 685, 380)
    with open(r'D:\AKDWPythonCMD\core\Valves\Kalsits\show.txt', 'r', encoding='utf-8') as f:
        tl = []
        t = f.readlines()
        for i in t:
            if len(i) > 18 and len(i) < 40 and len(i) != 18:
                txt = re.findall(r'.{18}', i)
                te0 = font.render(txt[0], True, (0, 0, 0), None)
                tl.append(te0)
                if i.replace(txt[0], '') != '\n':
                    te = font.render(i.replace(txt[0], '').replace('\n', ''), True, (0, 0, 0), None)
                    tl.append(te)
            elif len(i) < 18 and len(i) > 0 or len(i) == 18:
                te = font.render(i.replace('\n', ''), True, (0, 0, 0), None)
                tl.append(te)
            else:
                raise ValueError('too much word in one line!less than 40!')

pygame.init()
screen = pygame.display.set_mode((900, 450))
MDF=MDF()
background = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\chosback.jpg').convert()
directionl=pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\direction.png').convert_alpha()
None_show=pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\None_show.png').convert_alpha()
pages_1=pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\page1.png').convert_alpha()
pages_2=pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\page2.png').convert_alpha()
pages_3=pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\page3.png').convert_alpha()
#showbackground = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\ShowBack.png').convert()
organization_path = r'D:\AKDWPythonCMD\data\UI\LOGO\S_RhodesIslan.png'
back = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\BackButton.png').convert_alpha()
#skin = pygame.image.load(r'D:\AKDWPythonCMD\data\UI\BACKGROUND\SkinButton.png').convert_alpha()
organization = pygame.image.load(organization_path).convert_alpha()

BackButton = Button(screen, back, back_func, 10, 10)
#SkinButton = Button(screen, skin, func, 97, 10)
directionr=pygame.transform.flip(directionl,True,False)
direction0=Button(screen,directionl,reduction,0,145.5)
direction1=Button(screen,directionr,plus,813,145.5)
page_buton_name=['page1_1','page1_2','page1_3','page1_4','page1_5','page1_6','page1_7','page1_8','page2_1','page2_2','page2_3','page2_4','page2_5','page2_6','page2_7','page2_8','page3_1','page3_2','page3_3','page3_4','page3_5','page3_6','page3_7','page3_8']
x=225
y=40
c=1
l=[]
VP=''
drawing=1
scence='chos'
path='D:\AKDWPythonCMD\core\Valves'
pak=MDF.Search(path)
for name in page_buton_name:
    if c == 5 or c==13 or c==21:
        x=225
        y+=200
    if c==9 or c==17:
        x=225
        y=40
    name = Button(screen,None_show,func,x,y)
    x+=120
    c+=1
    l.append(name)
page1=l[0:8]
page2=l[8:16]
page3=l[16::1]
page1no=page2no=page3no=0
c=0
last=2
if len(pak)<=24:
    for dir_name in pak:
        show_path=path+'\\'+dir_name+'\\'+'Show.png'
        dir_name=pygame.image.load(show_path).convert()
        if page1no!=8:
            for button in page1:
                if button.i==None_show:
                    button.i = dir_name
                    button.c=lambda path=show_path.replace('\\Show.png',''):show(path)
                    page1no+=1
                    break
        elif page1no == 8 and page2no!=8:
            for button in page2:
                if button.i == None_show:
                    button.i = dir_name
                    page2no += 1
                    break
        elif page1no==8 and page2no == 8 and page3no!=8:
            for button in page3:
                if button.i == None_show:
                    button.i = dir_name
                    break
else:
    raise ValueError('too much packages!less than 24!')
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if scence == 'chos':
        screen.blit(background, (0, 0))
        direction0.button(events)
        direction1.button(events)
        if drawing == 1:
            for button in page1:
                button.button(events)
            screen.blit(pages_1,(437,430))
        if drawing == 2:
            for button in page2:
                button.button(events)
            screen.blit(pages_2, (437, 430))
        if drawing == 3:
            for button in page3:
                button.button(events)
            screen.blit(pages_3, (437, 430))
    if scence == 'show':
        screen.blit(background, (0, 0))
        screen.blit(VP, (0, 0))
        DeployButton.button(events)
        screen.blit(organization, (0, 0))
        BackButton.button(events)
        #SkinButton.button(events)
        y = 70
        for text in tl:
            screen.blit(text, (655, y))
            y += 20
    pygame.display.flip()
