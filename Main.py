import chess

base_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

def chess_move():
    global board
    board.push(move)
    print(board)
   # if board.is_checkmate():
   #elif board.is_stalemate():
#board.is_check():
    
def start():
    global board
    board = chess.Board(base_board)
    print(board)
    move_choice()
    
#def move_choice():
 #   global move
  #  starting_square = input('What sqaure are you moving from? ')
   # if (starting_square == 'reset'):
    #    start()
   # ending_square = input('What sqaure are you moving to? ')
    # ending_square[1] == 8 and starting_squad[1] == 7 and piece_type_at endingsquare = pawn then promotion 
    #if (ending_square == 'reset'):
     #   start()
  #  else:
   #     desired_move = chess.Move.from_uci(starting_square + ending_square)
    #    if (board.is_legal(desired_move) == True):
     #       move = desired_move
      #      chess_move()
       # else:
       #     print('This is an illegal move!')
       # move_choice()
def move_choice():
    global move
    starting_square = input('What square are you moving from? ')
    if starting_square == 'reset':
        start()

    ending_square = input('What square are you moving to? ')
    if ending_square == 'reset':
        start()

    if starting_square == ending_square:
        print("Starting and ending square cannot be the same!")
        move_choice()

    promotion_piece = ""
    piece = board.piece_at(chess.parse_square(starting_square))

    if starting_square[1] == "7" and ending_square[1] == "8" and piece and piece.symbol() == "P":
        promotion_piece = input("Promote to (q,r,b,n)? ").lower()
    elif starting_square[1] == "2" and ending_square[1] == "1" and piece and piece.symbol() == "p":
        promotion_piece = input("Promote to (q,r,b,n)? ").lower()

    desired_move = chess.Move.from_uci(starting_square + ending_square + promotion_piece)

    if board.is_legal(desired_move):
        move = desired_move
        chess_move()
    else:
        print("This is an illegal move!")

    move_choice()




    
start()


