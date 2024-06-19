from typing import List, Optional
from src.pieces import Piece, Rook, Knight, Bishop, Queen, King, Pawn


def initialize_board(board: 'Board') -> 'Board':
    rows = board.rows
    cols = board.cols

    board.board = [[None for _ in range(cols)] for _ in range(rows)]

    # Initialize black pieces
    board.board[0][0] = Rook(0, 0, "B")
    board.board[0][1] = Knight(0, 1, "B")
    board.board[0][2] = Bishop(0, 2, "B")
    board.board[0][3] = Queen(0, 3, "B")
    board.board[0][4] = King(0, 4, "B")
    board.board[0][5] = Bishop(0, 5, "B")
    board.board[0][6] = Knight(0, 6, "B")
    board.board[0][7] = Rook(0, 7, "B")

    for col in range(cols):
        board.board[1][col] = Pawn(1, col, "B")
        board.board[1][col].is_pawn = True

    # Initialize white pieces
    board.board[7][0] = Rook(7, 0, "W")
    board.board[7][1] = Knight(7, 1, "W")
    board.board[7][2] = Bishop(7, 2, "W")
    board.board[7][3] = Queen(7, 3, "W")
    board.board[7][4] = King(7, 4, "W")
    board.board[7][5] = Bishop(7, 5, "W")
    board.board[7][6] = Knight(7, 6, "W")
    board.board[7][7] = Rook(7, 7, "W")

    for col in range(cols):
        board.board[6][col] = Pawn(6, col, "W")
        board.board[6][col].is_pawn = True

    # Set additional attributes for kings and rooks
    board.board[0][4].is_king = True
    board.board[7][4].is_king = True

    # Here in the tuple the first value indicates this piece is a rook and
    # the second element indicates that the rook is from the left side
    board.board[0][0].is_rook = (True, True)
    board.board[7][0].is_rook = (True, True)
    board.board[7][7].is_rook = (True, False)
    board.board[0][7].is_rook = (True, False)

    return board
