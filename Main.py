import chess


base_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = chess.Board(base_board)




def set_move(desired_move):
    global move
    move = desired_move


def chess_move():
    board.push(move)
    print(board)

set_move(chess.Move(from_square=chess.E2, to_square=chess.E4))
chess_move()

set_move(chess.Move(from_square=chess.E7, to_square=chess.E5))
chess_move()

