import chess

def assignValue(i,board,score,yourColor):

    #determining start and end square of move
    startSquare = (str(i))[:2]
    endSquare = (str(i))[-2:]

    #determining value of each captured piece
    if board.is_capture(i):
        # Queen
        if (board.piece_type_at(chess.parse_square(endSquare)) == 5):
            if (board.piece_type_at(chess.parse_square(startSquare)) == yourColor):
                score += 10
            else:
                score -= 10

        # King
        if (board.piece_type_at(chess.parse_square(endSquare)) == 6):
            if (board.piece_type_at(chess.parse_square(startSquare)) == yourColor):
                score += 10
            else:
                score -= 10

        # Knight
        if (board.piece_type_at(chess.parse_square(endSquare)) == 2):         
            if (board.piece_type_at(chess.parse_square(startSquare)) == yourColor):
                score += 5
            else:
                score -= 5

        # Bishop
        if (board.piece_type_at(chess.parse_square(endSquare)) == 3):
            if (board.piece_type_at(chess.parse_square(startSquare)) == yourColor):
                score += 8
            else:
                score -= 8

        # Rook
        if (board.piece_type_at(chess.parse_square(endSquare)) == 4):
            if (board.piece_type_at(chess.parse_square(startSquare)) == yourColor):
                score += 6
            else:
                score -= 6

        # Pawn
        if (board.piece_type_at(chess.parse_square(endSquare)) == 1):
            if (board.piece_type_at(chess.parse_square(startSquare)) == yourColor):
                score += 1
            else:
                score -= 1

    return score