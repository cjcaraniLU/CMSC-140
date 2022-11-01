import pygame
import sys
import numpy as np

pygame.init()
#constants
width = 600
height = 600
line_width = 10
board_rows = 3
board_column = 3
black = (0, 0, 0)
background = (200,150,120)

screen = pygame.display.set_mode((width, height)) #create screen
pygame.display.set_caption("Tic-Tac-Toe") #label top of pop up
screen.fill(background) #set background

board = np.zeros((board_rows, board_column))

def mark_spot(row, col, player):
    

def draw_lines(): #create lines
    pygame.draw.line(screen, black, (0,200), (600, 200), line_width)
    pygame.draw.line(screen, black, (0,400), (600, 400), line_width)
    pygame.draw.line(screen, black, (200,0), (200, 600), line_width)
    pygame.draw.line(screen, black, (400,0), (400, 600), line_width)
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()