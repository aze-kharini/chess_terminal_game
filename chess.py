
# import move_funcs



# chess_board = [
#     ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
#     ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
#     [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
#     ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
#     [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
#     ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
#     ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
#     ['♖', '♘', '♗', '♕', '♔', '♗' ,'♘', '♖']
# ]

# white_pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
# black_pieces = ['♜', '♞', '♝', '♛', '♚', '♟︎']

# str_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

# white_piece_dic = {
#     'pawn': '♙',
#     'knight': '♘',
#     'bishop': '♗',
#     'rook': '♖',
#     'queen': '♕',
#     'king': '♔'
# }

# black_piece_dic = {
#     'pawn': '♟︎',
#     'knight': '♞',
#     'bishop': '♝',
#     'rook': '♜',
#     'queen': '♛',
#     'king': '♚'
# }

# filler_char = "x"

# def move_cursor_up(n):
#     print("\033[%dA" % (n+1))

# def move_cursor_down(n):
#     print('\033[%dB' % (n-2))

# def move_cursor_left(n):
#     print('\033[%dD' % (n))

# def move_cursor_right(n):
#     print('\033[%dC' % (n))

# def print_chess(color, counter):
#     move_cursor_up(15)
#     if color=="white":
#         print(filler_char*35)
#         print(filler_char*10 + "    Move: {:<5n}".format(counter) + filler_char*10)
#         print(filler_char*35)
#         print(filler_char*8 + "  a b c d e f g h  " + filler_char*8)
#         for index, row in enumerate(chess_board):
#             print(filler_char*7 + " " + str(7-index+1), end="")
#             for square in row:
#                 print("|" + square, end="")
#             print('|', end="")
#             print(str(7-index+1) + " " + filler_char*7)
#         print(filler_char*8 + "  a b c d e f g h  " + filler_char*8)
#         print(filler_char*35)
#     elif color=='black': 
#         print(filler_char*35)
#         print(filler_char*10 + "    Move: {:<5n}".format(counter) + filler_char*10)
#         print(filler_char*35)
#         print(filler_char*8 + "  h g f e d c b a  " + filler_char*8)
#         for index_row in range(len(chess_board)-1,-1,-1):
#             print(filler_char*7 + " " + str(8-index_row), end="")
#             row = chess_board[index_row]
#             for index_square in range(len(row)-1, -1, -1):
#                 square = chess_board[index_row][index_square]
#                 print("|" + square, end="")
#             print('|', end="")
#             print(str(8-index_row) + " " + filler_char*7)
#         print(filler_char*8 + "  h g f e d c b a  " + filler_char*8)
#         print(filler_char*35)


# def reset_chess():
#     chess_board = [
#     ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
#     ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
#     [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
#     ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
#     [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
#     ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
#     ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
#     ['♖', '♘', '♗', '♕', '♔', '♗' ,'♘', '♖']
#     ]

# what is the color
# def square_color(coords):
#     if coords[0]%2==0:
#         if coords[1]%2==0:
#             return '#'
#         else:
#             return " "
#     else:
#         if coords[1]%2==0:
#             return " "
#         else:
#             return "#"
# Notation: always write the starting square and the landing square -> easier

# Understanding command

# coordinates_dic = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8
# }

# def get_start_coord(command):
#     start_coord = []
#     start_coord.append(coordinates_dic[command[0:1]])
#     start_coord.append(int(command[1:2]))
#     return start_coord

# def get_end_coord(command):
#     end_coord = []
#     end_coord.append(coordinates_dic[command[2:3]])
#     end_coord.append(int(command[3:]))
#     return end_coord

# find whatever is at the first coordinate, copy and then insert on the same place either a space or a hashtag

# def piece_on_square(coord):
#     piece = chess_board[8-coord[1]][coord[0]-1]
#     return piece

# def is_piece(coord):
#     piece_to_move = piece_on_square(coord)

#     if piece_to_move == ' ' or piece_to_move == '#':
#         return False
#     else:
#         return True

# def is_opponent(command):
#     end_coord = get_end_coord(command)
#     start_coord = get_start_coord(command)
#     if is_piece(get_end_coord(command)) == True:
#         if piece_on_square(end_coord) in black_pieces and piece_on_square(start_coord) in white_pieces or piece_on_square(end_coord) in white_pieces and piece_on_square(start_coord) in black_pieces:
#             return True
#     return False

# def move_piece(command):
#     start_coord = get_start_coord(command)
#     end_coord = get_end_coord(command)
#     piece_to_move = piece_on_square(start_coord)
#     chess_board[8-start_coord[1]][start_coord[0]-1] = square_color(start_coord)
#     chess_board[8-end_coord[1]][end_coord[0]-1] = piece_to_move

# def rule_check (command):
#     start_coord = get_start_coord(command)
#     end_coord = get_end_coord(command)
#     piece = piece_on_square(start_coord)
#     if (start_coord[1] > 8 and end_coord[1] > 8):
#         return False
#     elif is_piece(start_coord) == False:
#         return False
#     elif moves_check(command) == False:
#         return False
#     elif (is_opponent(command) == False and is_piece(end_coord)==True):
#         return False
#     elif clear_path(command)==False and (piece != '♘' or piece != '♞'):
#         return False
#     else:
#         return True

# def moves_check(command):
#     start_coord = get_start_coord(command)
#     end_coord = get_end_coord(command)
#     piece = piece_on_square(start_coord)
#     if piece == '♜' or piece == '♖':
#         # one of the coordinates have to stay the same 
#         if start_coord[1] == end_coord[1] or start_coord[0] == end_coord[0]:
#             return True
#     elif piece == '♝' or piece == '♗':
#         # the chang in coordinates have to be the same
#         if abs(start_coord[1]-end_coord[1]) == abs(start_coord[0]-end_coord[0]):
#             return True
#     elif piece == '♘' or piece == '♞':
#         # if the first coordinate has changed by 2, the other one can change only by one, end vice versa\
#         if abs(start_coord[1]-end_coord[1]) == 2 and abs(start_coord[0]-end_coord[0])==1 or abs(start_coord[1]-end_coord[1]) == 1 and abs(start_coord[0]-end_coord[0])==2:
#             return True
#     elif piece == '♙' or piece == '♟︎':
#         # if the piece is on the 7 or 2 rank, then it can move by 2, otherwise it can only move one forward, or if there is piece, move to the side 
#         # moving from the starting square
#         if (start_coord[1] == 2 or start_coord[1] == 7) and abs(start_coord[1]-end_coord[1])==2 and start_coord[0]==end_coord[0]:
#             return True
#         # simply moving forward
#         elif abs(start_coord[1]-end_coord[1])==1 and start_coord[0]==end_coord[0]:
#             return True
#         # capturing en passant, normally
#         elif abs(start_coord[1]-end_coord[1])==1 and abs(start_coord[0]-end_coord[0])==1 and (is_piece(end_coord) == True or is_piece([start_coord[1],start_coord[0]+1])==True or is_piece([start_coord[1],start_coord[0]-1])==True):
#             return True
#     elif piece == '♛' or piece == '♕':
#         # like a rook and bishop
#         if start_coord[1] == end_coord[1] or start_coord[0] == end_coord[0]:
#             return True
#         elif abs(start_coord[1]-end_coord[1]) == abs(start_coord[0]-end_coord[0]):
#             return True
#     elif piece == '♚' or piece == '♔':
#         # both coordinates can change max by one 
#         if abs(start_coord[1]-end_coord[1]) <= 1 and abs(start_coord[0]-end_coord[0])<=1:
#             return True
#         # Castling

#     return False

# def range_between(start, end):
#     range_bet = []
#     difference = abs(start-end)
#     if start - end < 0:
#         for i in range(1,difference):
#             range_bet.append(i+start)
#     elif start-end>0:
#         for i in range(1,difference):
#             range_bet.append(start-i)
#     return range_bet

# print(range_between(10,5))

# def path(command):
#     # this concerns only moving in a straight line or diagonal
#     start_coord = get_start_coord(command)
#     end_coord = get_end_coord(command)
#     path = []
#     # diagonal
#     if abs(start_coord[1]-end_coord[1]) == abs(start_coord[0]-end_coord[0]):
#         x_coords = range_between(start_coord[0], end_coord[0])
#         y_coords = range_between(start_coord[1], end_coord[1])
#         for i in range(len(x_coords)):
#             path.append([x_coords[i], y_coords[i]])
#     # straight path
#     elif start_coord[0] == end_coord[0]:
#         y_coords = range_between(start_coord[1],end_coord[1])
#         x_coord = start_coord[0]
#         for i in range(len(y_coords)):
#             path.append([x_coord, y_coords[i]])
#     elif start_coord[1] == end_coord[1]:
#         x_coords = range_between(start_coord[0], end_coord[0])
#         y_coord = start_coord[1]
#         for i in range(len(x_coords)):
#             path.append([x_coords[i], y_coord])
#     return path

# def clear_path(command):
#     path_list = path(command)
#     for square in path_list:
#         if is_piece(square)==True:
#             return False
#     return True 

# def is_white(piece):
#     if piece in white_pieces:
#         return True
#     return False

# def win(color, moves, command, counter):
#     if command != 'resign':
#         move_piece(command)
#     if color == 'white':
#         print_chess('black', counter)
#     else:
#         print_chess('white', counter)
#     print(filler_char*10 + f"   {color.upper()} WON   " + filler_char*10)
#     print(filler_char*35)
#     print(moves)
#     quit()

# Castling

# def castle(command, color):
#     if color == 'white':
#         y_coord = 8
#     else:
#         y_coord = 1
#     if command == 'O-O':
#         move_piece(f"e{y_coord}g{y_coord}")
#         move_piece(f"h{y_coord}f{y_coord}")
#     else:
#         move_piece(f"e{y_coord}c{y_coord}")
#         move_piece(f"a{y_coord}d{y_coord}")

# def castle_check(command, color):
#     if color == 'white':
#         y_coord = 8
#     else:
#         y_coord = 1
#     start_coord = get_start_coord(f"e{y_coord}g{y_coord}")
#     end_coord = get_end_coord(f"e{y_coord}g{y_coord}")
#     if piece_on_square(start_coord) != '♚' or piece_on_square(start_coord) != '♔':
#         return False
#     elif piece_on_square(end_coord) != '' or piece_on_square(end_coord) != '':
#         return False
#     elif rule_check(f"h{y_coord}f{y_coord}") == False or rule_check(f"a{y_coord}d{y_coord}") == False:
#         return False
    



# Correct input format

# def format_check(command):
#     if command=='resign' or command == 'O-O' or command == 'O-O-O' or command in black_piece_dic.keys() or command in white_piece_dic.keys():
#         return True
#     elif len(command) != 4:
#         return False
#     elif command[0] not in coordinates_dic.keys() or command[2] not in coordinates_dic.keys():
#         return False
#     elif command[1] not in str_numbers or command[3] not in str_numbers:
#         return False
#     elif int(command[1]) >8 or int(command[3])>8:
#         return False
#     else:
#         return True
# Input

# def get_move():
#     print(filler_char*10 + f"  Move:        " +  filler_char*10)
#     print(filler_char*35)
#     move_cursor_up(2)
#     command = input(filler_char*10 + "  Move: ")
#     return command


# def update_castle_check(command, color):
#     moved_white_king = False
#     moved_black_king = False
#     moved_white_a1_rook = False
#     moved_white_h1_rook = False
#     moved_black_a8_rook = False
#     moved_black_h8_rook = False
#     piece = piece_on_square(get_start_coord(command))
#     if piece == '♔':
#         moved_white_king = True
#     elif piece == '♖' and get_start_coord(command) == [0,7]:
#         moved_white_a1_rook = True
#     elif piece == '♖' and get_start_coord(command) == [7,7]:
#         moved_white_h1_rook = True

# def turn(counter, moves):
#     print_chess("white", counter)
#     command = get_move()
#     while format_check(command) != True:
#         move_cursor_up(1)
#         command = get_move()
#     if command == 'resign':
#         win('black', moves, command, counter)
#     elif command == 'O-O' or 'O-O-O':
#         castle(command, 'white')
#     piece = piece_on_square(get_start_coord(command))
#     while rule_check(command) != True or is_white(piece) != True:
#         move_cursor_up(1)
#         command = get_move()
#         piece = piece_on_square(get_start_coord(command))
#     moves.append(command)
#     if piece_on_square(get_end_coord(command)) == '♚':
#         win('white', moves, command, counter)
#     move_piece(command)

#     print_chess("black", counter)
#     command = get_move()
#     if command == 'resign':
#         win('white', moves, command, counter)
#     elif command == 'O-O' or 'O-O-O':
#         castle(command, 'black')
#     piece = piece_on_square(get_start_coord(command))
#     while rule_check(command) != True or is_white(piece) != False:
#         move_cursor_up(1)
#         command = get_move()
#         piece = piece_on_square(get_start_coord(command))
#     moves.append(command)
#     if piece_on_square(get_end_coord(command)) == '♔' : 
#         win('black', moves, command, counter)   
#     move_piece(command)


# def run_demo():
#     print(filler_char*50)
#     print(
#         '''Rules:
#     1.  Win by capturing the opponent's king 
#     2.  No En Passant
#     3.  No Stalemate
#     4.  Draw by three fold repetition

# How to:
#     1.  Move by typing coordinates (start, end)
#         For example "e2e4"
#     2.  To resign, type 'resign'
#     3.  To short castle type 'O-O'
#         'O-O-O' for long castle
#     4.  To promote, type the name of the piece
#         For example "queen"'''
#     )
#     print(filler_char*50)
#     print()
#     counter = 1
#     moves = []
#     print('\n'*15)
#     while True:
#         turn(counter, moves)
#         counter += 1


# castling
# promoting
# Draws (no stalemate), three fold repetition
# time control



