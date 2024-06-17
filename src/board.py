from typing import List, Optional, Tuple
from src.pieces import *
from src.constants import *
from pygame.surface import Surface


class Board:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.board: List[List[Optional[Piece]]] = [[None for _ in range(cols)] for _ in range(rows)]

        # Initialize black pieces
        self.board[0][0] = Rook(0, 0, "B")
        self.board[0][1] = Knight(0, 1, "B")
        self.board[0][2] = Bishop(0, 2, "B")
        self.board[0][3] = Queen(0, 3, "B")
        self.board[0][4] = King(0, 4, "B")
        self.board[0][5] = Bishop(0, 5, "B")
        self.board[0][6] = Knight(0, 6, "B")
        self.board[0][7] = Rook(0, 7, "B")

        for col in range(cols):
            self.board[1][col] = Pawn(1, col, "B")
            self.board[1][col].is_pawn = True

        # Initialize white pieces
        self.board[7][0] = Rook(7, 0, "W")
        self.board[7][1] = Knight(7, 1, "W")
        self.board[7][2] = Bishop(7, 2, "W")
        self.board[7][3] = Queen(7, 3, "W")
        self.board[7][4] = King(7, 4, "W")
        self.board[7][5] = Bishop(7, 5, "W")
        self.board[7][6] = Knight(7, 6, "W")
        self.board[7][7] = Rook(7, 7, "W")

        for col in range(cols):
            self.board[6][col] = Pawn(6, col, "W")
            self.board[6][col].is_pawn = True

        # Set additional attributes for kings and rooks
        self.board[0][4].is_king = True
        self.board[7][4].is_king = True

        # Here in the tuple the first value indicates this the piece is a rook and
        # the second element indicates that the rook is from the left side
        self.board[0][0].is_rook = (True, True)
        self.board[7][0].is_rook = (True, True)
        self.board[7][7].is_rook = (True, False)
        self.board[0][7].is_rook = (True, False)

    def draw(self, win: Surface, board: List[List[Optional[Piece]]]) -> None:
        global turn
        self.draw_turn_indicator(win)
        for row in board:
            for piece in row:
                if piece:
                    piece.draw(win, board)
                    self.update_first_move_flags(piece)

    def draw_turn_indicator(self, win: Surface) -> None:
        global turn
        turn_text = font.render(f"Turn: {turn}", True, (255, 0, 0))
        win.blit(turn_text, (10, 10))

    def update_first_move_flags(self, piece: Piece) -> None:
        if piece.is_pawn:
            if piece.first_move:
                self.update_pawn_first_move(piece)
            self.promotion_check(piece)
        elif piece.is_king:
            if piece.first_move:
                self.update_king_first_move(piece)
        elif isinstance(piece.is_rook, tuple):
            if piece.first_move:
                self.update_rook_first_move(piece)

    def promotion_check(self, piece: Piece) -> None:
        color = piece.color
        if (color == "B" and piece.row == 7) or (color == "W" and piece.row == 0):
            print(f"Choose your promotion piece between Queen, Rook, Knight, and Bishop for {color}: ")
            while True:
                name = input().strip().lower()
                if name in ['queen', 'rook', 'bishop', 'knight']:
                    promotion_row = piece.row
                    promotion_col = piece.col
                    promoted_piece = None
                    if name == 'queen':
                        promoted_piece = Queen(promotion_row, promotion_col, color)
                    elif name == 'rook':
                        promoted_piece = Rook(promotion_row, promotion_col, color)
                        promoted_piece.is_rook = True  # Example of setting an attribute
                    elif name == 'bishop':
                        promoted_piece = Bishop(promotion_row, promotion_col, color)
                    else:
                        promoted_piece = Knight(promotion_row, promotion_col, color)

                    if promoted_piece:
                        self.board[promotion_row][promotion_col] = promoted_piece
                        break
                else:
                    print("Invalid input. Please choose Queen, Rook, Bishop, or Knight.")

    def update_pawn_first_move(self, piece: Piece) -> None:
        if piece.row > 1 and piece.color == "B":
            piece.first_move = False
        elif piece.row < 6 and piece.color == "W":
            piece.first_move = False

    def update_king_first_move(self, piece: Piece) -> None:
        if piece.color == "B":
            if piece.row != 0 or piece.col != 4:
                piece.first_move = False
        elif piece.color == "W":
            if piece.row != 7 or piece.col != 4:
                piece.first_move = False

    def update_rook_first_move(self, piece: Piece) -> None:
        if piece.color == "W":
            if not piece.is_rook[1]:
                if piece.first_move:
                    if piece.row != 7 or piece.col != 7:
                        piece.first_move = False
            else:
                if piece.first_move:
                    if piece.row != 7 or piece.col != 0:
                        piece.first_move = False
        else:
            if not piece.is_rook[1]:
                if piece.first_move:
                    if piece.row != 0 or piece.col != 7:
                        piece.first_move = False
            else:
                if piece.first_move:
                    if piece.row != 0 or piece.col != 0:
                        piece.first_move = False

    def select(self, row: int, col: int) -> None:
        global turn

        # Previous Selection will be used when already one piece is selected and to get that piece
        previous_selection: Tuple[Optional[int], Optional[int]] = (None, None)

        for board_row in range(self.rows):
            for board_col in range(self.cols):
                piece = self.board[board_row][board_col]
                if piece and piece.selected and piece.color == turn:
                    previous_selection = (board_row, board_col)

        previous_row, previous_col = previous_selection

        # Takes care of the selection process to make good selection decision
        if self.board[row][col]:
            if self.board[row][col].color == turn:
                pass
            else:
                if (previous_col is not None and previous_row is not None
                        and self.board[previous_row][previous_col].color == turn):
                    if (row, col) in self.board[previous_row][previous_col].available_moves_taking_piece:
                        pass
                    else:
                        return
                else:
                    return

        if (previous_row is not None and previous_col is not None and
                self.board[previous_row][previous_col].color == turn and
                not self.board[previous_row][previous_col].is_king):
            # Deselect Feature
            if row == previous_row and col == previous_col:
                self.board[row][col].selected = False
            else:
                if self.board[previous_row][previous_col].available_moves_taking_piece:
                    if (row, col) in self.board[previous_row][previous_col].available_moves_taking_piece:
                        self.deselect_all()
                        self.move(previous_row, previous_col, row, col)
                        turn = "W" if turn == "B" else "B"
                        return
                if self.board[previous_row][previous_col].available_moves_not_taking_piece:
                    if (row, col) in self.board[previous_row][previous_col].available_moves_not_taking_piece:
                        self.deselect_all()
                        self.move(previous_row, previous_col, row, col)
                        turn = "W" if turn == "B" else "B"
                        return
                # Handling the case when already one piece is selecting, but you want to select another one
                if (self.board[previous_row][previous_col].available_moves_taking_piece or
                    self.board[previous_row][previous_col].available_moves_not_taking_piece or
                    ["Something"] and self.board[previous_row][previous_col].color == turn):
                    self.deselect_all()
                    self.select_piece(row, col)
        elif (previous_row is not None and previous_col is not None and
              self.board[previous_row][previous_col].color == turn and
              self.board[previous_row][previous_col].is_king):
            if self.board[previous_row][previous_col].first_move:

                if col == 2:
                    if turn == "B":
                        self.board[0][3] = self.board[0][0]
                        self.board[0][0] = None
                        self.board[0][3].row = 0
                        self.board[0][3].col = 3
                    else:
                        self.board[7][3] = self.board[7][0]
                        self.board[7][0] = None
                        self.board[7][3].row = 7
                        self.board[7][3].col = 3
                    self.deselect_all()
                    self.move(previous_row, previous_col, row, col)

                elif col == 6:
                    if turn == "B":
                        self.board[0][5] = self.board[0][7]
                        self.board[0][7] = None
                        self.board[0][5].row = 0
                        self.board[0][5].col = 5
                    else:
                        self.board[7][5] = self.board[7][7]
                        self.board[7][7] = None
                        self.board[7][5].row = 7
                        self.board[7][5].col = 5

                    self.deselect_all()
                    self.move(previous_row, previous_col, row, col)
                    turn = "W" if turn == "B" else "B"
                    return
                else:
                    if self.board[previous_row][previous_col].available_moves_taking_piece:
                        if (row, col) in self.board[previous_row][previous_col].available_moves_taking_piece:
                            self.deselect_all()
                            self.move(previous_row, previous_col, row, col)
                            turn = "W" if turn == "B" else "B"
                            return
                    if self.board[previous_row][previous_col].available_moves_not_taking_piece:
                        if (row, col) in self.board[previous_row][previous_col].available_moves_not_taking_piece:
                            self.deselect_all()
                            self.move(previous_row, previous_col, row, col)
                            turn = "W" if turn == "B" else "B"
                            return
                    if (self.board[previous_row][previous_col].available_moves_taking_piece or
                            self.board[previous_row][previous_col].available_moves_not_taking_piece or
                            ["Something"] and self.board[previous_row][previous_col].color == turn):
                        self.deselect_all()
                        self.select_piece(row, col)
            else:
                self.deselect_all()
                self.move(previous_row, previous_col, row, col)
                turn = "W" if turn == "B" else "B"
                return

        else:
            self.deselect_all()
            self.select_piece(row, col)

    def deselect_all(self) -> None:
        for board_row in self.board:
            for piece in board_row:
                if piece is not None:
                    piece.selected = False

    def select_piece(self, row: int, col: int) -> None:
        global run
        count = 0
        if self.board[row][col] is not None and not self.king_checkmate()[-1]:
            self.board[row][col].selected = True

        if self.board[row][col] is not None and self.king_checkmate()[-1]:
            game_over = False

            while not game_over:
                moves_take = self.board[row][col].available_moves_taking_piece
                moves_not_take = self.board[row][col].available_moves_not_taking_piece
                moves = moves_take + moves_not_take

                if self.board[row][col].color == turn:
                    temp1 = None
                    temp2 = None

                    for move in moves:
                        temp1 = self.board[row][col]
                        temp2 = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = self.board[row][col]
                        self.board[row][col] = None

                        if not self.king_checkmate()[-1]:
                            self.board[row][col] = temp1
                            self.board[row][col].selected = True
                            self.board[move[0]][move[1]] = temp2

                        if move in moves_take:
                            self.board[row][col].check = [move]
                        else:
                            self.board[move[0]][move[1]] = None
                            print(row, col)
                            self.board[row][col].check = [move]
                        count += 1
                        break

                    if temp1 is not None and temp2 is not None:
                        self.board[row][col] = temp1
                        self.board[move[0]][move[1]] = temp2
                    else:
                        print("King is checked mate")
                        run = False
                        break

                game_over = True
        if count == 0:
            run = False

    def move(self, current_row: int, current_col: int, to_go_row: int, to_go_col: int) -> None:
        global turn
        if not self.board[to_go_row][to_go_col]:
            self.board[to_go_row][to_go_col] = self.board[current_row][current_col]
            self.board[current_row][current_col] = None
            self.board[to_go_row][to_go_col].selected = False
            self.board[to_go_row][to_go_col].row = to_go_row
            self.board[to_go_row][to_go_col].col = to_go_col
        else:
            if not self.board[to_go_row][to_go_col].is_king:
                self.board[to_go_row][to_go_col] = self.board[current_row][current_col]
                self.board[current_row][current_col] = None
                self.board[to_go_row][to_go_col].selected = False
                self.board[to_go_row][to_go_col].row = to_go_row
                self.board[to_go_row][to_go_col].col = to_go_col
            else:
                turn = "W" if turn == "B" else "B"

    def king_checkmate(self) -> Tuple[str, bool]:
        w_king: Tuple[Optional[int], Optional[int]] = (None, None)
        b_king: Tuple[Optional[int], Optional[int]] = (None, None)

        # Getting the position of the two kings
        for board_row in range(self.rows):
            for board_col in range(self.cols):
                if self.board[board_row][board_col]:
                    if self.board[board_row][board_col].is_king:
                        if self.board[board_row][board_col].color == "W":
                            w_king = (board_row, board_col)
                        else:
                            b_king = (board_row, board_col)

        for board_row in range(self.rows):
            for board_col in range(self.cols):
                if self.board[board_row][board_col]:
                    available_moves_taking_piece, _ = self.board[board_row][board_col].valid_moves(self.board)
                    if w_king in available_moves_taking_piece:
                        return "W", True
                    if b_king in available_moves_taking_piece:
                        return "B", True

        return "WB", False
