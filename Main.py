from optparse import check_choice
import chess

base_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

def chess_move():
    global board
    board.push(move)
    print(board)
    
def start():
    global board
    board = chess.Board(base_board)
    print(board)
    move_choice()
    
def get_promotion_piece():
    choice = input("Choose the piece to promote (Q/R/N/B)")
    if choice in ['Q','R','N','B']:
        match choice:
            case 'Q': 
                return chess.QUEEN
            case 'R': 
                return chess.ROOK
            case 'N': 
                return chess.KNIGHT
            case 'B': 
                return chess.BISHOP
    
def move_choice():
    global move
    starting_square = input('What sqaure are you moving from? ')
    if (starting_square == 'reset'):
        start()
    ending_square = input('What sqaure are you moving to? ')
    
    if (ending_square == 'reset'):
        start()
        
    else:
        desired_move = chess.Move.from_uci(starting_square + ending_square)
        if (board.is_legal(desired_move) == True):
            move = desired_move
            chess_move()
        else:
            print('This is an illegal move!')
        move_choice()
        
        
        
    
start()


