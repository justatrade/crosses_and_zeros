from typing import Final


class Playground:
    base_mark: Final = '.'

    def __init__(self, size):
        if size >= 3:
            self.size = size
        else:
            raise ValueError
        self.field = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def draw_field(self) -> str:
        """
        Show the current field with all moves.
        Creating a temp full field with borders, then put the current moves
        values on it
        :return:
        """
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
        return '\n'.join(
            [''.join(temp_field[i]) for i in range(len(temp_field))]
        )

    def get_available_moves(self) -> list[tuple[int, int]]:
        """
        List of available moves
        :return:
        """
        available_moves = []
        for y in range(self.size):
            for x in range(self.size):
                if self.field[y][x] == '.':
                    available_moves.append((y, x))
        return available_moves

    def check_if_win(self) -> bool:
        """
        Check weather game is done or not
        :return: True or False
        """
        for row in range(len(self.field)):
            if (len(set(self.field[row])) == 1 and
                    self.field[row][0] != self.base_mark):
                return True
        for col in range(len(self.field)):
            cur_col = []
            for row in range(len(self.field)):
                cur_col.append(self.field[row][col])
            if (len(set(cur_col)) == 1 and
                    cur_col[0] != self.base_mark):
                return True
        left_cross = [self.field[x][x] for x in range(len(self.field))]
        right_cross = [self.field[x][-1-x] for x in range(len(self.field))]
        if len(set(left_cross)) == 1 and left_cross[0] != self.base_mark:
            return True
        if len(set(right_cross)) == 1 and right_cross[0] != self.base_mark:
            return True
        return False

    def make_move(self, move: tuple[int, int], sign: str) -> None:
        """
        Put a move on a playfield
        :return:
        """
        self.field[move[0]][move[1]] = sign
