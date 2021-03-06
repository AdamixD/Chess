from pygame import color
from History.file_functions import write_to_file
from typing import Counter
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
import time
import math
import copy
from Game_GUI import Game_Gui
from Button import Button
from History.file_functions import write_to_file
from SoundsPlayer import play_sound
import Time
import pygame


WIDTH, HEIGHT = 920, 510
M_WIDTH, M_HEIGHT = 300, 200
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 90
DIALOG_WIN_HEIGHT = 250
DIALOG_WIN_WIDTH = 200

MAIN_FONT = "trebuc.ttf"
FIELD_SIZE = 60
S_WIDTH = 8*FIELD_SIZE + FIELD_SIZE//2 + 20

BASIC_GREEN = (119, 149, 86)
BASIC_WHITE = (235, 236, 208)
CHESS_WHITE = (236 ,236, 236)
WHITE_CIRCLE = (214, 214, 189)
GREEN_CIRCLE = (106, 135, 77)
MAIN_COLOR = (44, 44, 44)
CONTOUR_COLOR = (55, 45, 45)
BROWN_WIN_COLOR = (36, 36, 36)

GAME_TIME = 0
QUIT_CONST = [False, ""]

# Draw ################################
def draw_launch_background(display):
    background_image = pygame.image.load("Images/background.jpg")
    logo_image = pygame.image.load("Images/new_logo.png")
    display.blit(background_image, (0, 0))
    display.blit(logo_image, (550, 50))

def dialog_window(display):
    draw_launch_background(display)
    window_image = pygame.image.load("Images/dialog_win.png")
    display.blit(window_image, ((WIDTH - DIALOG_WIN_WIDTH)//2, (HEIGHT - DIALOG_WIN_HEIGHT)//2 + 50))

    one_button = Button("Images/one_no.png", "Images/one_yes.png", [(WIDTH - DIALOG_WIN_WIDTH)//2, (HEIGHT - DIALOG_WIN_HEIGHT)//2 + 120], [200, 35])
    five_button = Button("Images/five_no.png", "Images/five_yes.png", [(WIDTH - DIALOG_WIN_WIDTH)//2, (HEIGHT - DIALOG_WIN_HEIGHT)//2 + 155], [200, 35])
    ten_button = Button("Images/ten_no.png", "Images/ten_yes.png", [(WIDTH - DIALOG_WIN_WIDTH)//2, (HEIGHT - DIALOG_WIN_HEIGHT)//2 + 190], [200, 35])
    unlimited_button = Button("Images/unlimited_no.png", "Images/unlimited_yes.png", [(WIDTH - DIALOG_WIN_WIDTH)//2, (HEIGHT - DIALOG_WIN_HEIGHT)//2 + 225], [200, 35])

    buttons = [one_button, five_button, ten_button, unlimited_button]
    values = [60, 300, 600, 1000]
    
    set_game_time(display, buttons, values)
    
def set_game_time(display, buttons, values):
    time_is_choosen = False
    time_value = None

    while not time_is_choosen:
        for i in range(4):
            buttons[i].draw(display)
            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range(4):
                        if buttons[i].check_click():
                            time_value = values[i]
                            time_is_choosen = True
                            break
            elif event.type == pygame.QUIT:
                time_is_choosen = True
                global QUIT_CONST
                QUIT_CONST[0] = True
                QUIT_CONST[1] = "Button"


    global GAME_TIME
    GAME_TIME = time_value

def draw_board(display, chackmate_king_pos, check_king_pos):
    for i in range(8):
        font = pygame.font.Font(MAIN_FONT, 15)
        label = font.render(str(i+1), 0.5, (206, 206, 206))
        display.blit(label, (15, 10 + FIELD_SIZE*i))
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(display, pygame.Color(BASIC_WHITE), pygame.Rect(i*FIELD_SIZE + FIELD_SIZE//2, j*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
            else:
                pygame.draw.rect(display, pygame.Color(BASIC_GREEN), pygame.Rect(i*FIELD_SIZE + FIELD_SIZE//2, j*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
            if i == 7:
                font = pygame.font.Font(MAIN_FONT, 15)
                label = font.render(chr(97+j), 0.5, (206, 206, 206))
                display.blit(label, (45 + FIELD_SIZE//2 + FIELD_SIZE*j, 480))

    if len(check_king_pos):
        pygame.draw.rect(display, pygame.Color("Orange"), pygame.Rect(check_king_pos[1]*FIELD_SIZE + FIELD_SIZE//2, check_king_pos[0]*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))

    if len(chackmate_king_pos):
        pygame.draw.rect(display, pygame.Color("Red"), pygame.Rect(chackmate_king_pos[1]*FIELD_SIZE + FIELD_SIZE//2, chackmate_king_pos[0]*FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))

def draw_figures(display, array, next_fields_list=[]):
    for field in next_fields_list:
        field_x = field[1]
        field_y = field[0]
        x = (field_x + 1/2)*FIELD_SIZE + FIELD_SIZE//2
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
                display.blit(image, (i*FIELD_SIZE + FIELD_SIZE//2, j*FIELD_SIZE))

def draw_end_game_window(display, result):
    if result == 0:
        image = pygame.image.load("Images/black_won.png")
    elif result == 1:
        image = pygame.image.load("Images/white_won.png")
    else:
        image = pygame.image.load("Images/draw.png")

    display.blit(image, (WIDTH//2 - M_WIDTH//2, HEIGHT//2 - M_HEIGHT//2, M_WIDTH, M_HEIGHT))

def new_game_function():
    pygame.time.delay(500)
    main()

def draw_pause_and_new_game_buttons(display, buttons):
    for button in buttons:
        button.draw(display)

def draw_chess_notation(display, notation):
    pygame.draw.rect(display, pygame.Color(BROWN_WIN_COLOR), pygame.Rect(S_WIDTH, 90, WIDTH-S_WIDTH - 20, 242))

    num = 0
    TEXT_X = S_WIDTH
    for i in range(0, len(notation) - len(notation) % 2, 2):
        if num % 16 == 0 and num > 1:
            TEXT_X += 125
        font = pygame.font.Font(MAIN_FONT, 15)
        label = font.render(f"{num+1}. {notation[i]} {notation[i+1]}", 0.5, CHESS_WHITE)
        display.blit(label, (TEXT_X, 90 + (num % 16)*15))
        num += 1

    if len(notation) % 2 == 1:
        if num % 16 == 0 and num > 1:
            TEXT_X += 120
        font = pygame.font.Font(MAIN_FONT, 15)
        label = font.render(f"{num+1}. {notation[len(notation)-1]}", 0.5, CHESS_WHITE)
        display.blit(label, (TEXT_X, 90 + (num % 16)*15))

def draw_time_box(display, player, position, path):
    box_image = pygame.image.load(path)
    time = math.floor(player.get_time())
    text = f" -- : --"
    if time != 1000:
        text = f"{time // 60:02} : {time % 60:02}"
    font = pygame.font.Font(MAIN_FONT, 15)
    color = MAIN_COLOR
    if not player.get_team():
        color = CHESS_WHITE
    label = font.render(text, 0.5, color)

    display.blit(box_image, (position[0], position[1]))
    display.blit(label, (position[0] + 5, position[1] + 5))

def draw_time_boxes(display, playerW, playerB):
    draw_time_box(display, playerW, [8*FIELD_SIZE + FIELD_SIZE//2 + 20, 7*FIELD_SIZE + FIELD_SIZE//2], "Images/white_time.png")
    draw_time_box(display, playerB, [8*FIELD_SIZE + FIELD_SIZE//2 + 20, 0], "Images/black_time.png")

def update_players_time(display, players, start_time, pause_time, is_move):
    playerW = players[0]
    playerB = players[1]
    
    if GAME_TIME == 1000:
        pass # unlimited
    elif is_move:
        opponent_time_move = playerB.get_const_time() - (start_time + playerB.get_time())
        player_time = playerW.get_const_time() - (time.time()) + pause_time + opponent_time_move
        playerW.set_time(player_time)
    else:
        opponent_time_move = playerW.get_const_time() - (start_time + playerW.get_time())
        player_time = playerB.get_const_time() - (time.time()) + pause_time + opponent_time_move
        playerB.set_time(player_time)

    draw_time_boxes(display, playerW, playerB)

def check_time_end(game, players):
    playerW = players[0]
    playerB = players[1]

    if playerW.get_time() <= 0 or playerB.get_time() <= 0:
        if playerB.get_time() <= 0:
            playerB.set_time(0)
            game.set_result(1)
        else:
            playerW.set_time(0)
            game.set_result(0)
        global QUIT_CONST
        QUIT_CONST[0] = True
        QUIT_CONST[1] = "Time"

def draw_broken_figure_window(display, team, pos, game):
    pygame.draw.rect(display, pygame.Color(BROWN_WIN_COLOR), pygame.Rect(pos[0], pos[1], 370, 50))
    index = 0
    if team:
        for figure in game.get_broken_figures_W():
            path = figure.get_picture()
            l = len(path)
            modified_path = path[:l-4] + "_m.png"
            image = pygame.image.load(modified_path)
            if index <= 13:
                display.blit(image, (S_WIDTH + (index % 14)*25, 35))
            else:
                display.blit(image, (S_WIDTH + (index % 14)*25, 60))
            index += 1

    else:
        for figure in game.get_broken_figures_B():
            path = figure.get_picture()
            l = len(path)
            modified_path = path[:l-4] + "_m.png"
            image = pygame.image.load(modified_path)
            if index <= 13:
                display.blit(image, (S_WIDTH + (index % 14)*25, 390))
            else:
                display.blit(image, (S_WIDTH + (index % 14)*25, 415))
            index += 1

def draw_broken_figures_windows(display, game):
    draw_broken_figure_window(display, True, [S_WIDTH, 35], game)
    draw_broken_figure_window(display, False, [S_WIDTH, 390], game)

def create_figure(name, team, pos):
    if name == "r":
        if team:
            new_figure = Rook("R", pos, "Images/Rook_W.png", True)
        else:
            new_figure = Rook("r", pos, "Images/Rook_B.png", False)
    elif name == "n":
        if team:
            new_figure = Knight("N", pos, "Images/Knight_W.png", True)
        else:
            new_figure = Knight("n", pos, "Images/Knight_B.png", False)
    elif name == "b":
        if team:
            new_figure = Bishop("B", pos, "Images/Bishop_W.png", True)
        else:
            new_figure = Bishop("b", pos, "Images/Bishop_B.png", False)
    else:
        if team:
            new_figure = Queen("Q", pos, "Images/Queen_W.png", True)
        else:
            new_figure= Queen("q", pos, "Images/Queen_B.png", False)

    return new_figure

def replacing_pawn(board, pawn):
    is_choosen = False
    while not is_choosen:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = pygame.mouse.get_pos()

                    if pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2 < click_pos[0] < (pawn.get_position()[1] + 1) * FIELD_SIZE + FIELD_SIZE//2:
                        if pawn.get_team():
                            list_of_pos = [1, 5]
                        else:
                            list_of_pos = [5, 9]
                            # I don't know how, but it is working (also line 149)
                        list_of_figures_names = ["n", "b", "q", "r"]


                        for i in range(list_of_pos[0], list_of_pos[1]):
                            if i - 1 * FIELD_SIZE< click_pos[1] < i * FIELD_SIZE:
                                # code for fun :)
                                new_figure_name = list_of_figures_names[i - list_of_pos[0] - 2]
                                #
                                new_figure = create_figure(new_figure_name, pawn.get_team(), pawn.get_position())
                                board.addFigure(new_figure)
                                is_choosen = True
                                break

def draw_pawn_converting_window(display, pawn):
    if pawn.get_team():
        pygame.draw.rect(display, pygame.Color(MAIN_COLOR), pygame.Rect(pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2 , 0 * FIELD_SIZE, FIELD_SIZE, 4 * FIELD_SIZE))

        queenW_image = pygame.image.load("Images/Queen_W.png")
        rookW_image = pygame.image.load("Images/Rook_W.png")
        knightW_image = pygame.image.load("Images/Knight_W.png")
        bishopW_image = pygame.image.load("Images/Bishop_W.png")

        display.blit(queenW_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 0 * FIELD_SIZE))
        display.blit(rookW_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 1 * FIELD_SIZE))
        display.blit(knightW_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 2 * FIELD_SIZE))
        display.blit(bishopW_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 3 * FIELD_SIZE))
    else:
        pygame.draw.rect(display, pygame.Color(MAIN_COLOR), pygame.Rect(pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 4 * FIELD_SIZE, FIELD_SIZE, 4 * FIELD_SIZE))

        queenB_image = pygame.image.load("Images/Queen_B.png")
        rookB_image = pygame.image.load("Images/Rook_B.png")
        knightB_image = pygame.image.load("Images/Knight_B.png")
        bishopB_image = pygame.image.load("Images/Bishop_B.png")

        display.blit(queenB_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 4 * FIELD_SIZE))
        display.blit(rookB_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 5 * FIELD_SIZE))
        display.blit(knightB_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 6 * FIELD_SIZE))
        display.blit(bishopB_image, (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, 7 * FIELD_SIZE))

    i_min = 0
    i_max = 4
    if not pawn.get_team():
        i_min = 4
        i_max = 8

    pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, i_min * FIELD_SIZE), ((pawn.get_position()[1] + 1) * FIELD_SIZE + FIELD_SIZE//2, i_min * FIELD_SIZE), 3)
    pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, i_min * FIELD_SIZE), (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, i_max * FIELD_SIZE), 3)
    pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), ((pawn.get_position()[1] + 1) * FIELD_SIZE + FIELD_SIZE//2, i_min * FIELD_SIZE), ((pawn.get_position()[1] + 1) * FIELD_SIZE + FIELD_SIZE//2, i_max * FIELD_SIZE), 3)
    pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), ((pawn.get_position()[1] + 1) * FIELD_SIZE + FIELD_SIZE//2, i_max * FIELD_SIZE), (pawn.get_position()[1] * FIELD_SIZE + FIELD_SIZE//2, i_max * FIELD_SIZE), 3)
    pygame.display.flip()

def create_pos(click_pos):
    row = click_pos[1]// FIELD_SIZE
    col = (click_pos[0] - FIELD_SIZE//2) // FIELD_SIZE

    return [row, col]

def lauch_window(display):
    draw_launch_background(display)
    play_clicked = False
    play_button = Button("Images/Play_no.png", "Images/Play_yes.png", [562, 300], [190, 30])

    while not play_clicked:
        play_button.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    play_clicked = play_button.check_click()
            elif event.type == pygame.QUIT:
                play_clicked = True
                global QUIT_CONST
                QUIT_CONST[0] = True
                QUIT_CONST[1] = "Button"

def chess_window(display):
    display.fill(pygame.Color(MAIN_COLOR))

    game = Game_Gui()
    open = True

    # is_move == True when white, == False when black
    is_move = True

    start_time = time.time()
    global GAME_TIME

    playerW = Player(True, GAME_TIME, GAME_TIME + start_time)
    playerB = Player(False, GAME_TIME, GAME_TIME + start_time)
    winner = None

    chackmate_king_pos = []
    check_king_pos = []

    first_click = []
    next_fields_list = []

    pause_time = 0
    start_pause = 0
    resume_clicked = False

    pause_button = Button("Images/Pause_no.png", "Images/Pause_yes.png", [725, 345], [130, 30])
    new_game_button = Button("Images/new_game_no.png", "Images/new_game_yes.png", [575, 345], [130, 30])
    # resume_button = Button("Images/resume_no.png", "Images/resume_yes.png", [725, 345], [130, 30])

    while open and not QUIT_CONST[0]:
        if not resume_clicked:
            update_players_time(display, [playerW, playerB], start_time, pause_time, is_move)
            check_time_end(game, [playerW, playerB])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = pygame.mouse.get_pos()

                    if new_game_button.check_click():
                        new_game_function()
                    
                    if pause_button.check_click():
                        if resume_clicked:
                            resume_clicked = False
                            pause_time = time.time() - start_pause
                            pause_button.change_images(["Images/Pause_no.png", "Images/Pause_yes.png"])
                        else:
                            resume_clicked = True
                            start_pause = time.time()
                            pause_button.change_images(["Images/resume_no.png", "Images/resume_yes.png"])

                    if resume_clicked:
                        continue
                    if click_pos[0] >= 510 or click_pos[1] >= 480:
                        continue
                    if len(first_click) == 0:
                        pos = create_pos(click_pos)
                        if is_move:
                            if game.check_choosen_figure(playerW, pos):
                                next_fields_list = game.get_board().get_next_fields_list(pos)
                                first_click = click_pos
                        else:
                            if game.check_choosen_figure(playerB, pos):
                                next_fields_list = game.get_board().get_next_fields_list(pos)
                                first_click = click_pos
                    elif len(first_click) == 2:
                        old_pos = create_pos(first_click)
                        new_pos = create_pos(click_pos)

                        if game.check_move(old_pos, new_pos):
                            figure = copy.deepcopy(game.get_board().get_array()[new_pos[0]][new_pos[1]])
                            if figure.get_name() != " ":
                                game.add_to_broken_figures(figure)
                            game.move(old_pos, new_pos)
                            if game.check_if_pawn_converting(new_pos):
                                draw_pawn_converting_window(display, game.get_board().get_array()[new_pos[0]][new_pos[1]])
                                replacing_pawn(game.get_board(), game.get_board().get_array()[new_pos[0]][new_pos[1]])
                                notation = game.get_chess_notation()
                                string = notation[len(notation) - 1]
                                new_string = string[0:3] + game.get_board().get_array()[new_pos[0]][new_pos[1]].get_name() + string[3:]
                                notation[len(notation) - 1] = new_string
                                game.set_chess_notation(notation)

                            check_king_pos = []

                            if is_move:
                                is_move = False
                                if game.get_board().is_checkmate(False):
                                    winner = playerW
                                    chackmate_king_pos = game.get_board().get_kingB_position()
                                    # game.set_winner_message("White won!!!")
                                    game.set_result(1)
                                    game.set_checkmate_notation()
                                    play_sound("Sounds/Checkmate.mp3")
                                    break
                                if game.get_board().is_check(False):
                                    check_king_pos = game.get_board().get_kingB_position()
                                    game.set_check_notation()
                                    play_sound("Sounds/Check.mp3")
                            else:
                                is_move = True
                                if game.get_board().is_checkmate(True):
                                    winner = playerB
                                    chackmate_king_pos = game.get_board().get_kingW_position()
                                    # game.set_winner_message("Black won!!!")
                                    game.set_result(0)
                                    game.set_checkmate_notation()
                                    play_sound("Sounds/Checkmate.mp3")
                                    break
                                if game.get_board().is_check(True):
                                    check_king_pos = game.get_board().get_kingW_position()
                                    game.set_check_notation()
                                    play_sound("Sounds/Check.mp3")

                        first_click = []
                        next_fields_list = []

            elif event.type == pygame.QUIT:
                QUIT_CONST[0] = True
                QUIT_CONST[1] = "Button"

        draw_board(display, chackmate_king_pos, check_king_pos)
        draw_figures(display, game.get_board().get_array(), next_fields_list)
        draw_broken_figures_windows(display, game)
        draw_chess_notation(display, game.get_chess_notation())

        # if resume_clicked:
        #     draw_pause_and_new_game_buttons(display, [new_game_button, resume_button])
        # else:
        draw_pause_and_new_game_buttons(display, [new_game_button, pause_button])

        pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), (0, 0), (0, HEIGHT), 3)
        pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), (0, 0), (WIDTH, 0), 3)
        pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), (WIDTH, HEIGHT), (0, HEIGHT), 3)
        pygame.draw.line(display, pygame.Color(CONTOUR_COLOR), (WIDTH, HEIGHT), (WIDTH, 0), 3)
        pygame.display.flip()

        if len(chackmate_king_pos):
            # draw_end_game_window(display, game.get_winner_message())
            draw_end_game_window(display, game.get_result())
            pygame.display.flip()
            write_to_file(game.get_chess_notation(), f"History/{Time.get_now()}.json")
            pygame.time.delay(5000)
            open = False
            main()
        if game.get_board().check_if_draw(game.get_chess_notation()):
            draw_end_game_window(display, game.get_result())
            pygame.display.flip()
            write_to_file(game.get_chess_notation(), f"History/{Time.get_now()}.json")
            pygame.time.delay(5000)
            open = False
            main()


def main():
    pygame.init()
    pygame.display.set_caption("Chess")
    display = pygame.display.set_mode((WIDTH, HEIGHT))

    program_icon = pygame.image.load('Images/program_icon.png')
    pygame.display.set_icon(program_icon)

    global QUIT_CONST
    lauch_window(display)
    if not QUIT_CONST[0]:
        dialog_window(display)
    if not QUIT_CONST[0]:
        chess_window(display)

    pygame.quit()

if __name__ == "__main__":
    main()
