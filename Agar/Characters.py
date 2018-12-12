import math
import random
import pygame
from pygame import Rect

# Constants:
POINT_MULTIPLY = 100
POINT_PERCENTAGE_TAKEN_BY_PLAYER = .25
POINT_PERCENTAGE_TAKEN_BY_ENEMY = .1
POINTS_FOR_KILL = 200
PERCENTAGE_OF_POINTS_GAINED_BY_PLAYER = .25
PERCENTAGE_OF_POINTS_GAINED_BY_ENEMY = .25


class Player:
    '''Temporary docstring
    '''

    def __init__(self, cam_w, cam_h, w, h, color, radius, speed):
        '''Temporary docstring
        '''
        self.alive = True
        self.x = cam_w // 2
        self.y = cam_h // 2
        self.radius = radius
        self.color = color
        self.speed = speed
        self.cam_x = 0
        self.cam_y = 0
        self.points = self.radius * POINT_MULTIPLY


    def draw(self, screen):
        '''Temporary docstring
        '''
        pygame.draw.circle(screen, self.color,
                           (self.x - self.cam_x, self.y - self.cam_y),
                           self.radius)

    def up(self):
        self.cam_y -= self.speed
        self.y -= self.speed
    
    def down(self):
        self.cam_y += self.speed
        self.y += self.speed

    def left(self):
        self.cam_x -= self.speed
        self.x -= self.speed

    def right(self):
        self.cam_x += self.speed
        self.x += self.speed


    def update(self,direction):
        '''Temporary docstring
        '''
        eval("self." + direction)
    
    def checkCollideDistance(self, x):
        distance = math.sqrt(((self.x - x.x) ** 2) + ((self.y - x.y) ** 2))
        if distance < 0:
            distance = distance * -1
        if distance <= self.radius + x.radius:
            return True
        else:
            return False


    def checkCollide(self, x):
        '''Temporary docstring
        '''
        if self.checkCollideDistance(x):
            if self.points > x.points:
                if  x.points <= POINTS_FOR_KILL:
                    self.points += x.points
                    x.points -= x.points
                else:
                    self.points += x.points * POINT_PERCENTAGE_TAKEN_BY_PLAYER * PERCENTAGE_OF_POINTS_GAINED_BY_PLAYER
                    x.points -= x.points * POINT_PERCENTAGE_TAKEN_BY_PLAYER
                if x.points <= 0:
                    x.pop = True
            else:
                if self.points <= POINTS_FOR_KILL:
                    x.points += self.points
                    self.points -= self.points
                else:
                    x.points += self.points * POINT_PERCENTAGE_TAKEN_BY_ENEMY * PERCENTAGE_OF_POINTS_GAINED_BY_ENEMY
                    self.points -= self.points * POINT_PERCENTAGE_TAKEN_BY_ENEMY
                if self.points <= 0:
                    self.alive = False
            self.radius = int(self.points / POINT_MULTIPLY)
            x.radius = int(x.points / POINT_MULTIPLY)


class Enemy:
    '''Temporary docstring
    '''

    def __init__(self, x, y, radius, color, speed, rand_x, rand_y):
        '''Temporary docstring
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.rand_x = rand_x
        self.rand_y = rand_y
        self.pop = False
        self.points = self.radius * POINT_MULTIPLY


    def draw(self, screen, cam_x, cam_y, cam_w, cam_h):
        '''Temporary docstring
        '''
        if self.x < (cam_x + cam_w) \
           and self.x > cam_x \
           and self.y < (cam_y + cam_h) \
           and self.y > cam_y:
            pygame.draw.circle(screen, self.color,
                               (self.x - cam_x, self.y - cam_y),
                               self.radius)


    def move(self, w, h):
        '''Temporary docstring
        '''
        rand_check = random.randint(0, 10)
        if rand_check == 10:
            self.rand_x = random.randint(0, 1)
            if self.rand_x == 0:
                self.rand_x = -1
        if rand_check == 5:
            self.rand_y = random.randint(0, 1)
            if self.rand_y == 0:
                self.rand_y = -1

        if self.x > 0 and self.x < w:
            self.x += int(self.rand_x * self.speed)
        elif self.x < 0:
            self.x += self.speed
        elif self.x > w:
            self.x -= self.speed
        if self.y > 0 and self.y < h:
            self.y += int(self.rand_y * self.speed)
        elif self.y < 0:
            self.y += self.speed
        elif self.y > h:
            self.y -= self.speed
    
    def checkCollideDistance(self, x):
        distance = math.sqrt(((self.x - x.x) ** 2) + ((self.y - x.y) ** 2))
        if distance < 0:
            distance = distance * -1
        if distance <= self.radius + x.radius:
            return True
        else:
            return False


    def checkCollide(self, x):
        '''Temporary docstring
        '''
        if self.checkCollideDistance(x):
            if self.points > x.points:
                if  x.points <= POINTS_FOR_KILL:
                    self.points += x.points
                    x.points -= x.points
                else:
                    self.points += x.points * POINT_PERCENTAGE_TAKEN_BY_ENEMY  * PERCENTAGE_OF_POINTS_GAINED_BY_ENEMY
                    x.points -= x.points * POINT_PERCENTAGE_TAKEN_BY_ENEMY
                if x.points <= 0:
                    x.pop = True
            elif self.points == x.points:
                pass
            else:
                if self.points <= POINTS_FOR_KILL:
                    x.points += self.points
                    self.points -= self.points
                else:
                    x.points += self.points * POINT_PERCENTAGE_TAKEN_BY_ENEMY  * PERCENTAGE_OF_POINTS_GAINED_BY_ENEMY
                    self.points -= self.points * POINT_PERCENTAGE_TAKEN_BY_ENEMY
                if self.points <= 0:
                    self.alive = False
            self.radius = int(self.points / POINT_MULTIPLY)
            x.radius = int(x.points / POINT_MULTIPLY)