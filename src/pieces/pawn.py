from .piece import Piece
from typing import List, Tuple, Optional

class Pawn(Piece):
    img: int = 3

    def __init__(self, row: int, col: int, color: str):
        super().__init__(row, col, color)
        self.toggle: bool = False
        self.first_move: bool = True  # This will be updated after the first move

    def valid_moves(self, board: List[List[Optional['Piece']]]) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        pawn_row: int = self.row
        pawn_col: int = self.col

        moves_taking_piece: List[Tuple[int, int]] = []
        moves_not_taking_piece: List[Tuple[int, int]] = []

        promotion_rank_white = 0  # The rank number for white pawn promotion
        promotion_rank_black = 7  # The rank number for black pawn promotion

        if self.color == 'B':
            # Moving forward
            if pawn_row < 7 and board[pawn_row + 1][pawn_col] is None:
                moves_not_taking_piece.append((pawn_row + 1, pawn_col))
                # Double step for first move
                if self.first_move and board[pawn_row + 2][pawn_col] is None:
                    moves_not_taking_piece.append((pawn_row + 2, pawn_col))

            # Capturing diagonally
            if 0 <= pawn_row + 1 < 8 and 0 <= pawn_col + 1 < 8 and board[pawn_row + 1][pawn_col + 1] is not None:
                if board[pawn_row + 1][pawn_col + 1].color != self.color:
                    moves_taking_piece.append((pawn_row + 1, pawn_col + 1))
            if 0 <= pawn_row + 1 < 8 and 0 <= pawn_col - 1 < 8 and board[pawn_row + 1][pawn_col - 1] is not None:
                if board[pawn_row + 1][pawn_col - 1].color != self.color:
                    moves_taking_piece.append((pawn_row + 1, pawn_col - 1))

            # Promotion check
            if pawn_row + 1 == promotion_rank_black:
                moves_not_taking_piece.append((promotion_rank_black, pawn_col))

        elif self.color == 'W':
            # Moving forward
            if pawn_row > 0 and board[pawn_row - 1][pawn_col] is None:
                moves_not_taking_piece.append((pawn_row - 1, pawn_col))
                # Double step for first move
                if self.first_move and board[pawn_row - 2][pawn_col] is None:
                    moves_not_taking_piece.append((pawn_row - 2, pawn_col))

            # Capturing diagonally
            if 0 <= pawn_row - 1 < 8 and 0 <= pawn_col + 1 < 8 and board[pawn_row - 1][pawn_col + 1] is not None:
                if board[pawn_row - 1][pawn_col + 1].color != self.color:
                    moves_taking_piece.append((pawn_row - 1, pawn_col + 1))
            if 0 <= pawn_row - 1 < 8 and 0 <= pawn_col - 1 < 8 and board[pawn_row - 1][pawn_col - 1] is not None:
                if board[pawn_row - 1][pawn_col - 1].color != self.color:
                    moves_taking_piece.append((pawn_row - 1, pawn_col - 1))

            # Promotion check
            if pawn_row - 1 == promotion_rank_white:
                moves_not_taking_piece.append((promotion_rank_white, pawn_col))

        return moves_taking_piece, moves_not_taking_piece
