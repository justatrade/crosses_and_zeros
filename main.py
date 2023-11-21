import move
import playground as plgr
import random

FIELD_SIZE = 3


def choose_first_move():
    return random.choice(['Human', 'AI'])


def make_ai_move():
    '''
    Create a best move for an ai
    :return: return coordinates of a move
    '''
    pass


def make_human_move(p, m) -> None:
    '''
    Get human input as a coordinates
    :return: return coordinates of a move
    '''
    cur_move = (-1, -1)
    while cur_move not in p.get_available_moves():
        cur_move = tuple(map(lambda x: int(x), input().split()))
    else:
        p.make_move(cur_move, m.sign['Human'])
        m.move_done()



def main():
    '''
    Main management orchestration function
    :return:
    '''
    first = choose_first_move()
    second = 'AI' if first == 'Human' else 'Human'
    m = move.Move(FIELD_SIZE, first, second)
    p = plgr.Playground(FIELD_SIZE)
    while p.get_available_moves() and not p.check_if_win():
        make_human_move(p, m)
        p.draw_field()



if __name__ == '__main__':
    main()
    # p = plgr.Playground(FIELD_SIZE)
    # p.draw_field()
    # print(p.get_available_moves())