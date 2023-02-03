import pyganim
import pygame
import sys
import win32api
import win32con
import win32gui
pygame.init()
screen = pygame.display.set_mode((400,400))
trans = (0, 0, 0)  # 窗口透明的必要条件 A requirement for window transparency
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*trans), 0, win32con.LWA_COLORKEY)
a = pyganim.PygAnimation([])


while True:
    # 循环获取事件，监听事件
    for event in pygame.event.get():
        # 判断用户是否点了关闭按钮
        if event.type == pygame.QUIT:
            # 当用户关闭游戏窗口时执行以下操作
            # 这里必须调用quit()方法，退出游戏
            pygame.quit()
            #终止系统
            sys.exit()
    screen.fill(trans)
    a.play()
    a.blit(screen)
    #更新并绘制屏幕内容
    pygame.display.flip()