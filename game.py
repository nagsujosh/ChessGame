import pygame
from src.board import Board
from src.constants import *
from src.game_utils import redraw_game_window, click

def main():
    # Initialize Pygame
    pygame.init()

    # Set the window title and icon
    pygame.display.set_caption("Chess Game")
    pygame.display.set_icon(icon)

    # Create a clock object to manage the frame rate
    clock = pygame.time.Clock()

    # Initialize the Board object
    board = Board(ROW, COL)

    global run
    # Main game loop
    while run:
        # Cap the frame rate
        clock.tick(FPS)

        # Redraw the game window
        redraw_game_window(win, board_img, board)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                result = click(position, BOARD_RECT)
                if result:
                    board.select(*result)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
