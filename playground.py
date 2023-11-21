class Playground:

    def __init__(self, size):
        if size >= 3:
            self.size = size
        else:
            raise ValueError
        self.field = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def draw_field(self) -> None:
        '''
        Show the current field with all moves.
        Creating a temp full field with borders, then put the current moves
        values on it
        :return:
        '''
        temp_field = []
        x_border = []
        for i in range(self.size+1):
            if i > 0:
                x_border.append(str(i))
            else:
                x_border.append(' ')
            x_border.append(' ')
        x_border.append('x')
        temp_field.append(x_border)
        for i in range(1, self.size+1):
            temp_y = [str(i), ' ']
            temp_y.extend([self.field[i-1][x//2] if x % 2 == 0 else '|' for x in range(self.size*2-1)])
            temp_field.append(temp_y)
        temp_field.append(['y'])
        for i in range(len(temp_field)):
            print(''.join(temp_field[i]))

    def get_available_moves(self) -> list[tuple[int, int]]:
        '''
        List of available moves
        :return:
        '''
        available_moves = []
        for y in range(self.size):
            for x in range(self.size):
                if self.field[y][x] == '.':
                    available_moves.append((y+1, x+1))
        return available_moves

    def check_if_win(self) -> bool:
        '''
        Check weather game is done or not
        :return: True or False
        '''
        pass

    def make_move(self, move: tuple[int, int], sign: str) -> None:
        '''
        Put a move on a playfield
        :return:
        '''
        self.field[move[0]-1][move[1]-1] = sign
