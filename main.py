from move import Move
from playground import Playground
import random
from typing import Final

FIELD_SIZE: Final = 3


def choose_first_move() -> 'str':
    """
    Making a random choice of a player, making first move
    :return:
    """
    return random.choice(['Human', 'AI'])


def find_line_candidates(playground: Playground, move: Move):
    """
    Searching for lines, which is one step to win, to prevent winning.
    :param playground:
    :param move:
    :return line_candidates: List of lists of points on the playing field, making the line
    """
    h_sign = move.sign['Human']
    line_candidates = []
    for y in range(FIELD_SIZE):
        cur_row = []
        cur_col = []
        for x in range(FIELD_SIZE):
            if playground.field[y][x] == h_sign:
                cur_row.append((y, x))
            if playground.field[x][y] == h_sign:
                cur_col.append((x, y))
        if len(cur_row) == FIELD_SIZE - 1:
            line_candidates.append(cur_row)
        if len(cur_col) == FIELD_SIZE - 1:
            line_candidates.append(cur_col)
    right_cross = [(x, FIELD_SIZE-1-x) for x in range(FIELD_SIZE)
                   if playground.field[x][-1 - x] == h_sign]
    left_cross = [(x, x) for x in range(FIELD_SIZE)
                  if playground.field[x][x] == h_sign]
    if len(right_cross) == FIELD_SIZE - 1:
        line_candidates.append(right_cross)
    if len(left_cross) == FIELD_SIZE - 1:
        line_candidates.append(left_cross)
    print(line_candidates)
    return line_candidates


def define_best_move(line_candidates: list[tuple[int, int]]) -> tuple[int, int]:
    """
    TODO: Create this function
    Defining point which could be ending for several lines, if there's not - take only one

    :param line_candidates:
    :return:
    """
    pass


def make_ai_move(playground: Playground, move: Move) -> None:
    """
    Create a random move for an ai
    :param playground: Playground object
    :param move: Move object
    :return: returns nothing
    """
    playground.make_move(
        random.choice(playground.get_available_moves()),
        move.sign['AI']
    )
    move.move_done()


def make_human_move(playground: Playground, move: Move) -> None:
    """
    Get human input as a coordinates
    :param playground: Playground object
    :param move: Move object
    :return: returns nothing
    """
    cur_move = (-1, -1)
    while cur_move not in playground.get_available_moves():
        cur_move = tuple(map(lambda x: int(x), input().split()))
    else:
        playground.make_move(cur_move, move.sign['Human'])
        move.move_done()


def main():
    """
    Main management orchestration function
    :return:
    """
    first = choose_first_move()
    second = 'AI' if first == 'Human' else 'Human'
    move = Move(FIELD_SIZE, first, second)
    playground = Playground(FIELD_SIZE)
    cur_move = ''
    while playground.get_available_moves() and not playground.check_if_win():
        cur_move = move.next_move()
        if cur_move == 'Human':
            if len(playground.get_available_moves()) == FIELD_SIZE ** 2:
                print('Make your first move')
                playground.draw_field()
            make_human_move(playground, move)
        else:
            make_ai_move(playground, move)
        playground.draw_field()
    else:
        if playground.check_if_win():
            print(f'{cur_move} wins')
        else:
            print('Round draw')


if __name__ == '__main__':
    main()
    # p = plgr.Playground(FIELD_SIZE)
    # p.draw_field()
    # print(p.get_available_moves())