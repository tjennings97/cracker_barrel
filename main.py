import pygame
import os
import math
import Game

WIDTH, HEIGHT = 600, 600
BLOCK_HEIGHT = (1/10) * (math.sqrt(3)/2) * WIDTH
BLOCK_WIDTH = (1/22) * WIDTH
TRIANGLE_HEIGHT = math.sqrt(3)/2 * WIDTH
HOLE_RADIUS = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peg Game")

# color RGB
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60 # frames per second we are updating our game at

GAME_BOARD_IMAGE = pygame.image.load(os.path.join('assets', 'wood_triangle.png'))
picture = pygame.transform.scale(GAME_BOARD_IMAGE, (WIDTH, TRIANGLE_HEIGHT)) 

def draw_board(holes):
    hole = 0
    x_start = WIDTH / 2
    y_dist = 1
    x_dist = 0

    for row in range(0,5):
        x_row = row
        while x_row != -1:
            x = x_start + (x_dist * BLOCK_WIDTH)
            x_row = x_row -1
            y = y_dist * BLOCK_HEIGHT
            x_dist = x_dist + 4
            coordinates = (x,y)
            pygame.draw.circle(WIN, holes[hole].color, coordinates, HOLE_RADIUS)
            pygame.draw.circle(WIN, BLACK, coordinates, HOLE_RADIUS, width=2)
            holes[hole].coordinates = coordinates
            hole += 1
        x_start = x_start - 2 * BLOCK_WIDTH
        x_dist = 0
        y_dist = y_dist + 2

def draw_pointer(x, y, color):
    point1 = (x, y + HOLE_RADIUS + 10)
    point2 = (x -10, y + HOLE_RADIUS + 20)
    point3 = (x +10, y + HOLE_RADIUS + 20)
    pygame.draw.polygon(WIN, color, [point1, point2, point3])
    pygame.display.update()
        
def draw_window(board):
    WIN.fill(WHITE)
    WIN.blit(picture, (0,0))
    draw_board(board)
    pygame.display.update()

def move_pointer(pointer_location, direction):
    if direction == "right":
        if pointer_location < 14:
            pointer_location += 1
        else:
            pointer_location = 0
    if direction == "left":
        if pointer_location > 0:
            pointer_location -= 1
        else:
            pointer_location = 14
    return pointer_location

def main():

    g = Game.Game()

    clock = pygame.time.Clock()
    run = True
    pointer_location = 0
    color = RED
    pointer_flag = True
    starting_hole = 0
    
    while run:
        clock.tick(FPS) # control speed of while loop. run 60 FPS per second
        for event in pygame.event.get(): # get a list of all events and looping through them
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pointer_location = move_pointer(pointer_location, "right")
                if event.key == pygame.K_LEFT:
                    pointer_location = move_pointer(pointer_location, "left")
                if event.key == pygame.K_SPACE:
                    if pointer_flag is True:
                        pointer_flag = False
                        color = BLUE
                        starting_hole = pointer_location
                    else:
                        pointer_flag = True
                        color = RED
                        landing_hole = pointer_location
                        jumped_hole = g.board.check_move(starting_hole, landing_hole)
                        if jumped_hole == -1:
                            print("This is an invalid move. Please try again.")
                        else:
                            g.jump(starting_hole, jumped_hole, landing_hole)
                        run = g.board.are_moves()

        draw_window(g.board.holes)
        draw_pointer(g.board.holes[pointer_location].coordinates[0], g.board.holes[pointer_location].coordinates[1], color)
        
    pygame.quit()

if __name__ == "__main__":
    main()