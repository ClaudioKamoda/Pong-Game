# Recreation of the classic game Pong using Python and the pygame library
# Author: Claudio Kamoda
# Date: 08/07/2019
# Main file

# modules and library importation
import pygame
import functions as f
import classPlayer as cp
import classBall as cb


pygame.init()   # library initialing

# window's height and width in pixels
WIND_WIDTH = 500
WIND_HEIGHT = 300

# window initialization
wind = pygame.display.set_mode((WIND_WIDTH, WIND_HEIGHT))

pygame.display.set_caption("Pong")                  # Upper screen caption
font = pygame.font.SysFont('zig', 30, True)         # object that receives the score's font with size 30 bold
clock = pygame.time.Clock()                         # clock
midLine = pygame.image.load('mid line.png')         # mid screen line

# object instantiation (check classes)
left_P = cp.player(20, 135, 30, 10)                 # left bar
right_P = cp.player(470, 135, 30, 10)               # right bar
ball = cb.ball(10)                                  # ball


# function that gathers all the screen draw operations
def drawScreen():
    wind.fill((0, 0, 0))                # fills the screen in black to erase the last iteration
    score1 = font.render(str(left_P.score), 1, (255, 255, 255))     # left score
    score2 = font.render(str(right_P.score), 1, (255, 255, 255))    # right score
    left_P.draw_player(wind)            # draw the left bar
    right_P.draw_player(wind)           # draw the left bar
    ball.draw_ball(wind)                # draw the ball
    wind.blit(midLine, (245, 0))        # draw the mid line
    wind.blit(score1, (180, 20))        # draw the left score
    wind.blit(score2, (290, 20))        # draw the right score
    pygame.display.update()             # updates the screen


# main loop
run = True
while run:
    clock.tick(30)  # 30 fps
    
    for event in pygame.event.get():        # checks if the player closed the screen
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()         # read the keyboard inputs

    # left player commands
    if keys[pygame.K_w] and left_P.y != 0:
        left_P.y -= left_P.vel
    if keys[pygame.K_s] and left_P.y != (WIND_HEIGHT - left_P.height):
        left_P.y += left_P.vel

    # right player commands
    if keys[pygame.K_UP] and right_P.y != 0:
        right_P.y -= right_P.vel
    if keys[pygame.K_DOWN] and right_P.y != (WIND_HEIGHT - right_P.height):
        right_P.y += right_P.vel

    f.movement(ball, left_P, right_P)         # checks the ball movement
    if f.score(ball, left_P, right_P):     # checks score
        ball = cb.ball(10)
    drawScreen()                               # draw screen after inputs

pygame.quit()       # finish the game
