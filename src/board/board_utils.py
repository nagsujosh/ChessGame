# from typing import Optional, List
# from pygame.surface import Surface
# from src.pieces import Piece, Rook, Knight, Bishop, Queen, King, Pawn
# from src.constants import font
#
#
# def draw_turn_indicator(piece, win: Surface) -> None:
#     global turn
#     turn_text = font.render(f"Turn: {turn}", True, (255, 0, 0))
#     win.blit(turn_text, (10, 10))
#
#
# def update_first_move_flags(piece, piece: Piece) -> None:
#     if piece.is_pawn:
#         if piece.first_move:
#             piece.update_pawn_first_move(piece)
#         piece.promotion_check(piece)
#     elif piece.is_king:
#         if piece.first_move:
#             piece.update_king_first_move(piece)
#     elif isinstance(piece.is_rook, tuple):
#         if piece.first_move:
#             piece.update_rook_first_move(piece)
#
#
# def promotion_check(piece, piece: Piece) -> None:
#     color = piece.color
#     if (color == "B" and piece.row == 7) or (color == "W" and piece.row == 0):
#         print(f"Choose your promotion piece between Queen, Rook, Knight, and Bishop for {color}: ")
#         while True:
#             name = input().strip().lower()
#             if name in ['queen', 'rook', 'bishop', 'knight']:
#                 promotion_row = piece.row
#                 promotion_col = piece.col
#                 promoted_piece = None
#                 if name == 'queen':
#                     promoted_piece = Queen(promotion_row, promotion_col, color)
#                 elif name == 'rook':
#                     promoted_piece = Rook(promotion_row, promotion_col, color)
#                     promoted_piece.is_rook = True  # Example of setting an attribute
#                 elif name == 'bishop':
#                     promoted_piece = Bishop(promotion_row, promotion_col, color)
#                 else:
#                     promoted_piece = Knight(promotion_row, promotion_col, color)
#
#                 if promoted_piece:
#                     piece.piece[promotion_row][promotion_col] = promoted_piece
#                     break
#             else:
#                 print("Invalid input. Please choose Queen, Rook, Bishop, or Knight.")
#
#
# def update_pawn_first_move(piece, piece: Piece) -> None:
#     if piece.row > 1 and piece.color == "B":
#         piece.first_move = False
#     elif piece.row < 6 and piece.color == "W":
#         piece.first_move = False
#
#
# def update_king_first_move(piece, piece: Piece) -> None:
#     if piece.color == "B":
#         if piece.row != 0 or piece.col != 4:
#             piece.first_move = False
#     elif piece.color == "W":
#         if piece.row != 7 or piece.col != 4:
#             piece.first_move = False
#
#
# def update_rook_first_move(piece, piece: Piece) -> None:
#     if piece.color == "W":
#         if not piece.is_rook[1]:
#             if piece.first_move:
#                 if piece.row != 7 or piece.col != 7:
#                     piece.first_move = False
#         else:
#             if piece.first_move:
#                 if piece.row != 7 or piece.col != 0:
#                     piece.first_move = False
#     else:
#         if not piece.is_rook[1]:
#             if piece.first_move:
#                 if piece.row != 0 or piece.col != 7:
#                     piece.first_move = False
#         else:
#             if piece.first_move:
#                 if piece.row != 0 or piece.col != 0:
#                     piece.first_move = False
