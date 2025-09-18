import chess

# 1. Setup the board
base_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = chess.Board(base_board)

# Optional: Print the board before the move
print("--- Board before move ---")
print(board)

# 2. Create the move object (e2 to e4)
move = chess.Move(from_square=chess.E2, to_square=chess.E4)
print(f"\nMove object created: {move}")

# 3. Apply the move to the board
board.push(move)

# Optional: Print the board after the move
print("\n--- Board after move ---")
print(board)