from collections import Counter
from functions.move import Move
from functions.playground import Playground
from random import choice
from typing import Final

FIELD_SIZE: Final = 3


def choose_first_move() -> 'str':
    """
    Making a random choice of a player, making first move
    :return:
    """
    return choice(['Human', 'AI'])


def find_line_candidates(playground: Playground,
                         move: Move) -> list[tuple[int, int]]:
    """
    Searching for lines, which is one step to win, to prevent winning.
    :param playground:
    :param move:
    :return line_candidates: List of points which could make the winning line for Human player
    """
    h_sign = move.sign['Human']
    line_candidates = []
    right_cross = []
    left_cross = []
    right_cross_candidate = left_cross_candidate = None
    for y in range(FIELD_SIZE):
        cur_row = []
        cur_col = []
        cur_row_candidate = cur_col_candidate = None
        for x in range(FIELD_SIZE):
            if playground.field[y][x] == h_sign:
                cur_row.append((y, x))
            elif playground.field[y][x] == playground.base_mark:
                cur_row_candidate = (y, x)

            if playground.field[x][y] == h_sign:
                cur_col.append((x, y))
            elif playground.field[x][y] == playground.base_mark:
                cur_col_candidate = (x, y)

        if len(cur_row) == FIELD_SIZE - 1 and cur_row_candidate:
            line_candidates.append(cur_row_candidate)
        if len(cur_col) == FIELD_SIZE - 1 and cur_col_candidate:
            line_candidates.append(cur_col_candidate)

        if playground.field[y][FIELD_SIZE-1-y] == h_sign:
            right_cross.append((y, FIELD_SIZE - 1 - y))
        elif playground.field[y][FIELD_SIZE-1-y] == playground.base_mark:
            right_cross_candidate = (y, FIELD_SIZE - 1 - y)
        if playground.field[y][y] == h_sign:
            left_cross.append((y, y))
        elif playground.field[y][y] == playground.base_mark:
            left_cross_candidate = (y, y)
    if len(right_cross) == FIELD_SIZE - 1 and right_cross_candidate:
        line_candidates.append(right_cross_candidate)
    if len(left_cross) == FIELD_SIZE - 1 and left_cross_candidate:
        line_candidates.append(left_cross_candidate)
    return line_candidates


def best_attack_move(playground: Playground) -> tuple[int, int] | None:
    """
    TODO: Make clever attacking move
    Defining best attack move to continue existing line
    :param playground:
    :return:
    """
    if playground.field[FIELD_SIZE//2][FIELD_SIZE//2] == playground.base_mark:
        return FIELD_SIZE//2, FIELD_SIZE//2
    else:
        return None


def best_defence_move(
        line_candidates: list[tuple[int, int]]) -> tuple[int, int] | None:
    """
    Defining point which could be ending for several lines, if there's not - returns nothing

    :param line_candidates:
    :return: One best move for current situation
    """
    if not line_candidates:
        return None
    line_candidates = Counter(line_candidates)
    if max(line_candidates.values()) > 1:
        return line_candidates.most_common()[0][0]
    else:
        return choice(list(line_candidates.keys()))


def make_ai_move(playground: Playground, move: Move) -> None:
    """
    Create a random move for an ai
    :param playground: Playground object
    :param move: Move object
    :return: returns nothing
    """
    best_move = best_defence_move(find_line_candidates(playground, move))
    if not best_move:
        best_move = best_attack_move(playground)
        if not best_move:
            best_move = choice(playground.get_available_moves())
    playground.make_move(best_move, move.sign['AI'])
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
        cur_move = tuple(map(lambda x: int(x)-1, input().split()))
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
                print(playground.draw_field())
            make_human_move(playground, move)
        else:
            make_ai_move(playground, move)
        print(playground.draw_field())
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