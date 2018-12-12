import random
import pygame
from pygame import *
from characters import *

# Init pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Defines Constants
# Width and Height of Screen
W, H = 1000, 500
# Frames Per Second
FPS = 30
# Check if the game is running or not
IS_RUNNING = True
IS_STARTED = False

# Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)

# Paddle Constants
PLAYER_ONE_X = 2
PLAYER_TWO_X = W - PADDLE_WIDTH - 2
PLAYER_Y = H // 2

# Start button dimensions
START_X = W // 4
START_Y = W // 10
WIDTH = W - 2 * START_X
HEIGHT = 75

# Create button squares
ONE = Rect(START_X, START_Y, WIDTH, HEIGHT)
TWO = Rect(START_X, START_Y + (HEIGHT * 2), WIDTH, HEIGHT)

# Direction Constants
UP = 'up()'
DOWN = 'down()'

# Open game window
size = (W, H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
background = pygame.surface.Surface(size).convert()
background.fill(BLACK)

# Create fonts
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Check for input
def input():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_one.update(UP, ball)
    if keys[pygame.K_DOWN]:
        player_one.update(DOWN, ball)
    if keys[pygame.K_w]:
        player_two.update(UP, ball)
    if keys[pygame.K_s]:
        player_two.update(DOWN, ball)

# Main Loop Method
def run():
    time_passed = clock.tick(FPS) / 1000.0
    input()
    drawScreen()

# Drawing method
def drawScreen():
    screen.blit(background, (0 ,0))
    player_one.draw(screen)
    player_two.draw(screen)
    player_one_score = myfont.render('Score: ' + str(player_one.score), False, WHITE)
    player_two_score = myfont.render('Score: ' + str(player_two.score), False, WHITE)
    screen.blit(player_one_score, (5, 5))
    screen.blit(player_two_score, (W - 125, 5))
    ball.update(player_one, player_two)
    player_two.update(False, ball)
    ball.draw(screen)
    pygame.display.update()

def createPlayers(number):
    global IS_STARTED, player_one, player_two, ball
    if number == 2:
        player_one = Paddle(PLAYER_ONE_X, PLAYER_Y, True, WHITE, H)
        player_two = Paddle(PLAYER_TWO_X, PLAYER_Y, True, WHITE, H)
    else:
        player_one = Paddle(PLAYER_ONE_X, PLAYER_Y, True, WHITE, H)
        player_two = Paddle(PLAYER_TWO_X, PLAYER_Y, False, WHITE, H)
    ball = Ball((W // 2), (H // 2), WHITE)
    IS_STARTED = True
    


def startScreen():
    screen.blit(background, (0 ,0))
    pygame.draw.rect(screen, WHITE, ONE)
    pygame.draw.rect(screen, WHITE, TWO)
    one_player = myfont.render('One Player', False, BLACK)
    two_players = myfont.render('Two Players', False, BLACK)
    screen.blit(one_player, (START_X + (WIDTH // 3), START_Y + (HEIGHT // 4)))
    screen.blit(two_players, (START_X + (WIDTH // 3), START_Y + (HEIGHT * 2) + (HEIGHT // 4)))
    pygame.display.update()
    input()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if pressed1:
        pos = pygame.mouse.get_pos()
        if ONE.collidepoint(pos):
            createPlayers(1)
        elif TWO.collidepoint(pos):
            createPlayers(2)


# Main Loop
while IS_RUNNING:
    if IS_STARTED:
        run()
    else: 
        startScreen()