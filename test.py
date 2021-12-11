import pygame
import os
import math

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peg Game")

WHITE = (255,255,255)

FPS = 60 # frams per second we are updating our game at

GAME_BOARD_IMAGE = pygame.image.load(os.path.join('assets', 'wood_triangle.png'))
picture = pygame.transform.scale(GAME_BOARD_IMAGE, (WIDTH, (math.sqrt(3)/2) * WIDTH))
rect = picture.get_rect()

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(picture, (0,0))
    block_height = (1/10) * (math.sqrt(3)/2) * WIDTH
    block_width = (1/22) * WIDTH
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
                x = x_middle + (x_dist * block_width)
                x_dist = x_dist + 4
            else:
                x = x_middle - (x_dist * block_width)
            x_toggle = not x_toggle
            x_row = x_row - 1
            y = y_dist * block_height
            coordinates = (x,y)
            pygame.draw.circle(WIN, (0,0,0), coordinates, 10)
        y_dist = y_dist + 2


    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # control speed of while loop. run 60 FPS per second
        for event in pygame.event.get(): # get a list of all events and looping through them
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
        
    pygame.quit()

if __name__ == "__main__":
    main()