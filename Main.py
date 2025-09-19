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

def reset():
    while True:
        reset_input = input('Type "restart" to restart: ')
        
        if reset_input.upper() == 'RESTART':
            start()
            break  # Exit the loop after restarting
        else:
            print("Invalid input. Please type 'restart' to restart.")
    
def get_promotion_piece():
    choice = input("Choose the piece to promote (Q/R/N/B): ")
    if choice.upper() in ['Q','R','N','B']:
        match choice.upper():
            case 'Q': 
                return 'q'
            case 'R': 
                return 'r'
            case 'N': 
                return 'n'
            case 'B': 
                return 'b'
    else:
        print("Invalid choice, defaulting to Queen")
        return 'q'  # Default to queen if invalid choice

def needs_promotion(board, move):
    piece = board.piece_at(move.from_square)
    if piece and piece.piece_type == chess.PAWN:
        # Check if pawn is moving to promotion rank
        to_rank = chess.square_rank(move.to_square)
        if (piece.color == chess.WHITE and to_rank == 7) or (piece.color == chess.BLACK and to_rank == 0):
            print('PROMOTION YAYAYAYAYAYYAYYAYAYAYAYAY')
            return True
    return False

def get_game_status():
    if board.is_checkmate():
        winner = "Black" if board.turn == chess.WHITE else "White"
        print(f"\nCheckmate! {winner} wins!")
        return True
    elif board.is_stalemate():
        print("\nStalemate! The game is a draw.")
        return True
    elif board.is_insufficient_material():
        print("\nDraw by insufficient material!")
        return True
    elif board.is_seventyfive_moves():
        print("\nDraw by 75-move rule!")
        return True
    elif board.is_fivefold_repetition():
        print("\nDraw by fivefold repetition!")
        return True
    elif board.is_check():
        current_player = "White" if board.turn == chess.WHITE else "Black"
        print(f"\n{current_player} is in check!")
        return False
    
    return False
    
def move_choice():
    global move
    starting_square = input('What square are you moving from? ')
    if starting_square.lower() == 'reset':
        start()
        return
        
    ending_square = input('What square are you moving to? ')
    
    if ending_square.lower() == 'reset':
        start()
        return
    
    try:
        desired_move = chess.Move.from_uci(starting_square + ending_square)
        
        # Check if this move needs promotion
        if needs_promotion(board, desired_move):
            promotion_piece = get_promotion_piece()
            desired_move = chess.Move.from_uci(starting_square + ending_square + promotion_piece)
        
        if board.is_legal(desired_move):
            move = desired_move
            chess_move()
            
            gameover = get_game_status()
            if gameover:
                reset()   
            else:
                move_choice()
        else:
            print('This is an illegal move!')
            move_choice()  # Try again instead of continuing
            
    except ValueError:
        print('Invalid move format! Use format like "e2e4"')
        move_choice()  # Try again
        
start()