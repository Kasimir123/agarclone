import random
import pygame
from pygame import *

# Init pygame
pygame.init()
clock = pygame.time.Clock()

# Defines Constants
# Width and Height of Screen
W, H = 1000, 500
# Frames Per Second
FPS = 30
# Check if the game is running or not
IS_RUNNING = True

# Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)

# Direction Constants
UP = 'up()'
DOWN = 'down()'
LEFT = 'left()'
RIGHT = 'right()'

# Open game window
size = (W, H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("NAME")
background = pygame.surface.Surface(size).convert()
background.fill(BLACK)

# Check for input
def input():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass

# Main Loop Method
def run():
    time_passed = clock.tick(FPS) / 1000.0
    input()
    drawScreen()

# Drawing method
def drawScreen():
    screen.blit(background, (0 ,0))
    pygame.display.update()


# Main Loop
while IS_RUNNING:
        run()