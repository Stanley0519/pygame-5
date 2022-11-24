import pygame
import numpy as np
WHITE = (255,255,255)
BLACK = (0,0,0)
BG_COLOR = (100,180,250)

BOARD_LEN = 5
DIS_TO_BOUNDARY = 200
CHESS_SQUARE_LEN = 200
screen_len = BOARD_LEN+CHESS_SQUARE_LEN+2*DIS_TO_BOUNDARY

#checkerboard setup
WHITE_BOARDER_IMG = pygame.image.load("white_boarder.png")
WHITE_BOARDER_IMG = pygame.transform.scale(WHITE_BOARDER_IMG,(CHESS_SQUARE_LEN,CHESS_SQUARE_LEN))

pygame.init()
screen = pygame.display.set_mode((screen_len,screen_len))
screen.fill(BG_COLOR)
pygame.display.flip()

def init_game():
    global is_black,board_matrix
    is_black = True
    board_matrix = np.zeros((BOARD_LEN,BOARD_LEN),dtype = int)

def matrix_pos_to_screen_pos(row,col):
    return (DIS_TO_BOUNDARY+col*CHESS_SQUARE_LEN,DIS_TO_BOUNDARY+row*CHESS_SQUARE_LEN)


def draw_checkerboard():
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            screen_pos = matrix_pos_to_screen_pos(i,j)
            screen.blit(WHITE_BOARDER_IMG,screen_pos)

running = True
init_game()
print(is_black,board_matrix)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False