import random
import pygame
from pygame import *
from Characters import Player, Enemy


# Init pygame
pygame.init()
clock = pygame.time.Clock()


# Defines constants
# Width and Height of the game
W, H = 3000, 3000
# Width and Height for what the player can see
CAM_W, CAM_H = 1000, 1000
# Frames Per Second
FPS = 30
# Check if the game is running or not
IS_RUNNING = True

# Player Constants
PLAYER_RADIUS = 10
PLAYER_SPEED = 10

# Color Constants
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
NUM_OF_COLORS = 3

# Color Switch
colors = {
    1: YELLOW,
    2: WHITE,
    3: RED
}

# Direction Constants
UP = 'up()'
DOWN = 'down()'
LEFT = 'left()'
RIGHT = 'right()'

# Create Player
character = Player(CAM_W, CAM_H, W, H, YELLOW, PLAYER_RADIUS, PLAYER_SPEED)

# Game Timers
pygame.time.set_timer(USEREVENT + 1, random.randrange(3000, 5000))

# Create Enemies list
enemies = []

# Open game window
size = (CAM_W, CAM_H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Agar")
background = pygame.surface.Surface((W,H)).convert()
background.fill(BLACK)


# Create enemies
def createEnemies():
    if len(enemies) < 250:
        X = random.randint(0, W)
        Y = random.randint(0, H)
        rad = random.randint(1, 25)
        color = random.randint(1, NUM_OF_COLORS)
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

        enemies.append(Enemy(X, Y, rad, colors[color], speed, randX, randY))


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
        character.checkCollide(x)
        for y in enemies:
            x.checkCollide(y)
        if x.pop:
            enemies.pop(enemies.index(x))
        x.draw(screen, character.cam_x, character.cam_y, CAM_W, CAM_H)
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
            for x in enemies:
                enemies.pop(enemies.index(x))
            character.alive = True
            character.radius = PLAYER_RADIUS


# Main Game loop
while True:
    if character.alive:
        run()
    else:
        endScreen()
