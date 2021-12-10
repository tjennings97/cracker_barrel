import pygame

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peg Game")

WHITE = (255,255,255)

FPS = 60 # frams per second we are updating our game at

def draw_window():
    WIN.fill(WHITE)
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