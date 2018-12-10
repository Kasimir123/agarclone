import math
import random
import pygame
from pygame import Rect


# We should think about making character and Enemy both
# children of a class.
class Player:
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
        self.x_offset = int(math.sqrt(
            (math.sqrt(self.radius ** 2 + self.radius ** 2) - self.radius)
            / 2))
        self.hitbox = Rect(self.x - self.x_offset, self.y - self.x_offset,
                           self.radius * 2, self.radius * 2)


    def draw(self, screen, cam_x, cam_y, cam_w, cam_h):
        '''Temporary docstring
        '''
        # What in the hell does 250 and 1000 mean?
        if self.x < (cam_x + cam_w) + 250 \
           and self.x > cam_x - 250 \
           and self.y < (cam_y + cam_h) + 250 \
           and self.y > cam_y - 1000:
            pygame.draw.circle(screen, self.color,
                               (self.x - cam_x, self.y - cam_y),
                               self.radius)


    def move(self, w, h):
        '''Temporary docstring
        '''
        # The variables w and h are really undescriptive. What do they mean?

        # This would be more clear as a random float
        rand_check = random.randint(0, 10)
        # We could split the simple creating positive or negative number
        # to be a separate method, or maybe just find something that natively
        # does that
        if rand_check == 10:
            self.rand_x = random.randint(0, 1)
            if self.rand_x == 0:
                self.rand_x = -1
        if rand_check == 5:
            self.rand_y = random.randint(0, 1)
            if self.rand_y == 0:
                self.rand_y = -1

        # This is incredibly repetitive and ugly. Is there any way we
        # could write this cleaner? Most of what we're doing is slightly
        # changing a single number
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

        self.hitbox = Rect(self.x - self.x_offset, self.y - self.x_offset,
                           self.radius * 2, self.radius * 2)
