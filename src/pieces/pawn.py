from .piece import Piece
from typing import List, Tuple, Optional

class Pawn(Piece):
    img: int = 3

    def __init__(self, row: int, col: int, color: str):
        super().__init__(row, col, color)
        self.toggle: bool = False
        self.first_move: bool = True  # This will be updated after the first move
        # TODO: Implement En passant

    def valid_moves(self, board: List[List[Optional['Piece']]]) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        pawn_row: int = self.row
        pawn_col: int = self.col

        moves_taking_piece: List[Tuple[int, int]] = []
        moves_not_taking_piece: List[Tuple[int, int]] = []

        # Move logic for pawns
        if self.color == 'B':
            # Moving forward
            if board[pawn_row + 1][pawn_col] is None:
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

        if self.color == 'W':
            # Moving forward
            if board[pawn_row - 1][pawn_col] is None:
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

        return moves_taking_piece, moves_not_taking_piece
