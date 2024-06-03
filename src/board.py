from src.piece import *
from src.constants import *

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

        self.board[0][0] = Rook  (0, 0, "B")
        self.board[0][1] = Knight(0, 1, "B")
        self.board[0][2] = Bishop(0, 2, "B")
        self.board[0][3] = Queen (0, 3, "B")
        self.board[0][4] = King  (0, 4, "B")
        self.board[0][5] = Bishop(0, 5, "B")
        self.board[0][6] = Knight(0, 6, "B")
        self.board[0][7] = Rook  (0, 7, "B")

        for col in range(cols):
            self.board[1][col] = Pawn(1, col, "B")
            self.board[6][col] = Pawn(6, col, "W")
            self.board[1][col].isPawn = True
            self.board[6][col].isPawn = True

        self.board[7][0] = Rook  (7, 0, "W")
        self.board[7][1] = Knight(7, 1, "W")
        self.board[7][2] = Bishop(7, 2, "W")
        self.board[7][3] = Queen (7, 3, "W")
        self.board[7][4] = King  (7, 4, "W")
        self.board[7][5] = Bishop(7, 5, "W")
        self.board[7][6] = Knight(7, 6, "W")
        self.board[7][7] = Rook  (7, 7, "W")

        self.board[0][4].isKing = True
        self.board[7][4].isKing = True
        self.board[0][0].isRook = (0, 1)
        self.board[7][7].isRook = (1, 0)
        self.board[0][7].isRook = (1, 0)
        self.board[7][0].isRook = (0, 1)

    def draw(self, win, board):
        global turn
        turn_text = font.render(f"Turn: {turn}", True, (255, 0, 0))
        win.blit(turn_text, (10, 10))

        for row in board:
            for piece in row:
                if piece:
                    piece.draw(win, board)
                    if piece.isPawn:
                        if piece.row > 1 and piece.color == "B":
                            piece.firstMove = False
                        if piece.row < 6 and piece.color == "W":
                            piece.firstMove = False
                    if piece.isKing:
                        if piece.color ==  "B":
                            if piece.row != 0 or piece.col != 4:
                                piece.firstMove = False
                        else:
                            if piece.row != 7 or piece.col != 4 and piece.color == "W":
                                piece.firstMove = False
                    if piece.isRook:
                        if piece.color == "W":
                            if piece.isRook[0] == 0:
                                if piece.row != 7 or piece.col != 7:
                                    piece.firstMove = False
                            else:
                                if piece.row != 7 or piece.col != 0:
                                    piece.firstMove = False
                        else:
                            if piece.isRook[0] == 0:
                                if piece.row != 0 or piece.col != 7:
                                    piece.firstMove = False
                            else:
                                if piece.row != 0 or piece.col != 0:
                                    piece.firstMove = False

    def select(self, row, col):
        global turn
        previous_selection = (None, None)

        for board_row in range(ROW):
            for board_col in range(COL):
                piece = self.board[board_row][board_col]
                if piece and piece.selected:
                    if piece.color == turn:
                        previous_selection = [board_row, board_col]

        previous_row, previous_col = previous_selection

        if previous_row is not None and previous_col is not None and self.board[previous_row][previous_col].color == turn and not self.board[previous_row][previous_col].isKing:
            if row == previous_row and col == previous_col:
                # Deselect the currently selected piece if clicked again
                self.board[row][col].selected = False
            else:
                if self.board[previous_row][previous_col].availableMovesTakingPiece:
                    if (row, col) in self.board[previous_row][previous_col].availableMovesTakingPiece:
                        self.deselect_all()
                        self.move(previous_row, previous_col, row, col)
                        if turn == "B":
                            turn = "W"
                        else:
                            turn = "B"
                        return 
                if self.board[previous_row][previous_col].availableMovesNotTakingPiece:
                    if (row, col) in self.board[previous_row][previous_col].availableMovesNotTakingPiece:
                        self.deselect_all()
                        self.move(previous_row, previous_col, row, col)
                        if turn == "B":
                            turn = "W"
                        else:
                            turn = "B"
                        return
                if self.board[previous_row][previous_col].availableMovesTakingPiece or self.board[previous_row][previous_col].availableMovesNotTakingPiece or ["Something"] and self.board[previous_row][previous_col].color == turn:
                    # Deselect all pieces and select the new piece
                    self.deselect_all()
                    self.select_piece(row, col)
        elif  previous_row is not None and previous_col is not None and self.board[previous_row][previous_col].color == turn and self.board[previous_row][previous_col].isKing:
            if self.board[previous_row][previous_col].firstMove:
                self.deselect_all()
                self.move(previous_row, previous_col, row, col)

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
                
                if col == 6:
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

                if turn == "B":
                    turn = "W"
                else:
                    turn = "B"
                return
            else:
                self.deselect_all()
                self.move(previous_row, previous_col, row, col)
                if turn == "B":
                    turn = "W"
                else:
                    turn = "B"
                return

        else:
            # If no piece was previously selected, just select the new piece
            self.deselect_all()
            self.select_piece(row, col)

    def deselect_all(self):
        for board_row in self.board:
            for piece in board_row:
                if piece is not None:
                    piece.selected = False

    def select_piece(self, row, col):
        global run
        count = 0
        if self.board[row][col] is not None and not self.king_checkmate()[-1]:
            self.board[row][col].selected = True

        if self.board[row][col] is not None and self.king_checkmate()[-1]:
            game_over = False

            while not game_over:
                moves_take = self.board[row][col].availableMovesTakingPiece
                moves_not_take = self.board[row][col].availableMovesNotTakingPiece
                moves = moves_take + moves_not_take

                if self.board[row][col].color == turn:
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
                                self.board[row][col].check = [move]
                            count += 1
                            break

                        self.board[row][col] = temp1
                        self.board[move[0]][move[1]] = temp2

                game_over = True
        if count == 0:
            run = False
                
            
    def move(self, current_row, current_col, to_go_row, to_go_col):
        global turn
        if not self.board[to_go_row][to_go_col]:
            self.board[to_go_row][to_go_col] = self.board[current_row][current_col]
            self.board[current_row][current_col] = None
            self.board[to_go_row][to_go_col].selected = False
            self.board[to_go_row][to_go_col].row = to_go_row
            self.board[to_go_row][to_go_col].col = to_go_col
        else:
            if not self.board[to_go_row][to_go_col].isKing:
                self.board[to_go_row][to_go_col] = self.board[current_row][current_col]
                self.board[current_row][current_col] = None
                self.board[to_go_row][to_go_col].selected = False
                self.board[to_go_row][to_go_col].row = to_go_row
                self.board[to_go_row][to_go_col].col = to_go_col
            else:
                if turn == "B":
                    turn = "W"
                else:
                    turn = "B"

    def king_checkmate(self):
        w_king = (None, None)
        b_king = (None, None)
        for board_row in range(ROW):
            for board_col in range(COL):
                if self.board[board_row][board_col]:
                    if self.board[board_row][board_col].isKing:
                        if self.board[board_row][board_col].color == "W":
                            w_king = (board_row, board_col)
                        else:
                            b_king = (board_row, board_col)

        for board_row in range(ROW):
            for board_col in range(COL):
                if self.board[board_row][board_col]:
                    availableMovesTakingPiece, _ = self.board[board_row][board_col].valid_moves(self.board)
                    if w_king in availableMovesTakingPiece:
                        return "W", True
                    if b_king in availableMovesTakingPiece:
                        return "B", True

        return "WB", False
