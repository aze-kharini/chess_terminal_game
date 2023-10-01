###################################################################################################################################
# getting a list of lists form of a chess board, reading the file

def chess_board():
    inFile = open('CS1117/chess/chess_board.txt', 'r')
    chess_lines = inFile.readlines()
    chess_board = []
    for line in chess_lines:
        line_list = list(line)
        line_list = line_list[:-1]
        chess_board.append(line_list)
    return chess_board

###################################################################################################################################
# Writing to the chess_board file

def update_chess_board(chess_board):
    chess_board_str = ''
    for row in chess_board:
        for element in row:
            chess_board_str += element
        chess_board_str += '\n'

    inFile = open('CS1117/chess/chess_board.txt', 'w')
    inFile.write(chess_board_str)
    inFile.close()

def reset_chess_board():
    chess_board_string = """♜♞♝♛♚♝♞♜
♟♟♟♟♟♟♟♟
 # # # #
# # # # 
 # # # #
# # # # 
♙♙♙♙♙♙♙♙
♖♘♗♕♔♗♘♖
"""
    inFile = open('CS1117/chess/chess_board.txt', 'w')
    inFile.write(chess_board_string)
    inFile.close()




###################################################################################################################################
# Debugging

def ready_for_castle():
    chess_board_string = """♜♞♝♛♚♝♞#
♟♟♟♟♟♟♟♟
 # # # #
# # # # 
 # # # #
# # #♜# 
♙♙♙♙ # #
♖♘♗♕♔ #♖
"""
    inFile = open('CS1117/chess/chess_board.txt', 'w')
    inFile.write(chess_board_string)
    inFile.close()