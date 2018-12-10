import math
import pygame
from pygame import Rect


# We should think about making character and Enemy both
# children of a class.
class Character:
    '''Temporary docstring
    '''

    def __init__(self, cam_w, cam_h, w, h, color, radius):
        '''Temporary docstring
        '''
        # We should set all these magic numbers to constants
        self.alive = True
        self.x = cam_w // 2
        self.y = cam_h // 2
        self.radius = 10
        self.color = color
        self.speed = 10
        self.cam_x = 0
        self.cam_y = 0
        self.x_offset = int(math.sqrt(
            (math.sqrt(self.radius ** 2 + self.radius ** 2) - self.radius)
            / 2))
        self.hitbox = Rect(self.x - self.x_offset, self.y - self.x_offset,
                           self.radius * 2, self.radius * 2)


    def draw(self, screen):
        '''Temporary docstring
        '''
        pygame.draw.circle(screen, self.color,
                           (self.x - self.cam_x, self.y - self.cam_y),
                           self.radius)


    def update(self,direction):
        '''Temporary docstring
        '''
        # Is there a way we could improve this? Switch statements?
        if direction == "UP":
            self.cam_y -= self.speed
            self.y -= self.speed
        elif direction == "DOWN":
            self.cam_y += self.speed
            self.y += self.speed
        elif direction == "LEFT":
            self.cam_x -= self.speed
            self.x -= self.speed
        elif direction == "RIGHT":
            self.cam_x += self.speed
            self.x += self.speed
        self.hitbox = Rect(self.x - self.x_offset, self.y - self.x_offset,
                           self.radius * 2, self.radius * 2)


    def checkCollide(self, x):
        '''Temporary docstring
        '''
        if self.hitbox.colliderect(x.hitbox):
            if self.radius > x.radius:
                self.radius += x.radius // 5
                x.pop = True
            else:
                self.alive = False
