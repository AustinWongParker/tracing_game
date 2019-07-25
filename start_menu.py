import pygame, sys
from pygame.locals import*
import time
import globals


pygame.init()

def start_menu_loop():

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

    class animated_press_any_key(object):
        def __init__(self): #constructor
            self.image = pygame.image.load('anykey.png')
            self.image = pygame.transform.scale(self.image, (415, 150))
            self.rect = self.image.get_rect()
            self.x = 220
            self.y = 280

        def draw(self, surface):
            surface.blit(self.image, (self.x, self.y))

    def press_any_key():
        if event.type == KEYDOWN:
            globals.menu_status = False

    Background = pygame.image.load('sky.jpeg')
    Background = pygame.transform.scale(Background, (800, 600))
    cloud_animated = animated_cloud()
    clock = pygame.time.Clock()
    any_key = animated_press_any_key()

    direction = 'down' # initial starting direction
    pygame.time.set_timer(pygame.USEREVENT, 50) # generates events for the cloud to move

    while globals.menu_status:
        for event in pygame.event.get():
            if event.type == QUIT:
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
            fpsClock.tick(FPS)
            press_any_key()
