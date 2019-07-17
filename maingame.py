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

pygame.init()

screen = pygame.display.set_mode((800, 600)) # display surface
pygame.display.set_caption('Tracing Game')

'''
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
'''

Background = pygame.image.load('sky.jpeg')
Background = pygame.transform.scale(Background, (800, 600))
cloud_BG = pygame.image.load('cloud.jpg')
cloud_BG = pygame.transform.scale(cloud_BG, (400, 300))

while True: # Game Loop
    for event in pygame.event.get(): # list of event objects generated throughout the game
        if event.type == QUIT: # checks for QUIT in the event type
            pygame.quit()
            sys.exit()
        screen.fill([255, 255, 255])
        screen.blit(Background, (0,0))
        screen.blit(cloud_BG, (220, 150))
        pygame.display.update() # draws the surface object to the screen/window
