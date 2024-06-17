from .piece import Piece
from typing import List, Tuple, Optional

class Knight(Piece):
    img: int = 2

    def valid_moves(self, board: List[List[Optional['Piece']]]) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        knight_row: int = self.row
        knight_col: int = self.col

        moves_taking_piece: List[Tuple[int, int]] = []
        moves_not_taking_piece: List[Tuple[int, int]] = []

        # Possible moves for a knight
        move_offsets: List[Tuple[int, int]] = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for offset in move_offsets:
            new_row: int = knight_row + offset[0]
            new_col: int = knight_col + offset[1]

            # Check if the new position is on the board
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                possible_move: Optional['Piece'] = board[new_row][new_col]
                if possible_move is None:
                    moves_not_taking_piece.append((new_row, new_col))
                else:
                    if possible_move.color != self.color:
                        moves_taking_piece.append((new_row, new_col))

        return moves_taking_piece, moves_not_taking_piece
