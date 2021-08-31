from Board import Board
from Game_GUI import Game_Gui

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
        game.find_the_best_move(turn, 2)
        next_move = game.get_ai_next_move()
        turn = True

    game.move(next_move[0], next_move[1])
    print(game.get_board().print_board())