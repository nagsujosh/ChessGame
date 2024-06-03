import pygame
import os

# Screen Dimensions
# TODO: Dynamic Screen Size based on user settings
WIDTH = 750
HEIGHT = 750

# Frames per Second
FPS = 30

# Board Dimensions and Coordinates
# TODO: Dynamic Dimension for the board
BOARD_RECT = (113, 113, 525, 525)

# Number of Rows and Columns on the Board
ROW = 8
COL = 8

# Piece Dimensions
PIECE_DIMENSION = (55, 55)

# Load Images of Black Pieces
b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

# Load Images of White Pieces
w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

# Lists of Black and White Pieces
b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

# Scale Images to Fit the Board
B = [pygame.transform.scale(img, PIECE_DIMENSION) for img in b]
W = [pygame.transform.scale(img, PIECE_DIMENSION) for img in w]

# Load and Scale Board Image
board_img = pygame.transform.scale(pygame.image.load(os.path.join("img", "board_alt.png")), (WIDTH, HEIGHT))

# Initialize Game Window
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Load Game Icon
icon = pygame.image.load(os.path.join("img", "board.png"))

turn = "W"

pygame.font.init()
font = pygame.font.Font(None, 32)

run = True
