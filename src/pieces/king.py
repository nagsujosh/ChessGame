from .piece import Piece


class King(Piece):
    img = 1

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first_move = True  # This will be updated after the first move

    def valid_moves(self, board):
        king_row = self.row
        king_col = self.col

        moves_taking_piece = []
        moves_not_taking_piece = []

        # Possible moves for a king
        move_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for offset in move_offsets:
            new_row = king_row + offset[0]
            new_col = king_col + offset[1]

            # Check if the new position is on the board
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                possible_move = board[new_row][new_col]
                if possible_move is None:
                    moves_not_taking_piece.append((new_row, new_col))
                else:
                    if possible_move.color != self.color:
                        moves_taking_piece.append((new_row, new_col))

        if self.first_move:
            # Castling logic for black
            if self.color == "B":
                # Short Castling
                if (board[0][5] is None and board[0][6] is None and isinstance(board[0][7], Piece) and board[0][7].is_rook
                        and board[0][7].first_move):
                    moves_not_taking_piece.append((0, 6))
                # Long Castling
                if (board[0][1] is None and board[0][2] is None and board[0][3] is None and isinstance(board[0][0], Piece) and board[0][0].is_rook
                        and board[0][0].first_move):
                    moves_not_taking_piece.append((0, 2))

            # Castling logic for white
            if self.color == "W":
                # Short Castling
                if (board[7][5] is None and board[7][6] is None and isinstance(board[7][7], Piece) and board[7][7].is_rook
                        and board[7][7].first_move):
                    moves_not_taking_piece.append((7, 6))
                # Long Castling
                if (board[7][1] is None and board[7][2] is None and board[7][3] is None and isinstance(board[7][0], Piece) and board[7][0].is_rook
                        and board[7][0].first_move):
                    moves_not_taking_piece.append((7, 2))

        return moves_taking_piece, moves_not_taking_piece
