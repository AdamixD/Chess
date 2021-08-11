from Figures.Figure import Figure
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
from Game_GUI import Game_Gui
import pygame

WIDTH, HEIGHT = 500, 500
M_WIDTH, M_HEIGHT = 300, 200

FIELD_SIZE = 60

BASIC_GREEN = (119, 149, 86)
BASIC_WHITE = (235, 236, 208)
WHITE_CIRCLE = (214, 214, 189)
GREEN_CIRCLE = (106, 135, 77)
MAIN_COLOR = (55, 55, 55)

def drawBoard(display, chackmate_king_pos):
    for i in range(8):
        font = pygame.font.SysFont('arial', 15)
        label = font.render(str(i+1), 0.5, (206, 206, 206))
        display.blit(label, (485, 15 + FIELD_SIZE*i))
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(display, pygame.Color(BASIC_WHITE), pygame.Rect(i*FIELD_SIZE, j*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
            else:
                pygame.draw.rect(display, pygame.Color(BASIC_GREEN), pygame.Rect(i*FIELD_SIZE, j*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
            if i == 7:
                font = pygame.font.SysFont('arial', 15)
                label = font.render(chr(97+j), 0.5, (206, 206, 206))
                display.blit(label, (45 + FIELD_SIZE*j, 480))
    if len(chackmate_king_pos):
        pygame.draw.rect(display, pygame.Color("Red"), pygame.Rect(chackmate_king_pos[1]*FIELD_SIZE, chackmate_king_pos[0]*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))

def drawFigures(display, array, next_fields_list=[]):
    for field in next_fields_list:
        field_x = field[1]
        field_y = field[0]
        x = (field_x + 1/2)*FIELD_SIZE
        y = (field_y + 1/2)*FIELD_SIZE
        color = WHITE_CIRCLE
        if (field_x + field_y)%2 != 0:
            color = GREEN_CIRCLE

        if array[field_y][field_x].get_name() == " ":
            pygame.draw.circle(display, pygame.Color(color), (x, y), 10)
        else:
            pygame.draw.circle(display, pygame.Color(color), (x, y), 30, 5)

    for i in range(8):
        for j in range(8):
            figure = array[j][i]
            if figure.get_name() != " ":
                image = pygame.image.load(figure.get_picture())
                display.blit(image, (i*FIELD_SIZE, j*FIELD_SIZE))

def drawCheckmateWindow(display, message):
    pygame.draw.rect(display, pygame.Color(MAIN_COLOR), pygame.Rect(WIDTH//2 - M_WIDTH//2, HEIGHT//2 - M_HEIGHT//2, M_WIDTH, M_HEIGHT))
    FONT_SIZE = 20
    font = pygame.font.SysFont('arial', FONT_SIZE)
    label = font.render(message, 0.5, (206, 206, 206))

    display.blit(label, label.get_rect(center = display.get_rect().center))

def create_pos(click_pos):
    row = click_pos[1] // FIELD_SIZE
    col = click_pos[0] // FIELD_SIZE

    return [row, col]

def main():
    pygame.init()
    pygame.display.set_caption("Chess")
    display = pygame.display.set_mode((WIDTH, HEIGHT))

    program_icon = pygame.image.load('Images/program_icon.png')
    pygame.display.set_icon(program_icon)

    pygame.display.update()
    display.fill(pygame.Color(MAIN_COLOR))

    game = Game_Gui()
    open = True

    # is_move == True when white, == False when black
    is_move = True
    playerW = Player(True)
    playerB = Player(False)
    winner = None
    chackmate_king_pos = []

    first_click = []
    next_fields_list = []
    while open:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = pygame.mouse.get_pos()

                    if len(first_click) == 0:
                        pos = create_pos(click_pos)
                        if is_move:
                            if game.check_choosen_figure(playerW, pos):
                                next_fields_list = game.get_next_fields_list(pos)
                                first_click = click_pos
                        else:
                            if game.check_choosen_figure(playerB, pos):
                                next_fields_list = game.get_next_fields_list(pos)
                                first_click = click_pos
                    elif len(first_click) == 2:
                        old_pos = create_pos(first_click)
                        new_pos = create_pos(click_pos)

                        if game.check_move(old_pos, new_pos):
                            game.move(old_pos, new_pos)
                            if is_move:
                                is_move = False
                                if game.get_board().is_checkmate(False):
                                    winner = playerW
                                    chackmate_king_pos = game.get_board().get_kingB_position()
                                    game.set_winner_message("White won!!!")
                                    break
                            else:
                                is_move = True
                                if game.get_board().is_checkmate(True):
                                    winner = playerB
                                    chackmate_king_pos = game.get_board().get_kingW_position()
                                    game.set_winner_message("Black won!!!")
                                    break
                        first_click = []
                        next_fields_list = []

            elif event.type == pygame.QUIT:
                open = False

        drawBoard(display, chackmate_king_pos)
        drawFigures(display, game.get_board().get_array(), next_fields_list)
        pygame.display.flip()

        if len(chackmate_king_pos):
            drawCheckmateWindow(display, game.get_winner_message())
            pygame.display.flip()
            pygame.time.delay(5000)
            open = False


    pygame.quit()

if __name__ == "__main__":
    main()
