import chess_board_funcs

###################################################################################################################################
# Useful variables, dics, lists
filler_char = "x"


###################################################################################################################################
# Getting the move from the user

def get_move():
    print(filler_char*10 + f"  Move:        " +  filler_char*10)
    print(filler_char*35)
    move_cursor_up(2)
    command = input(filler_char*10 + "  Move: ")
    return command

###################################################################################################################################
# Getting the color of a square

def square_color(coords):
    if coords[0]%2==0:
        if coords[1]%2==0:
            return '#'
        else:
            return " "
    else:
        if coords[1]%2==0:
            return " "
        else:
            return "#"

###################################################################################################################################
# Functions for moving the cursor

def move_cursor_up(n):
    print("\033[%dA" % (n+1))

def move_cursor_down(n):
    print('\033[%dB' % (n-2))

def move_cursor_left(n):
    print('\033[%dD' % (n))

def move_cursor_right(n):
    print('\033[%dC' % (n))

###################################################################################################################################
# Printing the board

def print_chess(color, counter):
    move_cursor_up(15)
    if color=="white":
        print(filler_char*35)
        print(filler_char*10 + "    Move: {:<5n}".format(counter) + filler_char*10)
        print(filler_char*35)
        print(filler_char*8 + "  a b c d e f g h  " + filler_char*8)
        for index, row in enumerate(chess_board_funcs.chess_board()):
            print(filler_char*7 + " " + str(7-index+1), end="")
            for square in row:
                print("|" + square, end="")
            print('|', end="")
            print(str(7-index+1) + " " + filler_char*7)
        print(filler_char*8 + "  a b c d e f g h  " + filler_char*8)
        print(filler_char*35)
    elif color=='black': 
        print(filler_char*35)
        print(filler_char*10 + "    Move: {:<5n}".format(counter) + filler_char*10)
        print(filler_char*35)
        print(filler_char*8 + "  h g f e d c b a  " + filler_char*8)
        for index_row in range(len(chess_board_funcs.chess_board())-1,-1,-1):
            print(filler_char*7 + " " + str(8-index_row), end="")
            row = chess_board_funcs.chess_board()[index_row]
            for index_square in range(len(row)-1, -1, -1):
                square = chess_board_funcs.chess_board()[index_row][index_square]
                print("|" + square, end="")
            print('|', end="")
            print(str(8-index_row) + " " + filler_char*7)
        print(filler_char*8 + "  h g f e d c b a  " + filler_char*8)
        print(filler_char*35)