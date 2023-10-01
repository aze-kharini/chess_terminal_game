import check_funcs
import print_funcs
import move_funcs
import chess_board_funcs



###################################################################################################################################
# Useful variables, dics, lists
filler_char = "x"

coordinates_dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

###################################################################################################################################
# Making turns
def turn(counter, white_moves, black_moves):
    print_funcs.print_chess("white", counter)
    command = print_funcs.get_move()
    while check_funcs.format_check(command) != True or check_funcs.castle_check('white', command) != True or castle_check('white', white_moves, command) != True:
        print_funcs.move_cursor_up(1)
        command = print_funcs.get_move()
    if command == 'resign':
        win('black', white_moves+black_moves, command, counter)
    if (command == 'O-O' or command == 'O-O-O'):
        # if castle_check('white', white_moves) == True and check_funcs.castle_check('white', command)==True:
        move_funcs.castle(command, 'white')
        if command == 'O-O':
            white_moves.append('e1cs')
        if command == 'O-O-O':
            white_moves.append('e1cl')

    else:
        piece = move_funcs.piece_on_square(move_funcs.get_start_coord(command))
        while check_funcs.rule_check(command) != True or check_funcs.is_white(piece) != True:
            print_funcs.move_cursor_up(1)
            command = print_funcs.get_move()
            piece = move_funcs.piece_on_square(move_funcs.get_start_coord(command))
        white_moves.append(command)
        if move_funcs.piece_on_square(move_funcs.get_end_coord(command)) == '♚':
            win('white', white_moves+black_moves, command, counter)
        move_funcs.move_piece(command)

    print_funcs.print_chess("black", counter)
    command = print_funcs.get_move()
    while check_funcs.format_check(command) != True or check_funcs.castle_check('black', command) != True or castle_check('black', white_moves, command) != True:
        print_funcs.move_cursor_up(1)
        command = print_funcs.get_move()
    if command == 'resign':
        win('white', white_moves+black_moves, command, counter)
    if command == 'O-O' or command ==  'O-O-O': # and castle_check('black', white_moves) == True and check_funcs.castle_check('black', command)==True:
        move_funcs.castle(command, 'black')
        if command == 'O-O':
            black_moves.append('e8cs')
        if command == 'O-O-O':
            black_moves.append('e8cl')
    else:
        piece = move_funcs.piece_on_square(move_funcs.get_start_coord(command))
        while check_funcs.rule_check(command) != True or check_funcs.is_white(piece) != False:
            print_funcs.move_cursor_up(1)
            command = print_funcs.get_move()
            piece = move_funcs.piece_on_square(move_funcs.get_start_coord(command))
        black_moves.append(command)
        if move_funcs.piece_on_square(move_funcs.get_end_coord(command)) == '♔' : 
            win('black', white_moves+black_moves, command, counter)   
        move_funcs.move_piece(command)


###################################################################################################################################
# Running the program

def run_demo():
    print(filler_char*50)
    print(
        '''Rules:
    1.  Win by capturing the opponent's king 
    2.  No En Passant
    3.  No Stalemate
    4.  Draw by three fold repetition

How to:
    1.  Move by typing coordinates (start, end)
        For example "e2e4"
    2.  To resign, type 'resign'
    3.  To short castle type 'O-O'
        'O-O-O' for long castle
    4.  To promote, type the name of the piece
        For example "queen"'''
    )
    print(filler_char*50)
    print()
    counter = 1
    white_moves = []
    black_moves = []
    print('\n'*15)
    while True:
        turn(counter, white_moves, black_moves)
        counter += 1

####################################################################################################################################
# Winning

def win(color, moves, command, counter):
    if command != 'resign':
        move_funcs.move_piece(command)
    if color == 'white':
        print_funcs.print_chess('black', counter)
    else:
        print_funcs.print_chess('white', counter)
    print(filler_char*10 + f"   {color.upper()} WON   " + filler_char*10)
    print(filler_char*35)
    print(moves)
    chess_board_funcs.reset_chess_board()
    quit()

####################################################################################################################################
# Checking if a color can castle

def castle_check (color, moves, command):
    if color == "white":
        y_coord = 1
    else:
        y_coord = 8
    if command == 'O-O' or command == 'O-O-O':
        for command in moves:
            if command[:2] == f'a{y_coord}' or command[:2] == f'e{y_coord}' or command[:2] == f'h{y_coord}':
                return False
    return True


####################################################################################################################################
# Running the program

run_demo()
