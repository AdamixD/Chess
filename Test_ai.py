from Board import Board
from Game_GUI import Game_Gui
import time
import random
CHECKMATE = 100000

game = Game_Gui()
print(game.get_board().print_board())
turn = True
while not game.get_board().is_checkmate(True) or not game.get_board().is_checkmate(False):
    if turn:
        turn = False
        old_pos = list(map(int, input().split()))
        new_pos = list(map(int, input().split()))
        next_move = [old_pos, new_pos]
    else:
        a = time.time()
        possible_moves = game.get_board().get_all_possible_moves(turn)
        random.shuffle(possible_moves)
        game.find_the_best_move(3, possible_moves, -CHECKMATE, CHECKMATE, 1 if turn else -1)
        next_move = game.get_ai_next_move()
        turn = True
        b = time.time()
        print(b - a)
        print("Deepcopy time", game.get_deepcopy_time())

    game.move(next_move[0], next_move[1])
    print(game.get_board().print_board())