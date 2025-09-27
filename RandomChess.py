import chess
import random
import chess.svg

print("=====================================================\nCS 290 Chess Bot Version 0.1 \n=====================================================")

board = chess.Board()
print(board)

board.push_uci("e2e4")
print(board)



print(board.legal_moves)