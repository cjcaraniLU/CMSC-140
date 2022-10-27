#Taylor Freeman Kaylee Wu  Emmeth Murphy Cj Carani
board = { "A" : [".", ".", "."], "B" : [".", ".", "."],"C" : [".", ".", "."]}

def print_board(board):
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])


def play_battleship(board):
    print("Welcome to Battleship!")
    column = input("Player 1, select a column for your battleship: ")
    row = int(input("Player 1, select a row for your battleship: "))
    print("Current Board: \n\n")
    print_board(board)

    guess_c = input("Player 2, select a column to check: ")
    guess_r = int(input("Player 2, select a row to check: "))
    score = 0
    while((guess_c != column) or (guess_r-1 != row-1)):
        print("Sorry, nothing there.")
        print("Current Board: ")
        board[guess_c][guess_r-1] = "x"
        print_board(board)
        score = score + 1 
        guess_c = input("Player 2, select a column to check: ")
        guess_r = int(input("Player 2, select a row to check: "))
    print("You won!")
    print("Current Board:")
    board[guess_c][guess_r-1] = "!"
    print_board(board)
    print("Score: ", score, " guesses")
        
play_battleship(board)

