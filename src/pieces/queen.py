from typing import List, Tuple, Optional
from .piece import Piece

class Queen(Piece):
    img: int = 4

    def valid_moves(self, board: List[List[Optional['Piece']]]) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        queen_row: int = self.row
        queen_col: int = self.col

        moves_taking_piece: List[Tuple[int, int]] = []
        moves_not_taking_piece: List[Tuple[int, int]] = []

        # Directions for queen moves (combining rook and bishop directions)
        directions: List[Tuple[int, int]] = [
            (-1, 0), (1, 0), (0, 1), (0, -1),  # Rook-like moves
            (-1, 1), (1, -1), (1, 1), (-1, -1)  # Bishop-like moves
        ]

        for direction in directions:
            row_increment, col_increment = direction
            for i in range(1, 8):
                new_row: int = queen_row + i * row_increment
                new_col: int = queen_col + i * col_increment

                # Check if the new position is on the board
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    possible_move: Optional[Piece] = board[new_row][new_col]

                    if possible_move is None:
                        moves_not_taking_piece.append((new_row, new_col))
                    else:
                        if possible_move.color != self.color:
                            moves_taking_piece.append((new_row, new_col))
                        break
                else:
                    break

        return moves_taking_piece, moves_not_taking_piece
