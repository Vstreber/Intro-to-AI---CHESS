import datetime
import chess

print("Computer Player? (w=white/b=black): ")
color = input()
now = datetime.datetime.now()
print(now)
if(color == "w"):
    computer_color = "b"
else:
    computer_color = "w"

starting_position = input()
current_player = color
if(starting_position == ""):
    starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
if color == "w":
    move = input()
else:
    # bot command
    print("x") #delete later

while True:
    if current_player == "w" & current_player == color:
        move = input()
        current_player == "b"
    if current_player == "w" & current_player != color:
        # bot command
        current_player == "b"
    if current_player == "b" & current_player == color:
        move = input()
        current_player == "w"
    if current_player == "b" & current_player != color:
        # bot command
        current_player == "w"
