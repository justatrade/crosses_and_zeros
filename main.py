import move
import playground as plgr
import random

FIELD_SIZE = 3


def choose_first_move():
    """
    Making a random choice of a player, making first move
    :return:
    """
    return random.choice(['Human', 'AI'])


def make_ai_move(p, m) -> None:
    """
    Create a best move for an ai
    :return: return coordinates of a move
    """
    p.make_move(random.choice(p.get_available_moves()), m.sign['AI'])
    m.move_done()


def make_human_move(p, m) -> None:
    """
    Get human input as a coordinates
    :return: return coordinates of a move
    """
    cur_move = (-1, -1)
    while cur_move not in p.get_available_moves():
        cur_move = tuple(map(lambda x: int(x), input().split()))
    else:
        p.make_move(cur_move, m.sign['Human'])
        m.move_done()



def main():
    """
    Main management orchestration function
    :return:
    """
    first = choose_first_move()
    second = 'AI' if first == 'Human' else 'Human'
    m = move.Move(FIELD_SIZE, first, second)
    p = plgr.Playground(FIELD_SIZE)
    cur_move = ''
    while p.get_available_moves() and not p.check_if_win():
        cur_move = m.next_move()
        if cur_move == 'Human':
            if len(p.get_available_moves()) == FIELD_SIZE ** 2:
                print('Make your first move')
                p.draw_field()
            make_human_move(p, m)
        else:
            make_ai_move(p, m)
        p.draw_field()
    else:
        print(f'{cur_move} wins')


if __name__ == '__main__':
    main()
    # p = plgr.Playground(FIELD_SIZE)
    # p.draw_field()
    # print(p.get_available_moves())