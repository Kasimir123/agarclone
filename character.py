# Imports
import pygame
from pygame import *
import math

class Char:
    def __init__(self, camW, camH, W, H, COLOR, radius):
        self.alive = True
        self.x = camW // 2
        self.y = camH // 2
        self.radius = 10
        self.color = COLOR
        self.speed = 10
        self.camX = 0
        self.camY = 0
        self.xOffset = int(math.sqrt((math.sqrt( ( (self.radius * self.radius)+(self.radius * self.radius) ) ) - self.radius)/2))
        self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x -self.camX,self.y -self.camY),self.radius)

    def update(self,direction):
        if direction == "UP":
            self.camY -= self.speed
            self.y -= self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif direction == "DOWN":
            self.camY += self.speed
            self.y += self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif direction == "LEFT":
            self.camX -= self.speed
            self.x -= self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
        elif direction == "RIGHT":
            self.camX += self.speed
            self.x += self.speed
            self.hitbox = Rect(self.x - self.xOffset, self.y -  self.xOffset, self.radius * 2, self.radius * 2)
    
    def checkCollide(self, x):
        if self.hitbox.colliderect(x.hitbox):
            if self.radius > x.radius:
                self.radius += x.radius // 5
                x.pop = True
            else:
                self.alive = False