import print_funcs
import chess_board_funcs



###################################################################################################################################
# Dictionaries

white_pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
black_pieces = ['♜', '♞', '♝', '♛', '♚', '♟']

white_piece_dic = {
    'a1':[],
    'b1':[],
    'c1':[],
    'd1':[],
    'e1':[],
    'f1':[],
    'g1':[],
    'h1':[],
    'a2':[],
    'b2':[],
    'c2':[],
    'd2':[],
    'e2':[],
    'f2':[],
    'g2':[],
    'h2':[]
}

black_piece_dic = {
    'a8':[],
    'b8':[],
    'c8':[],
    'd8':[],
    'e8':[],
    'f8':[],
    'g8':[],
    'h8':[],
    'a7':[],
    'b7':[],
    'c7':[],
    'd7':[],
    'e7':[],
    'f7':[],
    'g7':[],
    'h7':[]
}

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

commands_dic = {
    1 :'a',
    2 :'b',
    3 :'c',
    4 :'d',
    5 :'e',
    6 :'f',
    7 :'g',
    8 :'h'
}

# On each move, a function will generate a list of possible squares a piece can move to and store them in a dictionary, if a piece gets captured, the key gets deleted from the dictionary
# This should allow for checks, checkmates, stalemate, easier castling, checking if a command is valid etc. 
# it will also be much more easier to understand
# I will have to have a correlation with the actual board, because there is no way of knowing which piece is what (pawns, knights, rooks), the key in the dictionary might be a coord which would be getting updated every time

def update_dic(move, color):
    if color == 'white':
        white_piece_dic[move[2:]] = []
        white_piece_dic.pop(move[:2])



###################################################################################################################################
# Useful Functions about coords

def remove_duplicates(list):
    clean_list = []
    for coord in list:
        if coord not in clean_list:
            clean_list.append(coord)
    return clean_list

def get_start_coord(command):
    start_coord = []
    start_coord.append(coordinates_dic[command[0:1]])
    start_coord.append(int(command[1:2]))
    return start_coord

def get_end_coord(command):
    end_coord = []
    end_coord.append(coordinates_dic[command[2:3]])
    end_coord.append(int(command[3:]))
    return end_coord

def get_command(coord):
    command = ''
    command += commands_dic[coord[0]] + str(coord[1])
    return command

###################################################################################################################################
# Functions about pieces on squares

def piece_on_square(coord):
    piece = chess_board_funcs.chess_board()[8-coord[1]][coord[0]-1]
    return piece

def is_piece(coord):
    piece_to_move = piece_on_square(coord)

    if piece_to_move == ' ' or piece_to_move == '#':
        return False
    else:
        return True

def is_opponent(command):
    end_coord = get_end_coord(command)
    start_coord = get_start_coord(command)
    if is_piece(get_end_coord(command)) == True:
        if piece_on_square(end_coord) in black_pieces and piece_on_square(start_coord) in white_pieces or piece_on_square(end_coord) in white_pieces and piece_on_square(start_coord) in black_pieces:
            return True
    return False

def is_opponent_coords(start_coord, end_coord):
    if is_piece(end_coord) == True:
        if piece_on_square(end_coord) in black_pieces and piece_on_square(start_coord) in white_pieces or piece_on_square(end_coord) in white_pieces and piece_on_square(start_coord) in black_pieces:
            return True
    return False


###################################################################################################################################
# Functions about the path of a piece

def range_between(start, end):
    range_bet = []
    difference = abs(start-end)
    if start - end < 0:
        for i in range(1,difference):
            range_bet.append(i+start)
    elif start-end>0:
        for i in range(1,difference):
            range_bet.append(start-i)
    return range_bet

def path(command):
    # this concerns only moving in a straight line or diagonal
    start_coord = get_start_coord(command)
    end_coord = get_end_coord(command)
    path = []
    # diagonal
    if abs(start_coord[1]-end_coord[1]) == abs(start_coord[0]-end_coord[0]):
        x_coords = range_between(start_coord[0], end_coord[0])
        y_coords = range_between(start_coord[1], end_coord[1])
        for i in range(len(x_coords)):
            path.append([x_coords[i], y_coords[i]])
    # straight path
    elif start_coord[0] == end_coord[0]:
        y_coords = range_between(start_coord[1],end_coord[1])
        x_coord = start_coord[0]
        for i in range(len(y_coords)):
            path.append([x_coord, y_coords[i]])
    elif start_coord[1] == end_coord[1]:
        x_coords = range_between(start_coord[0], end_coord[0])
        y_coord = start_coord[1]
        for i in range(len(x_coords)):
            path.append([x_coords[i], y_coord])
    return path

def clear_path(command):
    path_list = path(command)
    for square in path_list:
        if is_piece(square)==True:
            return False
    return True 


###################################################################################################################################
# Vector Functions

vector_dic = {
    0: [1,0],
    1: [1, 1],
    2: [1, -1],
    3: [0, 1],
    4: [0, -1],
    5: [-1, 0], 
    6: [-1, 1],
    7: [-1, -1]
}

knight_vector_dic = {
    0: [2,1],
    1: [2, -1],
    2: [1, -2],
    3: [1, 2],
    4: [-2, -1],
    5: [2, 2], 
    6: [-1, 2],
    7: [-1, -2]
}

def vector_path(vector, current_pos):
    start_coord = current_pos
    current_pos = vector_square(vector, current_pos)
    squares = []
    while current_pos[0] >0 and current_pos[0] < 9 and current_pos[1]<9 and current_pos[1]>0 and is_piece(current_pos)==False:
        squares.append(current_pos)
        current_pos = vector_square(vector, current_pos)
        if current_pos[0] >0 and current_pos[0] < 9 and current_pos[1]<9 and current_pos[1]>0 and is_opponent_coords(start_coord, current_pos) == True:
            squares.append(current_pos)
    return squares

def vector_square(vector, current_pos):
    return [current_pos[0]+vector[0], current_pos[1]+vector[1]]

def vector_checked_square(vector, current_pos):
    square = [current_pos[0]+vector[0], current_pos[1]+vector[1]]
    if square[0]>0 and square[0] <9 and square[1]>0 and square[1]<9 and (is_opponent_coords(current_pos, square) == True or is_piece(square)==False):
        return [square]
    return []

###################################################################################################################################
# Functions returning a list of all possible squares


def rook_squares(start_coord):
    squares = []
    squares += vector_path([1,0], start_coord)
    squares += vector_path([-1,0], start_coord) 
    squares += vector_path([0,1], start_coord)
    squares += vector_path([0,-1], start_coord)
    return squares


def bishop_squares(start_coord):
    squares = []
    squares += vector_path([1,1], start_coord)
    squares += vector_path([1,-1], start_coord) 
    squares += vector_path([-1,1], start_coord)
    squares += vector_path([-1,-1], start_coord)
    return squares


def knight_squares(start_coord):
    squares = []
    for i in range(8):
        vector = knight_vector_dic[i]
        squares += vector_checked_square(vector, start_coord)
    return squares

def pawn_squares(start_coord, color):
    start_row = start_coord[1]
    start_col = start_coord[0]
    squares = [] 
    if color == 'white':
        squares += vector_checked_square([0,1], start_coord)
        if start_row == 2 and is_piece([start_col, 3]) == False: # checking the path of a pawn
            squares += vector_checked_square([0,2], start_coord)
    else:
        squares += vector_checked_square([0,-1], start_coord)
        if start_row == 7 and is_piece([start_col, 6]) == False: # checking the path of a pawn
                    squares += vector_checked_square([0,-2], start_coord)
    attacked_squares = attacked_pawn_squares(start_coord, color)
    all_squares = squares + attacked_squares
    return all_squares

def attacked_pawn_squares(start_coord, color):
    start_row = start_coord[1]
    start_col = start_coord[0]
    squares = [] 
    if color == 'white':
        if start_col+1 <9 and start_row+1 < 9 : # and is_opponent_coords(start_coord, [start_col+1, start_row+1]) == True:
            squares += vector_checked_square([1,1], start_coord)
        if start_col-1 <9 and start_row+1 < 9: # and is_opponent_coords(start_coord, [start_col-1, start_row+1]) == True:
            squares += vector_checked_square([-1,1], start_coord)
    else:
        if start_col+1 <9 and start_row-1 < 9: # and is_opponent_coords(start_coord, [start_col+1, start_row-1]) == True:
            squares += vector_checked_square([1,-1], start_coord)
        if start_col-1 <9 and start_row-1 < 9: # and is_opponent_coords(start_coord, [start_col-1, start_row-1]) == True:
            squares += vector_checked_square([-1,-1], start_coord)
    return squares

def queen_squares(start_coord):
    squares = []
    squares += bishop_squares(start_coord)
    squares += rook_squares(start_coord)
    return squares


def possible_king_squares(start_coord):
    squares = []
    for i in range(8):
        vector = vector_dic[i]
        squares += vector_checked_square(vector, start_coord)

    return squares

###################################################################################################################################
# All attacked squares
# go through the whole board and add to a list all of the squares attacked

def all_attacked_squares(color):
    attacked_squares = []
    if color == 'white':
        for end_row in range(1,9):
            for end_col in range(1,9):
                piece = piece_on_square([end_col, end_row])
                if piece == '♖':
                    attacked_squares += rook_squares([end_col, end_row])
                elif piece == '♗':
                    attacked_squares += bishop_squares([end_col, end_row])
                elif piece == '♘':
                    attacked_squares += knight_squares([end_col, end_row])
                elif piece == '♙':
                    attacked_squares += attacked_pawn_squares([end_col, end_row], 'white')
                elif piece == '♕':
                    attacked_squares += queen_squares([end_col, end_row])
                elif piece == '♔':
                    attacked_squares += possible_king_squares([end_col, end_row])
    else:
        for end_row in range(1,9):
            for end_col in range(1,9):
                piece = piece_on_square([end_col, end_row])
                if piece == '♜':
                    attacked_squares += rook_squares([end_col, end_row])
                elif piece == '♝':
                    attacked_squares += bishop_squares([end_col, end_row])
                elif piece == '♞':
                    attacked_squares += knight_squares([end_col, end_row])
                elif piece == '♟':
                    attacked_squares += attacked_pawn_squares([end_col, end_row], 'black')
                elif piece == '♛':
                    attacked_squares += queen_squares([end_col, end_row])
                elif piece == '♚':
                    attacked_squares += possible_king_squares([end_col, end_row])
    attacked_squares = remove_duplicates(attacked_squares)
    return attacked_squares


###################################################################################################################################
# Moving a piece

def move_piece(command):
    start_coord = get_start_coord(command)
    end_coord = get_end_coord(command)
    piece_to_move = piece_on_square(start_coord)
    chess_board = chess_board_funcs.chess_board()
    chess_board[8-start_coord[1]][start_coord[0]-1] = print_funcs.square_color(start_coord)
    chess_board[8-end_coord[1]][end_coord[0]-1] = piece_to_move
    chess_board_funcs.update_chess_board(chess_board)

###################################################################################################################################
# Castling

def castle(command, color):
    if color == 'white':
        y_coord = 1
    else:
        y_coord = 8
    if command == 'O-O':
        move_piece(f"e{y_coord}g{y_coord}")
        move_piece(f"h{y_coord}f{y_coord}")
    else:
        move_piece(f"e{y_coord}c{y_coord}")
        move_piece(f"a{y_coord}d{y_coord}")


###################################################################################################################################
# Debugging

# chess_board_funcs.ready_for_castle()
# print(all_attacked_squares('black'))