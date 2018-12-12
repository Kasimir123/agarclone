import math as m
import random
import pygame
from pygame import *

# Constants
PADDLE_SPEED = 10
PADDLE_WIDTH = 30
PADDLE_HEIGHT = 100
BALL_SPEED = 10
BALL_RADIUS = 5
# -1 for left or up 1 for right or down
BALL_DIRECTION = -1

class Paddle:
    def __init__(self, x, y, player, color, screen_height):
        self.x = x
        self.y = y
        self.is_player = player
        self.speed = PADDLE_SPEED
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = color
        self.screen_height = screen_height
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def up(self):
        if self.y > 0:
            self.y -= self.speed

    def down(self):
        if self.y + self.height < self.screen_height:
            self.y += self.speed

    def update(self, direction, ball):
        if self.is_player and direction != False:
            eval("self." + direction)
        elif self.is_player == False:
            if self.y < ball.y:
                self.down()
            elif self.y > ball.y:
                self.up()

class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.reset_x = x
        self.reset_y = y
        self.color = color
        self.speed = BALL_SPEED
        self.radius = BALL_RADIUS
        self.vertical_direction = BALL_DIRECTION
        self.horizontal_direction = BALL_DIRECTION

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def distance(self, x, y):
        distance = m.sqrt(((self.x - x) ** 2) + ((self.y - y) ** 2))
        return abs(distance)

    def checkForPaddle(self, paddle):
        if self.y >= paddle.y and self.y <= paddle.y + paddle.height:
            return True
        else:
            return False

    def checkTopCollision(self):
        if self.distance(self.x, 0) <= self.radius:
            return True
        else:
            return False

    def checkBottomCollision(self, player_one):
        if self.distance(self.x, player_one.screen_height) <= self.radius:
            return True
        else:
            return False

    def leftPaddleCollision(self, player_one, player_two):
        if self.distance(player_one.x + player_one.width, self.y) <= self.radius:
            if self.checkForPaddle(player_one):
                return True
            else:
                self.x = self.reset_x
                self.y = self.reset_y
                player_two.score += 1
        else:
            return False

    def rightPaddleCollision(self, player_one, player_two):
        if self.distance(player_two.x, self.y) <= self.radius:
            if self.checkForPaddle(player_two):
                return True
            else:
                self.x = self.reset_x
                self.y = self.reset_y
                player_one.score += 1
        else:
            return False

    def update(self, player_one, player_two):
        if self.checkTopCollision() or self.checkBottomCollision(player_one):
            self.vertical_direction = self.vertical_direction * -1
        if self.leftPaddleCollision(player_one, player_two) or self.rightPaddleCollision(player_one, player_two):
            self.horizontal_direction = self.horizontal_direction * -1

        self.x += self.speed * self.horizontal_direction
        self.y += self.speed * self.vertical_direction