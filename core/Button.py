import pygame


def func():
    ...

'''
c_show=True
def button(screen, imag: pygame.surface, command, x, y, event):
    if c_show == True:
        screen.blit(imag, (x, y))
    rect = imag.get_rect()
    nx = rect[2] +x
    ny = rect[3] + y
    func = command
    for e in event:
        if pygame.mouse.get_pos()[0] <= nx and pygame.mouse.get_pos()[0] >= x and pygame.mouse.get_pos()[1] <= ny and pygame.mouse.get_pos()[1] >= y and e.type == pygame.MOUSEBUTTONDOWN:
            func()
def un_show():
    global c_show
    c_show=False
'''

class Button:
    def __init__(self,screen, imag: pygame.surface, command, x, y):
        self.s=screen
        self.i=imag
        self.c=command
        self.x=x
        self.y=y
        self.cs=True
    def button(self,event):
        if self.cs == True:
            self.s.blit(self.i, (self.x, self.y))
        rect = self.i.get_rect()
        nx = rect[2] + self.x
        ny = rect[3] + self.y
        func = self.c
        for e in event:
            if pygame.mouse.get_pos()[0] <= nx and pygame.mouse.get_pos()[0] >= self.x and pygame.mouse.get_pos()[
                1] <= ny and pygame.mouse.get_pos()[1] >= self.y and e.type == pygame.MOUSEBUTTONDOWN and self.cs==True:
                func()
    def un_show(self):
        self.cs=False
    def show(self):
        self.cs=True
    def set_img(self,img):
        self.i=img