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
piece_color = (255, 200, 0)
win_line_color = (255, 80, 30)

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
            

def check_board(player):
    for row in range(board_rows):
        if(board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2] == player):
            draw_horizontal(row)
            return 1

    for column in range(board_column):
        if(board[column] == board[column + 3] == board[column +6] == player):
            draw_vertical(column)
            return 1
    
    #check diaganol
    if(board[0]== board[4] == board[8] == player):
        draw_r_to_l()
        return 1 
    
    if(board[2] == board[4] == board[6] == player):
        draw_l_to_r()
        return 1
    return -1

def draw_horizontal(row):
    position = row * 200 + 100
    pg.draw.line(screen, win_line_color, (15, position), (width - 15, position), 15 )

def draw_vertical(column):
    position = column * 200 + 100
    pg.draw.line(screen, win_line_color, (position, 15), (position, height - 15), 15 )

def draw_l_to_r():
    pg.draw.line(screen, win_line_color, (15, height - 15), (width -15, 15), 15)

def draw_r_to_l():
    pg.draw.line(screen, win_line_color, (15,15), (width -15, height -15), 15)


player = "o"
isWinner = -1
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and isWinner != 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            col_click = int(mouse_x//200)
            row_click = int(mouse_y// 200)


            if is_available(row_click, col_click):
                if player == "o":
                    mark_spot(row_click, col_click, "o")
                    #new b
                    isWinner = check_board(player)
                    player = "x"
                elif player == "x":
                    mark_spot(row_click, col_click, "x")
                    #new b
                    isWinner = check_board(player)
                    player = "o"

            draw_xo()
            print(isWinner)
            
    pg.display.update()