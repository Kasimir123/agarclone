# Imports
import pygame
from pygame import *
import random
import math

class Enemy:
    def __init__(self, X, Y, RADIUS, COLOR, SPEED, randX, randY):
        self.x = X
        self.y = Y
        self.radius = RADIUS
        self.color = COLOR
        self.speed = SPEED
        self.randX = randX
        self.randY = randY
        self.pop = False
        self.xOffset = int(math.sqrt((math.sqrt( ( (self.radius * self.radius)+(self.radius * self.radius) ) ) - self.radius)/2))
        self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)

    def draw(self, screen, camX, camY, camW, camH):
        if self.x < (camX + camW) + 250 and self.x > camX - 250 and self.y < (camY + camH) + 250 and self.y > camY - 1000:
            pygame.draw.circle(screen, self.color, (self.x - camX,self.y - camY),self.radius)

    def move(self, W, H):
        randCheck = random.randint(0,10)
        if randCheck == 10:
            self.randX = random.randint(0,1)
            if self.randX == 0:
                self.randX = -1
        if randCheck == 5:
            self.randY = random.randint(0,1)
            if self.randY == 0:
                self.randY = -1
        if self.x > 0 and self.x < W:
            self.x += int(self.randX * self.speed)
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif self.x < 0:
            self.x += self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif self.x > W:
            self.x -= self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        if self.y > 0 and self.y < H:
            self.y += int(self.randY * self.speed)
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif self.y < 0:
            self.y += self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif self.y > H:
            self.y -= self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
