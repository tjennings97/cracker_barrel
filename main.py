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
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

FPS = 60 # frames per second we are updating our game at

GAME_BOARD_IMAGE = pygame.image.load(os.path.join('assets', 'wood_triangle.png'))
picture = pygame.transform.scale(GAME_BOARD_IMAGE, (WIDTH, TRIANGLE_HEIGHT))
'''
def draw_board(board):
    holes = board.holes
    hole = 0
    x_middle = (1/2) * WIDTH
    y_dist = 1

    for row in range(0,5):
        x_row = row
        if row % 2 == 0:
            x_toggle = True
            x_dist = 0
        else:
            x_toggle = False
            x_dist = 2

        while x_row != -1:
            if x_toggle is True:
                x = x_middle + (x_dist * BLOCK_WIDTH)
                x_dist = x_dist + 4
            else:
                x = x_middle - (x_dist * BLOCK_WIDTH)
                
            x_toggle = not x_toggle
            x_row = x_row - 1
            y = y_dist * BLOCK_HEIGHT
            coordinates = (x,y)
            if hole != 0:
                pygame.draw.circle(WIN, holes[hole].color, coordinates, HOLE_RADIUS)
                pygame.draw.circle(WIN, BLACK, coordinates, HOLE_RADIUS, width=1)
            else:
                pygame.draw.circle(WIN, BLACK, coordinates, HOLE_RADIUS)
            holes[hole].coordinates = coordinates
            hole += 1
        y_dist = y_dist + 2
'''  

def draw_board(board):
    holes = board.holes
    hole = 0
    x_start = (1/2) * WIDTH
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
            if hole != 0:
                pygame.draw.circle(WIN, holes[hole].color, coordinates, HOLE_RADIUS)
                pygame.draw.circle(WIN, BLACK, coordinates, HOLE_RADIUS, width=1)
            else:
                pygame.draw.circle(WIN, BLACK, coordinates, HOLE_RADIUS)
            holes[hole].coordinates = coordinates
            hole += 1
        x_start = x_start - 2 * BLOCK_WIDTH
        x_dist = 0
        y_dist = y_dist + 2



def draw_pointer(x, y):
    point1 = (x, y + HOLE_RADIUS + 10)
    point2 = (x -10, y + HOLE_RADIUS + 20)
    point3 = (x +10, y + HOLE_RADIUS + 20)
    pygame.draw.polygon(WIN, RED, [point1, point2, point3])
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
    #game = Game.Game()
    #game.print_instructions()
    #game.play_game()

    g = Game.Game()

    clock = pygame.time.Clock()
    run = True
    pointer_location = 0
    pressed = False
    
    while run:
        clock.tick(FPS) # control speed of while loop. run 60 FPS per second
        for event in pygame.event.get(): # get a list of all events and looping through them
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not pressed:
                    pointer_location = move_pointer(pointer_location, "right")
                    pressed = True
                if event.key == pygame.K_LEFT and not pressed:
                    pointer_location = move_pointer(pointer_location, "left")
                    pressed = True
            if event.type == pygame.KEYUP:
                pressed = False

        draw_window(g.board)
        draw_pointer(g.board.holes[pointer_location].coordinates[0], g.board.holes[pointer_location].coordinates[1])
        
    pygame.quit()

if __name__ == "__main__":
    main()