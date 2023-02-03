import pygame
import pygame.freetype
import sys,os
sys.path.append(os.getcwd())
import core.SoapSystem as SoapSystem

pygame.init()
# 设置窗口大小

screen = pygame.display.set_mode((850,91))

# 设置游戏标题
pygame.display.set_caption('pygame_test')
# 游戏时钟
clock = pygame.time.Clock()
while True:
    # 游戏更新频率
    clock.tick(60)
    # 退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    SoapSystem.function(screen=screen,x=0,y=0,back=r'D:\AKDWPythonCMD\data\UI\BACKGROUND\talkbak.png',text='我会定期为你进行理学检查，记录你的生命征象与意识状态，其他人没有这个权限。任何人想对你进行进一步的检查，你都有权拒绝，明白吗？')
    pygame.display.update()