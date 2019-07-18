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

pygame.init()

screen = pygame.display.set_mode((800, 600)) # display surface
pygame.display.set_caption('Tracing Game')
FPS = 30
fpsClock = pygame.time.Clock()

class animated_cloud(object):
    def __init__(self): # constructor
        self.image = pygame.image.load('cloud.png')
        self.image = pygame.transform.scale(self.image, (400, 300))
        self.rect = self.image.get_rect()
        # cloud's current position
        self.x = 210 # x and y hardcoded for center of screen // fix?
        self.y = 135

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    # manual movement of cloud
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 10 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

class animated_press_any_key(object):
    def __init__(self): #constructor
        self.image = pygame.image.load('anykey.png')
        self.image = pygame.transform.scale(self.image, (415, 150))
        self.rect = self.image.get_rect()
        self.x = 220
        self.y = 280

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

'''
    def bobbing(self):
        direction = 'down'
        if direction == 'down':
            self.y += 1
            if self.y == -1:
                direction = 'up'
        if direction == 'up':
            self.y -= 1
            if self.y == 120:
                direction = 'down'
        screen.blit(self.image, (self.x, self.y))

        while True:
            direction = 'up'
            if direction == 'up':
                self.y -= 10
                if self.y == 120:
                    direction = 'down'

            elif direction == 'down':
                self.y += 1
                if self.x == 150:
                    direction = 'up'
                    pygame.event.wait()
'''


Background = pygame.image.load('sky.jpeg')
Background = pygame.transform.scale(Background, (800, 600))
cloud_animated = animated_cloud()
clock = pygame.time.Clock()
any_key = animated_press_any_key()

direction = 'down' # initial starting direction



###########################################################
#                      GAME LOOP                          #
###########################################################

while True:
    for event in pygame.event.get(): # list of event objects generated throughout the game
        if event.type == QUIT: # checks for QUIT in the event type
            pygame.quit()
            sys.exit()

        # Start Screen w/ cloud and press any key to continue.
        # ----------------------------------------------------
        screen.blit(Background, (0,0))
        #cloud_animated.handle_keys()   # uncomment to use manual movement with arrow keys
        cloud_animated.draw(screen)
        any_key.draw(screen)
        top = 100
        bottom = 150
        if direction == 'down':
            cloud_animated.y += 1
            any_key.y += 1
            if cloud_animated.y == bottom:
                direction = 'up'
        elif direction == 'up':
            cloud_animated.y -= 1
            any_key.y -= 1
            if cloud_animated.y == top:
                direction = 'down'

        pygame.display.update() # draws the surface object to the screen/window

        #screen.blit(cloud_animated.image, (cloud_animated.x, cloud_animated.y))

        fpsClock.tick(FPS)

        # TO-DO: sky transition into tracing game background???


        # Main Tracing game
