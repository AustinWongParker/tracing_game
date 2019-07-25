'''
Main file of the tracing game using pygame.

Name(s): Austin Wong-Parker, Will Ament

Start date: June 2019

TO-DO:
1. Create floating animated text
    a. 'Click any key to continue'
    b. sound
    c. font (bubbly / cloudy font?)
    d. background: blue sky
        - cloud bouncing up and down with text moving with it
2. Create screen GUI
    a. display level top left corner
    b. refresh button to redraw shape top right corner
    c. no sound bottom right corner
3. Create shape drawings
    a. 5 levels
    b. different color per drawing
    c. animated drawing that will be slow enough for the user to see
        - last ~ 3 seconds after drawing is complete then disappear

'''

import pygame, sys
from pygame.locals import*
import time
import start_menu as SM
import globals

pygame.init()

screen = pygame.display.set_mode((800, 600)) # display surface
pygame.display.set_caption('Tracing Game')
FPS = 30
fpsClock = pygame.time.Clock()

def show_start_menu(self):
    pass


beach_background = pygame.image.load('beach.jpg')
beach_background = pygame.transform.scale(beach_background, (800, 600))

###########################################################
#                      GAME LOOP                          #
###########################################################

globals.initialize()
globals.menu_status = True
SM.start_menu_loop()

def gameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            screen.blit(beach_background, (0,0))
            pygame.display.update() # draws the surface object to the screen/window
            fpsClock.tick(FPS)



gameLoop()

#if __name__ == '__main__':
