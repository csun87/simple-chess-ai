import chess
import random
import math


def random_board(max_depth=100):
    board = chess.Board()
    depth = random.randint(0, max_depth)
    for _ in range(depth):
        board.push(random.choice(list(board.legal_moves)))
        if board.is_game_over():
            break
    return board

def calculate_score(board: chess.Board): # white = +, black = -
    if board.is_game_over():
        result = board.result()
        if result == "1-0":
            return 1000
        elif result == "0-1":
            return -1000
        elif result == "1/2-1/2":
            return 0
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        elif piece == chess.Piece(4, chess.WHITE):
            score += 5
        elif piece == chess.Piece(2, chess.WHITE) or piece == chess.Piece(3, chess.WHITE):
            score += 3
        elif piece == chess.Piece(5, chess.WHITE):
            score += 9
        elif piece == chess.Piece(1, chess.WHITE):
            score += 1
        elif piece == chess.Piece(6, chess.WHITE):
            score += 100
        elif piece == chess.Piece(4, chess.BLACK):
            score -= 5
        elif piece == chess.Piece(2, chess.BLACK) or piece == chess.Piece(3, chess.BLACK):
            score -= 3
        elif piece == chess.Piece(5, chess.BLACK):
            score -= 9
        elif piece == chess.Piece(1, chess.BLACK):
            score -= 1
        elif piece == chess.Piece(6, chess.BLACK):
            score -= 100
    return score


def minimax(board: chess.Board, depth: int, alpha: int, beta: int, maximizing_player: chess.Color):
    if board.is_game_over() or depth == 0:
        return calculate_score(board), chess.Move.null()

    if maximizing_player == chess.WHITE:
        bestEval = -math.inf
        bestMove = chess.Move.null()
        for move in list(board.legal_moves):
            copy = board.copy()
            copy.push(move)
            currEval, _ = minimax(copy, depth - 1, alpha, beta, chess.BLACK)
            if currEval > bestEval:
                bestEval = currEval
                bestMove = move
            alpha = max(alpha, bestEval)
            if beta <= alpha:
                break
        return bestEval, bestMove
    else:
        bestEval = math.inf
        bestMove = chess.Move.null()
        for move in list(board.legal_moves):
            copy = board.copy()
            copy.push(move)
            currEval, _ = minimax(copy, depth - 1, alpha, beta, chess.WHITE)
            if currEval < bestEval:
                bestEval = currEval
                bestMove = move
            beta = min(beta, bestEval)
            if beta <= alpha:
                break
        return bestEval, bestMove