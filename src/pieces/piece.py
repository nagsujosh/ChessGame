import pygame
from pygame.surface import Surface
from typing import List, Tuple, Optional
from src.constants import *


class Piece:
    img: int = None

    start_x: int = BOARD_RECT[0]
    start_y: int = BOARD_RECT[1]

    def __init__(self, row: int, col: int, color: str) -> None:
        self.row: int = row
        self.col: int = col
        self.color: str = color
        self.selected: bool = False
        self.available_moves_not_taking_piece: Optional[List[Tuple[int, int]]] = None
        self.available_moves_taking_piece: Optional[List[Tuple[int, int]]] = None
        self.check: Optional[List[Tuple[int, int]]] = None  # Stores possible checks of this piece
        self.is_king: bool = False
        self.is_pawn: bool = False
        self.is_rook: Optional[Tuple[int, int]] = None

    def is_selected(self) -> bool:
        return self.selected

    def valid_moves(self, board: List[List[Optional['Piece']]]) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
        # Placeholder for valid moves calculation
        return None, None

    def draw(self, window: Surface, board: List[List[Optional['Piece']]]) -> None:
        global turn

        self.available_moves_taking_piece, self.available_moves_not_taking_piece = self.valid_moves(board)

        # Getting the image for the piece to draw
        piece = W[self.img] if self.color == 'W' else B[self.img]

        # Coordinates for the rectangle for selecting a piece
        selected_rect_x = self.start_x + self.col * BOARD_RECT[2] // 8 + 5
        selected_rect_y = self.start_y + self.row * BOARD_RECT[3] // 8 + 5

        # Coordinates for the piece which is going to be drawn
        piece_x = self.start_x + self.col * BOARD_RECT[2] // 8 + 7
        piece_y = self.start_y + self.row * BOARD_RECT[3] // 8 + 5

        # Drawing the Pick Square if the piece is selected
        if self.selected:
            pygame.draw.rect(window, (255, 0, 0), (selected_rect_x, selected_rect_y, 60, 60), width=3)

        # Drawing the whole piece
        window.blit(piece, (piece_x, piece_y))

        if self.selected:
            if self.available_moves_not_taking_piece and not self.check:
                for move in self.available_moves_not_taking_piece:
                    circle_x = self.start_x + move[1] * BOARD_RECT[2] // 8 + 33
                    circle_y = self.start_y + move[0] * BOARD_RECT[3] // 8 + 33

                    pygame.draw.circle(window, (255, 0, 0), (circle_x, circle_y), 10)

            if self.available_moves_taking_piece and not self.check:
                for move in self.available_moves_taking_piece:
                    rect_x = self.start_x + move[1] * BOARD_RECT[2] // 8 + 5
                    rect_y = self.start_y + move[0] * BOARD_RECT[3] // 8 + 5

                    pygame.draw.rect(window, (0, 255, 0), (rect_x, rect_y, 60, 60), width=3)

            if self.check:
                for move in self.check:
                    circle_x = self.start_x + move[1] * BOARD_RECT[2] // 8 + 33
                    circle_y = self.start_y + move[0] * BOARD_RECT[3] // 8 + 33

                    pygame.draw.circle(window, (255, 0, 0), (circle_x, circle_y), 10)
