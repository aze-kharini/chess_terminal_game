import move_funcs
import chess_board_funcs

###################################################################################################################################
# Useful variables, dics, lists

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

white_pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
black_pieces = ['♜', '♞', '♝', '♛', '♚', '♟']

str_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

white_piece_dic = {
    'pawn': '♙',
    'knight': '♘',
    'bishop': '♗',
    'rook': '♖',
    'queen': '♕',
    'king': '♔'
}

black_piece_dic = {
    'pawn': '♟',
    'knight': '♞',
    'bishop': '♝',
    'rook': '♜',
    'queen': '♛',
    'king': '♚'
}

###################################################################################################################################
# Checking the format of the command

def format_check(command):
    if command=='resign' or command == 'O-O' or command == 'O-O-O' or command in black_piece_dic.keys() or command in white_piece_dic.keys():
        return True
    elif len(command) != 4:
        return False
    elif command[0] not in coordinates_dic.keys() or command[2] not in coordinates_dic.keys():
        return False
    elif command[1] not in str_numbers or command[3] not in str_numbers:
        return False
    elif int(command[1]) >8 or int(command[3])>8:
        return False
    else:
        return True


###################################################################################################################################
# Checking the rules

def rule_check (command):
    start_coord = move_funcs.get_start_coord(command)
    end_coord = move_funcs.get_end_coord(command)
    piece = move_funcs.piece_on_square(start_coord)
    if (start_coord[1] > 8 and end_coord[1] > 8):
        return False
    elif move_funcs.is_piece(start_coord) == False:
        return False
    elif moves_check(command) == False:
        return False
    elif (move_funcs.is_opponent(command) == False and move_funcs.is_piece(end_coord)==True):
        return False
    elif move_funcs.clear_path(command)==False and (piece != '♘' or piece != '♞'):
        return False
    else:
        return True

def moves_check(command):
    start_coord = move_funcs.get_start_coord(command)
    end_coord = move_funcs.get_end_coord(command)
    piece = move_funcs.piece_on_square(start_coord)
    if piece == '♜' or piece == '♖':
        # one of the coordinates have to stay the same 
        if start_coord[1] == end_coord[1] or start_coord[0] == end_coord[0]:
            return True
    elif piece == '♝' or piece == '♗':
        # the chang in coordinates have to be the same
        if abs(start_coord[1]-end_coord[1]) == abs(start_coord[0]-end_coord[0]):
            return True
    elif piece == '♘' or piece == '♞':
        # if the first coordinate has changed by 2, the other one can change only by one, end vice versa\
        if abs(start_coord[1]-end_coord[1]) == 2 and abs(start_coord[0]-end_coord[0])==1 or abs(start_coord[1]-end_coord[1]) == 1 and abs(start_coord[0]-end_coord[0])==2:
            return True
    elif piece == '♙' or piece == '♟':
        # if the piece is on the 7 or 2 rank, then it can move by 2, otherwise it can only move one forward, or if there is piece, move to the side 
        # moving from the starting square
        if (start_coord[1] == 2 or start_coord[1] == 7) and abs(start_coord[1]-end_coord[1])==2 and start_coord[0]==end_coord[0]:
            return True
        # simply moving forward
        elif abs(start_coord[1]-end_coord[1])==1 and start_coord[0]==end_coord[0]:
            return True
        # capturing en passant, normally
        elif abs(start_coord[1]-end_coord[1])==1 and abs(start_coord[0]-end_coord[0])==1 and (move_funcs.is_piece(end_coord) == True or move_funcs.is_piece([start_coord[1],start_coord[0]+1])==True or move_funcs.is_piece([start_coord[1],start_coord[0]-1])==True):
            return True
    elif piece == '♛' or piece == '♕':
        # like a rook and bishop
        if start_coord[1] == end_coord[1] or start_coord[0] == end_coord[0]:
            return True
        elif abs(start_coord[1]-end_coord[1]) == abs(start_coord[0]-end_coord[0]):
            return True
    elif piece == '♚' or piece == '♔':
        # both coordinates can change max by one 
        if abs(start_coord[1]-end_coord[1]) <= 1 and abs(start_coord[0]-end_coord[0])<=1:
            return True


    return False

###################################################################################################################################
# Useful Funcs

def is_white(piece):
    if piece in white_pieces:
        return True
    return False

###################################################################################################################################
# Castling check

def castle_check(color, command):
    if color == 'white':
        opponent_attacked_squares = move_funcs.all_attacked_squares('black')
        y_coord = 1
    else: 
        opponent_attacked_squares = move_funcs.all_attacked_squares('white')
        y_coord = 8
    if command == 'O-O': #and [6,y_coord] in opponent_attacked_squares or [7, y_coord] in opponent_attacked_squares or [8, y_coord] in opponent_attacked_squares or [5, y_coord] in opponent_attacked_squares:
        for x_coord in range(5, 9):
            if [x_coord,y_coord] in opponent_attacked_squares:
                return False
    elif command == 'O-O-O': #and [2,y_coord] in opponent_attacked_squares or [3, y_coord] in opponent_attacked_squares or [4, y_coord] in opponent_attacked_squares or [1, y_coord] in opponent_attacked_squares or [5, y_coord] in opponent_attacked_squares:
        for x_coord in range(1, 6):
            if [x_coord, y_coord] in opponent_attacked_squares:
                return False
    return True



###################################################################################################################################
# Debugging
# chess_board_funcs.ready_for_castle()
# print(castle_check('white', 'O-O'))