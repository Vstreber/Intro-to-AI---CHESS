import datetime
import chess
import random
import re

board = chess.Board()

now = datetime.datetime.now()
print(now)

print("Computer Player? (w=white/b=black): ")
color = input()
x = True

while x:
    if(color == "w"):
        computer = "b"
        x = False
    elif(color == "b"):
        computer = "w"
        x = False
    else:
        print("Please enter 'w' or 'b'")
        color = input()

current_player = "w"
human = color

print("Please enter your starting position.")
starting_position = input()
if(starting_position == ""):
    starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

board.set_fen(starting_position)

print(board)

while (board.is_checkmate() == False):
    if human == current_player:
        print("Enter your move: ")
        move = input()

        # while move not in list(board.legal_moves):
        #     move = input("Please input a valid move. ")

        board.push_uci(move)
        current_player = "b"
    elif computer == current_player:
        print("The bot's move is: ")
        legal_moves = list(board.legal_moves)
        move = random.choice(legal_moves)
        move = str(move)
        print(move)
        board.push_uci(move)
        current_player = "w"

    print("New Fen Position" + board.fen())
    print(board)

    if board.is_checkmate() == True:
        print("Checkmate!")
