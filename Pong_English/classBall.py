# Recreation of the classic game Pong using Python and the pygame library
# Author: Claudio Kamoda
# Date: 08/07/2019
# Class ball

# library importation
import pygame
import random


class ball(object):
    # constructor
    def __init__(self, size):
        self.size = size                              # size
        self.vel = 2                                # movement speed
        self.coord = [self.ballX(), self.ballY()]   # tuple with coordinates
        self.move = self.mov_ini()                  # movement direction

    def ballX(self):
        return random.randint(200, 290)             # assign a random starting position in x axis

    def ballY(self):
        return random.randint(0, 290)               # assign a random starting position in y axis

    def mov_ini(self):                      # assign a random starting direction in x
        dir = random.randint(1, 4)

        if dir == 1:
            mov = [self.vel, self.vel]      # right-down (south-east)
        elif dir == 2:
            mov = [-self.vel, self.vel]     # left-down (south-west)
        elif dir == 3:
            mov = [self.vel, -self.vel]     # right-up (north-east)
        else:
            mov = [-self.vel, -self.vel]    # left-up (north-west)

        return mov

    # function to draw the ball
    def draw_ball(self, jan):
        pygame.draw.rect(jan, (255, 255, 255), (self.coord[0], self.coord[1], self.size, self.size))
