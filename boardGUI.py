import pygame
from settings import GREEN, CREAM, SQUARE_SIZE
from ai_bot import *
import math

class BoardGUI:
    def __init__(self):
        self.board = chess.Board()
        self.selected_piece = None
        self.BLACK_BISHOP = pygame.image.load("./media/black_bishop.png")
        self.BLACK_KING = pygame.image.load("./media/black_king.png")
        self.BLACK_KNIGHT = pygame.image.load("./media/black_knight.png")
        self.BLACK_PAWN = pygame.image.load("./media/black_pawn.png")
        self.BLACK_QUEEN = pygame.image.load("./media/black_queen.png")
        self.BLACK_ROOK = pygame.image.load("./media/black_rook.png")
        self.WHITE_BISHOP = pygame.image.load("./media/white_bishop.png")
        self.WHITE_KING = pygame.image.load("./media/white_king.png")
        self.WHITE_KNIGHT = pygame.image.load("./media/white_knight.png")
        self.WHITE_PAWN = pygame.image.load("./media/white_pawn.png")
        self.WHITE_QUEEN = pygame.image.load("./media/white_queen.png")
        self.WHITE_ROOK = pygame.image.load("./media/white_rook.png")

    def draw_squares(self, window):
        window.fill(GREEN)
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(window, CREAM, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, x1, y1, x2, y2):
        start_square = self.convert_coords(x1, y1)
        end_square = self.convert_coords(x2, y2)
        move = None
        if ((self.board.piece_at(start_square) == chess.Piece(1, chess.WHITE)
             or self.board.piece_at(start_square) == chess.Piece(1, chess.BLACK)) and
                (chess.square_rank(end_square) == 7 or chess.square_rank(end_square) == 0)):
                print("This is running")
                move = chess.Move(start_square, end_square, promotion=chess.QUEEN)
        else:
            move = chess.Move(start_square, end_square)
        if self.board.is_legal(move):
            self.board.push(move)
            print("Legal Move.")
            return True
        else:
            print("Illegal Move!")
            return False


    def draw_state(self, window):
        for square in chess.SQUARES:
            file = chess.square_file(square) # columns, referred to as letters
            rank = 7 - chess.square_rank(square) # rows, referred to as numbers. Converted so 0 is top rank
            x = (file * 100) + 20
            y = (rank * 100) + 20
            piece = self.board.piece_at(square)
            if piece == None:
                continue
            elif piece == chess.Piece(4, chess.WHITE):
                window.blit(self.WHITE_ROOK, (x, y))
            elif piece == chess.Piece(2, chess.WHITE):
                window.blit(self.WHITE_KNIGHT, (x, y))
            elif piece == chess.Piece(3, chess.WHITE):
                window.blit(self.WHITE_BISHOP, (x, y))
            elif piece == chess.Piece(5, chess.WHITE):
                window.blit(self.WHITE_QUEEN, (x, y))
            elif piece == chess.Piece(1, chess.WHITE):
                window.blit(self.WHITE_PAWN, (x, y))
            elif piece == chess.Piece(6, chess.WHITE):
                window.blit(self.WHITE_KING, (x, y))
            elif piece == chess.Piece(4, chess.BLACK):
                window.blit(self.BLACK_ROOK, (x, y))
            elif piece == chess.Piece(2, chess.BLACK):
                window.blit(self.BLACK_KNIGHT, (x, y))
            elif piece == chess.Piece(3, chess.BLACK):
                window.blit(self.BLACK_BISHOP, (x, y))
            elif piece == chess.Piece(5, chess.BLACK):
                window.blit(self.BLACK_QUEEN, (x, y))
            elif piece == chess.Piece(1, chess.BLACK):
                window.blit(self.BLACK_PAWN, (x, y))
            elif piece == chess.Piece(6, chess.BLACK):
                window.blit(self.BLACK_KING, (x, y))

    def convert_coords(self, x, y) -> int:
        file = int(x / 100)
        rank = int((800 - y) / 100)
        return chess.square(file, rank)

    def get_turn(self):
        return self.board.turn

    def ai_move(self, depth=4):
        score, move = minimax(self.board, depth, -math.inf, math.inf, self.board.turn)
        print("Calculated score of move: " + str(score))
        self.board.push(move)

    def check_game_over(self):
        return self.board.is_game_over()

    def reset(self):
        self.board.reset()
