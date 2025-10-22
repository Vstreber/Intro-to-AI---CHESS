import chess
import random

def singleSearch(board):
    bestScore = float('-inf')
    bestMove = None
    score = 0

    myTestBoard = chess.Board()
    oppTestBoard = chess.Board()

    myTestBoard.set_fen(board.fen())
    legalMoves = list(myTestBoard.legal_moves)
    random.shuffle(legalMoves)

    for i in legalMoves:
        myTestBoard.set_fen(board.fen())
        myEndSquare = (str(i))[-2:]
        if myTestBoard.is_capture(i):

            # Queen
            if (myTestBoard.piece_type_at(chess.parse_square(myEndSquare)) == 5):
                score += 10

            # King
            if (myTestBoard.piece_type_at(chess.parse_square(myEndSquare)) == 6):
                score += 10

            # Knight
            if (myTestBoard.piece_type_at(chess.parse_square(myEndSquare)) == 2):         
                score += 5

            # Bishop
            if (myTestBoard.piece_type_at(chess.parse_square(myEndSquare)) == 3):
                score += 8

            # Rook
            if (myTestBoard.piece_type_at(chess.parse_square(myEndSquare)) == 4):
                score += 6

            # Pawn
            if (myTestBoard.piece_type_at(chess.parse_square(myEndSquare)) == 1):
                score += 1

        myTestBoard.push_uci(str(i))

        for j in legalMoves:
            oppTestBoard.set_fen(myTestBoard.fen())

            oppEndSquare = (str(j))[-2:]
            if myTestBoard.is_capture(j):
                if (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "Q") or (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "q"):
                    score -= 10
                if (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "K") or (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "k"):
                    score -= 10
                if (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "N") or (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "n"):
                    score -= 5
                if (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "B") or (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "b"):
                    score -= 8
                if (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "R") or (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "r"):
                    score -= 6
                if (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "P") or (str(oppTestBoard.piece_at(chess.parse_square(oppEndSquare))) == "p"):
                    score -= 1

            if score > bestScore:
                bestScore = score
                bestMove = i
    
    return str(bestMove)

