import pygame
import os
import math
import Game
pygame.font.init()

# Window settings
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peg Game")
FPS = 60 # frames per second we are updating our game at

# the following is based on a 5 row triangle. if for some reason, a bigger 
# triangle is desired, the structures in Game.py must be updated in addition 
# to the math done here
BLOCK_HEIGHT = (1/10) * (math.sqrt(3)/2) * WIDTH
BLOCK_WIDTH = (1/22) * WIDTH
TRIANGLE_HEIGHT = math.sqrt(3)/2 * WIDTH
HOLE_RADIUS = 10
HOLE_MAX = 14

# Font sizes
HEADER_FONT = pygame.font.SysFont('comicsans', 40)
PARAGRAPH_FONT = pygame.font.SysFont('comicsans', 20)

# Color codes
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game board import
GAME_BOARD_IMAGE = pygame.image.load(os.path.join('assets', 'wood_triangle.png'))
picture = pygame.transform.scale(GAME_BOARD_IMAGE, (WIDTH, TRIANGLE_HEIGHT)) 

def print_instructions():
    WIN.fill(WHITE)
    header_txt = HEADER_FONT.render("INSTRUCTIONS", 1, RED)
    instruction_1 = PARAGRAPH_FONT.render("USE LEFT AND RIGHT ARROWS TO MOVE POINTER.", 1, RED)
    instruction_2 = PARAGRAPH_FONT.render("USE SPACEBAR TO MAKE SELECTIONS.", 1, RED)
    instruction_3 = PARAGRAPH_FONT.render("RED ARROW IS PEG THAT WILL JUMP.", 1, RED)
    instruction_4 = PARAGRAPH_FONT.render("BLUE ARROW IS WHERE PEG WILL LAND.", 1, RED)
    instruction_5 = PARAGRAPH_FONT.render("CAN ONLY JUMP 1 PEG AT A TIME.", 1, RED)
    instruction_6 = PARAGRAPH_FONT.render("PERFORM JUMPS UNTIL 1 PEG LEFT OR NO MOVES LEFT.", 1, RED)
    enter_txt = PARAGRAPH_FONT.render("HIT [ENTER] TO CONTINUE", 1, RED)
    WIN.blit(header_txt, (WIDTH/2 - header_txt.get_width()/2, 10))
    WIN.blit(instruction_1, (WIDTH/2 - instruction_1.get_width()/2, 60))
    WIN.blit(instruction_2, (WIDTH/2 - instruction_2.get_width()/2, 90))
    WIN.blit(instruction_3, (WIDTH/2 - instruction_3.get_width()/2, 120))
    WIN.blit(instruction_4, (WIDTH/2 - instruction_4.get_width()/2, 150))
    WIN.blit(instruction_5, (WIDTH/2 - instruction_5.get_width()/2, 180))
    WIN.blit(instruction_6, (WIDTH/2 - instruction_6.get_width()/2, 210))
    WIN.blit(enter_txt, (WIDTH/2 - enter_txt.get_width()/2, 270))

def print_results(pegs):
    WIN.fill(WHITE)
    if pegs == 1:
        text = "YOU'RE GENIUS"
    elif pegs == 2:
        text = "YOU'RE PRETTY SMART"
    elif pegs == 3:
        text = "YOU'RE JUST PLAIN DUMB"
    elif pegs > 3:
        text = "YOU'RE JUST PLAIN \"EG-NO-RA-MOOSE\""
    else:
        text = "Something went wrong."
    result_txt = HEADER_FONT.render(text, 1, RED)
    end_txt = PARAGRAPH_FONT.render("PRESS [Q] TO QUIT", 1, RED)
    WIN.blit(result_txt, (WIDTH/2 - result_txt.get_width()/2, HEIGHT/2))
    WIN.blit(end_txt, (WIDTH/2 - end_txt.get_width()/2, HEIGHT/2 + 50))

def draw_board(holes):
    hole = 0
    x_start = WIDTH / 2
    y_dist = 1
    x_dist = 0

    for row in range(0,5):
        x_row = row
        while x_row != -1:
            x = x_start + (x_dist * BLOCK_WIDTH)
            y = y_dist * BLOCK_HEIGHT
            holes[hole].coordinates = (x,y)
            pygame.draw.circle(WIN, holes[hole].color, holes[hole].coordinates, HOLE_RADIUS)
            pygame.draw.circle(WIN, BLACK, holes[hole].coordinates, HOLE_RADIUS, width=2)
            hole += 1
            x_dist += 4
            x_row -= 1
        x_start = x_start - 2 * BLOCK_WIDTH
        x_dist = 0
        y_dist += 2

def draw_pointer(x, y, color):
    point1 = (x, y + (HOLE_RADIUS * 2))
    point2 = (x - HOLE_RADIUS, y + (HOLE_RADIUS * 3))
    point3 = (x + HOLE_RADIUS, y + (HOLE_RADIUS * 3))
    pygame.draw.polygon(WIN, color, [point1, point2, point3])

def print_message(message):
    message_txt = PARAGRAPH_FONT.render(message, 1, RED)
    WIN.blit(message_txt, (WIDTH/2 - message_txt.get_width()/2, TRIANGLE_HEIGHT + 20))
        
def draw_window(g, instructions, message):
    if instructions is True and g.board.are_moves() is True:
        WIN.fill(WHITE)
        WIN.blit(picture, (0,0))
        print_message(message)
        draw_board(g.board.holes)
        draw_pointer(g.board.holes[g.pointer].coordinates[0], g.board.holes[g.pointer].coordinates[1], g.pointer_color)
    else:
        print_instructions()

    if(g.board.are_moves() is False):
        print_results(g.board.peg_count)

    pygame.display.update()

def move_pointer(pointer_location, direction):
    if direction == "right":
        if pointer_location < HOLE_MAX:
            pointer_location += 1
        else:
            pointer_location = 0
    if direction == "left":
        if pointer_location > 0:
            pointer_location -= 1
        else:
            pointer_location = HOLE_MAX
    return pointer_location

def main():

    g = Game.Game()

    clock = pygame.time.Clock()
    run = True
    starting_hole = 0
    pointer_flag = True
    instructions = False
    message = ""
    
    while run:
        clock.tick(FPS) # control speed of while loop. run 60 FPS per second
        for event in pygame.event.get(): # get a list of all events and looping through them
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and instructions is False:
                    instructions = True

                if event.key == pygame.K_RIGHT and instructions is True:
                    g.pointer = move_pointer(g.pointer, "right")
                    message = ""

                if event.key == pygame.K_LEFT and instructions is True:
                    g.pointer = move_pointer(g.pointer, "left")
                    message = ""

                if event.key == pygame.K_SPACE and instructions is True:
                    if pointer_flag is True:
                        pointer_flag = False
                        g.pointer_color = BLUE
                        starting_hole = g.pointer
                    else:
                        pointer_flag = True
                        g.pointer_color = RED
                        landing_hole = g.pointer
                        jumped_hole = g.board.check_move(starting_hole, landing_hole)
                        if jumped_hole == -1:
                            message = "This is an invalid move. Please try again."
                        else:
                            g.jump(starting_hole, jumped_hole, landing_hole)                
                
                if event.key == pygame.K_q:
                    run = False

        draw_window(g, instructions, message)
        
    pygame.quit()

if __name__ == "__main__":
    main()