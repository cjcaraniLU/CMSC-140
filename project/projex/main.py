import pygame as pg
import sys

pg.init()
#constants
width = 600
height = 600
line_width = 10
board_rows = 3
board_column = 3
#markers
circle_radius = 60
circle_width = 15

cross_width = 25
space = 55

#colors
black = (0, 0, 0)
background = (200,150,120)
piece_color = (255, 20, 100)

screen = pg.display.set_mode((width, height)) #create screen
pg.display.set_caption("Tic-Tac-Toe") #label top of pop up
screen.fill(background) #set background

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def mark_spot(row, col, player):
    board[(row * 3)+ col] = player

def is_available(row, col):
    return board[(row * 3)+ col] == " "

def is_full():
    for i in board:
        if i == " ":
            return False
    return True



def draw_lines(): #create lines
    pg.draw.line(screen, black, (0,200), (600, 200), line_width)
    pg.draw.line(screen, black, (0,400), (600, 400), line_width)
    pg.draw.line(screen, black, (200,0), (200, 600), line_width)
    pg.draw.line(screen, black, (400,0), (400, 600), line_width)
draw_lines()

def draw_xo():
    for i in range(len(board)):
        col = i%3
        row = i//3
        if board[i] == "o":
            pg.draw.circle(screen, piece_color, (int(col * 200 + 100),int(row * 200 + 100)), circle_radius, circle_width)
        elif board[i] == "x":
            pg.draw.line(screen, piece_color, (col * 200 + space , row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 +space), cross_width)
            pg.draw.line(screen, piece_color, (col * 200 + space , row * 200 + space), (col * 200 + 200 - space, row * 200 + 200 - space), cross_width)            

player = "o"
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            col_click = int(mouse_x//200)
            row_click = int(mouse_y// 200)


            if is_available(row_click, col_click):
                if player == "o":
                    mark_spot(row_click, col_click, "o")
                    player = "x"
                elif player == "x":
                    mark_spot(row_click, col_click, "x")
                    player = "o"

            draw_xo()
    pg.display.update()