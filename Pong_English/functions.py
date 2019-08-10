# Recreation of the classic game Pong using Python and the pygame library
# Author: Claudio Kamoda
# Date: 08/07/2019
# Basic functions


# function to decide the movement of the ball
def movement(b, j1, j2):
    # checks collision with the window margin
    if b.coord[1] <= 0 or b.coord[1] >= 290:
        b.move[1] *= -1                         # reverse the ball's direction in the y axis

    # checks ball-bar collision
    if (b.coord[0] - j1.x <= j1.width and j1.y + j1.height > b.coord[1] > j1.y - b.size) \
            or (j2.x - b.coord[0] <= b.size and j2.y + j2.height > b.coord[1] > j2.y - b.size):
        b.move[0] *= -1                         # reverse the ball's direction in the x axis

    b.coord[0] += b.move[0]
    b.coord[1] += b.move[1]


# checks if the ball has gone through the side margin
def score(b, j1, j2):
    if b.coord[0] < -20:
        j2.score += 1
        return 1
    if b.coord[0] > 500:
        j1.score += 1
        return 1

    return 0
