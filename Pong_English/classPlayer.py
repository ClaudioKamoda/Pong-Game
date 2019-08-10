# Recreation of the classic game Pong using Python and the pygame library
# Author: Claudio Kamoda
# Date: 08/07/2019
# Class player

import pygame   # library importation


class player(object):
    # constructor
    def __init__(self, x, y, height, width):
        self.x = x                          # x coordinate
        self.y = y                          # y coordinate
        self.height = height                # height
        self.width = width                  # width
        self.vel = 5                        # speed of movement
        self.score = 0                      # score

    # function to draw the bar
    def draw_player(self, jan):
        pygame.draw.rect(jan, (255, 255, 255), (self.x, self.y, self.width, self.height))
