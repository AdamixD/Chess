from Figures.Knight import Knight
from Figures.Rook import Rook
from Figures.King import King
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Bishop import Bishop
from Figures.EmptyField import EmptyField
from Board import Board
from Player import Player
from time import time

import pygame

WIDTH, HEIGHT = 420, 420
FIELD_SIZE = 60

def drawBoard(display):
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(display, pygame.Color("white"), pygame.Rect(i*FIELD_SIZE, j*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
            else:
                pygame.draw.rect(display, pygame.Color("green"), pygame.Rect(i*FIELD_SIZE, j*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))

def main():
    pygame.init()

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()
    display.fill(pygame.Color('white'))

    open = True
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open = False
        drawBoard(display)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
