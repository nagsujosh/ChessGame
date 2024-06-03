import pygame
from src.constants import *

class Piece:
    img = None

    startX = BOARD_RECT[0]
    startY = BOARD_RECT[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.availableMovesNotTakingPiece = None
        self.availableMovesTakingPiece = None
        self.check = None
        self.isKing = False
        self.isPawn = False
        self.isRook = None

    def valid_moves(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win, board):

        self.availableMovesTakingPiece, self.availableMovesNotTakingPiece = self.valid_moves(board)            

        piece = W[self.img] if self.color == 'W' else B[self.img]

        selected_rect_x = self.startX + self.col * BOARD_RECT[2] // 8 + 5
        selected_rect_y = self.startY + self.row * BOARD_RECT[3] // 8 + 5

        piece_x = self.startX + self.col * BOARD_RECT[2] // 8 + 7
        piece_y = self.startY + self.row * BOARD_RECT[3] // 8 + 5

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (selected_rect_x, selected_rect_y, 60, 60), width=3)

        win.blit(piece, (piece_x, piece_y))

        if self.selected:

            if self.availableMovesNotTakingPiece and not self.check:
                for move in self.availableMovesNotTakingPiece:
                    circle_x = self.startX + move[1] * BOARD_RECT[2] // 8 + 33
                    circle_y = self.startY + move[0] * BOARD_RECT[3] // 8 + 33

                    pygame.draw.circle(win, (255, 0, 0), (circle_x, circle_y), 10)

            if self.availableMovesTakingPiece and not self.check:
                for move in self.availableMovesTakingPiece:
                    rect_x = self.startX + move[1] * BOARD_RECT[2] // 8 + 5
                    rect_y = self.startY + move[0] * BOARD_RECT[3] // 8 + 5

                    pygame.draw.rect(win, (0, 255, 0), (rect_x, rect_y, 60, 60), width=3)  

            if self.check:
                  for move in self.check:
                    circle_x = self.startX + move[1] * BOARD_RECT[2] // 8 + 33
                    circle_y = self.startY + move[0] * BOARD_RECT[3] // 8 + 33

                    pygame.draw.circle(win, (255, 0, 0), (circle_x, circle_y), 10)

class Bishop(Piece):
    img = 0

    def valid_moves(self, board):
        bishop_row = self.row
        bishop_col = self.col

        movesTakingPiece = []
        movesNotTakingPiece = []

        # Directions for diagonals
        directions = [(-1, 1), (1, -1), (1, 1), (-1, -1)]

        for direction in directions:
            row_increment, col_increment = direction
            for i in range(1, 8):
                new_row = bishop_row + i * row_increment
                new_col = bishop_col + i * col_increment

                # Check if the new position is on the board
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    possible_move = board[new_row][new_col]

                    if possible_move is None:
                        movesNotTakingPiece.append((new_row, new_col))
                    else:
                        if possible_move.color != self.color:
                            movesTakingPiece.append((new_row, new_col))
                        break
                else:
                    break

        return movesTakingPiece, movesNotTakingPiece


class King(Piece):
    img = 1

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.firstMove = True

    def valid_moves(self, board):
        king_row = self.row
        king_col = self.col

        movesTakingPiece = []
        movesNotTakingPiece = []

        # Possible moves for a king
        move_offsets = [
            (-1 , -1), (-1 ,  0), (-1 ,  1),
            (0  , -1),            (0  ,  1),
            (1  , -1), (1  ,  0), (1  ,  1)
        ]

        for offset in move_offsets:
            new_row = king_row + offset[0]
            new_col = king_col + offset[1]

            # Check if the new position is on the board
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                possible_move = board[new_row][new_col]
                if possible_move is None:
                    movesNotTakingPiece.append((new_row, new_col))
                else:
                    if possible_move.color != self.color:
                        movesTakingPiece.append((new_row, new_col))

        if self.firstMove:
            if self.color == "B":
                # Short Castling
                if board[0][5] is None and board[0][6] is None and board[0][7].isRook:
                    movesNotTakingPiece.append((0, 6))
                # Long Castling
                if board[0][3] is None and board[0][2] is None and board[0][1] is None and board[0][0].isRook:
                    movesNotTakingPiece.append((0, 2))
            
            if self.color == "W":
                # Short Castling
                if board[7][5] is None and board[7][6] is None and board[7][7].isRook:
                    movesNotTakingPiece.append((7, 6))
                # Long Castling
                if board[7][3] is None and board[7][2] is None and board[7][1] is None and board[7][7].isRook:
                    movesNotTakingPiece.append((7, 2))

        return movesTakingPiece, movesNotTakingPiece


class Knight(Piece):
    img = 2

    def valid_moves(self, board):
        knight_row = self.row
        knight_col = self.col

        movesTakingPiece = []
        movesNotTakingPiece = []

        # Possible moves for a knight
        move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for offset in move_offsets:
            new_row = knight_row + offset[0]
            new_col = knight_col + offset[1]

            # Check if the new position is on the board
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                possible_move = board[new_row][new_col]
                if possible_move is None:
                    movesNotTakingPiece.append((new_row, new_col))
                else:
                    if possible_move.color != self.color:
                        movesTakingPiece.append((new_row, new_col))

        return movesTakingPiece, movesNotTakingPiece


class Pawn(Piece):
    img = 3

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.toggle = False
        self.firstMove = True  # This will be updated after the first move
        # TODO: Implement En passant

    def valid_moves(self, board):
        pawn_row = self.row
        pawn_col = self.col
        
        movesTakingPiece = []
        movesNotTakingPiece = []

        # Move logic for pawns
        if self.color == 'B':
            # Moving forward
            if board[pawn_row + 1][pawn_col] is None:
                movesNotTakingPiece.append((pawn_row + 1, pawn_col))
                # Double step for first move
                if self.firstMove and board[pawn_row + 2][pawn_col] is None:
                    movesNotTakingPiece.append((pawn_row + 2, pawn_col))

            # Capturing diagonally
            if 0 <= pawn_row + 1 < 8 and 0 <= pawn_col + 1 < 8 and board[pawn_row + 1][pawn_col + 1] is not None:
                if board[pawn_row + 1][pawn_col + 1].color != self.color:
                    movesTakingPiece.append((pawn_row + 1, pawn_col + 1))
            if 0 <= pawn_row + 1 < 8 and 0 <= pawn_col - 1 < 8 and board[pawn_row + 1][pawn_col - 1] is not None:
                if board[pawn_row + 1][pawn_col - 1].color != self.color:
                    movesTakingPiece.append((pawn_row + 1, pawn_col - 1))

        else:
            # Moving forward
            if board[pawn_row - 1][pawn_col] is None:
                movesNotTakingPiece.append((pawn_row - 1, pawn_col))
                # Double step for first move
                if self.firstMove and board[pawn_row - 2][pawn_col] is None:
                    movesNotTakingPiece.append((pawn_row - 2, pawn_col))

            # Capturing diagonally
            if 0 <= pawn_row - 1 < 8 and 0 <= pawn_col + 1 < 8 and board[pawn_row - 1][pawn_col + 1] is not None:
                if board[pawn_row - 1][pawn_col + 1].color != self.color:
                    movesTakingPiece.append((pawn_row - 1, pawn_col + 1))
            if 0 <= pawn_row - 1 < 8 and 0 <= pawn_col - 1 < 8 and board[pawn_row - 1][pawn_col - 1] is not None:
                if board[pawn_row -1][pawn_col - 1].color != self.color:
                    movesTakingPiece.append((pawn_row - 1, pawn_col - 1))

        # Promotion check
        if (self.row == 6 and self.color == 'B') or (self.row == 1 and self.color == 'W'):
            print("Choose Between Queen, Rook, Bishop, and Knight. Type your option: ")
            # TODO: Implementing the promotion logic here

        return movesTakingPiece, movesNotTakingPiece


class Queen(Piece):
    img = 4

    def __init__(self, row, col, color):
        super().__init__(row, col, color);
        self.firstMove = True

    def valid_moves(self, board):
        queen_row = self.row
        queen_col = self.col

        movesTakingPiece = []
        movesNotTakingPiece = []

        # Directions for queen's movement
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Straight lines: up, down, left, right
            (-1, 1), (1, -1), (1, 1), (-1, -1)  # Diagonals: up-right, down-left, down-right, up-left
        ]

        for direction in directions:
            row_increment, col_increment = direction
            for i in range(1, 8):
                new_row = queen_row + i * row_increment
                new_col = queen_col + i * col_increment

                # Check if the new position is on the board
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    possible_move = board[new_row][new_col]

                    if possible_move is None:
                        movesNotTakingPiece.append((new_row, new_col))
                    else:
                        if possible_move.color != self.color:
                            movesTakingPiece.append((new_row, new_col))
                        break
                else:
                    break

        return movesTakingPiece, movesNotTakingPiece


class Rook(Piece):
    img = 5

    def valid_moves(self, board):
        rook_row = self.row
        rook_col = self.col

        movesTakingPiece = []
        movesNotTakingPiece = []

        # Right
        for col in range(rook_col + 1, 8):
            if board[rook_row][col] is None:
                movesNotTakingPiece.append((rook_row, col))
            else:
                if board[rook_row][col].color != self.color:
                    movesTakingPiece.append((rook_row, col))
                break  # Stop if encounter a piece
        # Left
        for col in range(rook_col - 1, -1, -1):
            if board[rook_row][col] is None:
                movesNotTakingPiece.append((rook_row, col))
            else:
                if board[rook_row][col].color != self.color:
                    movesTakingPiece.append((rook_row, col))
                break  # Stop if encounter a piece
        # Up
        for row in range(rook_row - 1, -1, -1):
            if board[row][rook_col] is None:
                movesNotTakingPiece.append((row, rook_col))
            else:
                if board[row][rook_col].color != self.color:
                    movesTakingPiece.append((row, rook_col))
                break  # Stop if encounter a piece
        # Down
        for row in range(rook_row + 1, 8):
            if board[row][rook_col] is None:
                movesNotTakingPiece.append((row, rook_col))
            else:
                if board[row][rook_col].color != self.color:
                    movesTakingPiece.append((row, rook_col))
                break  # Stop if encounter a piece
        
        return movesTakingPiece, movesNotTakingPiece
