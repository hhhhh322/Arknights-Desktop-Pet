import pygame

import pygame_widgets
from pygame_widgets.button import Button

# Set up Pygame
pygame.init()
win = pygame.display.set_mode((600, 600))
img=pygame.image.load(r'D:\AKDWPythonCMD\data\UI\YESNO\blackno.png')
img1=pygame.transform.scale(img,(425,50))
# Creates the button with optional parameters
img2= pygame.image.load(r'D:\AKDWPythonCMD\data\UI\YESNO\buleyes.png')# 4.9:1
img2_1=pygame.transform.scale(img2,(490,100))
page = 1
button=None
run = True
def set(n):
    global page
    page=n
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    if page == 1:
        button = Button(
            # Mandatory Parameters
            win,  # Surface to place button on
            100,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            425,  # Width
            50,  # Height

            # Optional Parameters
            margin=20,  # Minimum distance between text/image and edge of button
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda n=2: set(n),  # Function to call when clicked on
            image=img1
        )
    if page == 2:
        button.image = img2_1
    win.fill((255, 255, 255))

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()