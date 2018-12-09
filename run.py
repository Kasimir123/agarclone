# imports
import pygame
from pygame import *
import random
from character import Char
from enemies import Enemy

# Init pygame
pygame.init()
clock = pygame.time.Clock()

# Defines constants
W, H = 3000, 3000
camW, camH = 1000, 1000
FPS = 30
go = True

# Color Constants
YELLOW = (255,255,0)

# Direction Constants
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

# Create Player
radius = 10
character = Char(camW, camH, W, H, YELLOW, radius)

# Game Timers
pygame.time.set_timer(USEREVENT+1, random.randrange(3000, 5000))

# Create Enemies list
enemies = []

# Open game window
size = (camW, camH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Agar")
background = pygame.surface.Surface((W,H)).convert()
background.fill((0,0,0))

# Create enemies
def createEnemies():
    if len(enemies) < 250:
        X = random.randint(0, W)
        Y = random.randint(0, H)
        rad = random.randint(1, 25)
        speed = int(50 / rad)
        randCheck = random.randint(0,1)
        if randCheck == 1:
            randX = -1
        else:
            randX = 1
        randCheck2 = random.randint(0,1)
        if randCheck2 == 1:
            randY = -1
        else:
            randY = 1
        
        enemies.append(Enemy(X, Y, rad, YELLOW, speed, randX, randY))

# Check for input
def input():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        character.update(UP)
    if keys[pygame.K_DOWN]:
        character.update(DOWN)
    if keys[pygame.K_LEFT]:
        character.update(LEFT)
    if keys[pygame.K_RIGHT]:
        character.update(RIGHT)

# Drawing method
def drawScreen():
    screen.blit(background, (0 ,0))
    for x in enemies:
        x.move(W, H)
        delete = character.checkCollide(x)
        if x.pop:
            enemies.pop(enemies.index(x))
        x.draw(screen, character.camX, character.camY, camW, camH)
    character.draw(screen)
    pygame.display.update() 

# Main Loop Method
def run():
    time_passed = clock.tick(FPS) / 1000.0
    input()
    createEnemies()
    drawScreen()

def endScreen():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            character.alive = True
            character.radius = radius
            for x in enemies:
                enemies.pop(enemies.index(x))

# Main Game loop
while True:
    if character.alive:
        run()
    else:
        endScreen()
