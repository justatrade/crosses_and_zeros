import playground as plgr
import random

def chose_first_move():
    return random.choice(['Human', 'AI'])


def make_ai_move():
    '''
    Create a best move for an ai
    :return: return coordinates of a move
    '''
    pass


def get_human_move():
    '''
    Get human input as a coordinates
    :return: return coordinates of a move
    '''
    pass



def main():
    '''
    Main management orchestration function
    :return:
    '''
    pass


if __name__ == '__main__':
    p = plgr.Playground(3)
    p.draw_field()
    print(p._get_available_moves())