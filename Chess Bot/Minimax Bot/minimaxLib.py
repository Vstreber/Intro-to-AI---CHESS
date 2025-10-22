import chess
import random
import assignValue

def search(yourColor, score, board, depth=0, max_depth=1):
    
    bestScore = float('-inf')
    bestMove = None
    #fen = board.fen()
    
    legalMoves = list(board.legal_moves)
    random.shuffle(legalMoves)

    for i in legalMoves:
        print("Move: " + str(i))
        score = 0

        #reset fen position for next test
        #board.set_fen(fen)

        #calculate move score
        score = assignValue.assignValue(i, board, score, yourColor)

        #if score is larger, updates bestScore
        if score > bestScore:
            bestScore = score
            print("New best score: " + str(bestScore))
            print("Current score: " + str(score))
            bestMove = i
            print("New best move: " + str(i))

        if depth >= max_depth:
            return bestMove
        
        #updates board state with new move.
        board.push(i)
        print("Move stack: " + str(board.move_stack))

        #recursion
        search(yourColor, score, board, depth + 1, max_depth)

        print("Move stack: " + str(board.move_stack))
        board.pop()