import pygame
from pygame.surface import Surface
from typing import Tuple, Optional


def redraw_game_window(win: Surface, board_img: Surface, board) -> None:
    """
    Redraw the game window.

    :param win: Pygame window surface.
    :param board_img: Pygame surface for the board image.
    :param board: Board object.
    """
    win.blit(board_img, (0, 0))
    board.draw(win, board.board)
    pygame.display.update()


def click(pos: Tuple[int, int], rect: Tuple[int, int, int, int]) -> Optional[Tuple[int, int]]:
    """
    Convert pixel coordinates to board coordinates.

    :param pos: (x, y) position in pixels.
    :param rect: (x, y, width, height) of the board area.
    :return: (row, col) in range 0-7 or None if out of bounds.
    """
    x, y = pos
    if rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]:
        row = (y - rect[1]) // (rect[3] // 8)
        col = (x - rect[0]) // (rect[2] // 8)
        return row, col
    return None
