import pytest

from functions.playground import Playground


@pytest.mark.parametrize("size, expected",
                         [
                             (3, 3 ** 2),
                             (10, 10 ** 2),
                             (1001, 1001 ** 2)
                         ])
def test__init__success(size, expected):
    test_playground = Playground(size)
    field_size = sum([len(test_playground.field[y]) for y in range(size)])
    assert field_size == expected


@pytest.mark.parametrize("size, expected",
                         [
                             (0, ValueError),
                             (-3, ValueError)
                         ])
def test__init__fail(size, expected):
    with pytest.raises(expected):
        test_playground = Playground(size)


base_3x3_field = '  1 2 3 x\n' \
                 '1 .|.|.\n' \
                 '2 .|.|.\n' \
                 '3 .|.|.\n' \
                 'y'


@pytest.mark.parametrize('size, expected',
                         [
                             (3, base_3x3_field)
                         ])
def test__draw_field__success(size, expected):
    test_playground = Playground(size)
    assert test_playground.draw_field() == expected


base_3x3_field_matrix = [['.', '.', '.'],
                         ['.', '.', '.'],
                         ['.', '.', '.']]
some_3x3_field_matrix = [['.', 'X', '.'],
                         ['X', '0', '0'],
                         ['.', 'X', '.']]


@pytest.mark.parametrize('field, expected',
                         [
                             (base_3x3_field_matrix,
                              [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
                               (2, 0), (2, 1), (2, 2)]),
                             (some_3x3_field_matrix,
                              [(0, 0), (0, 2), (2, 0), (2, 2)])
                         ])
def test__get_available_moves__success(field, expected):
    test_playground = Playground(3)
    test_playground.field = field

    assert test_playground.get_available_moves() == expected


# winning_matrix = [([['X', 'X', 'X'] if x == i else ['.', '.', '.'] for x in range(3)]) for i in range(3)]
winning_matrix = []
for matrix in range(3):
    current_matrix = []
    for line_index in range(3):
        line = ['X', 'X', 'X'] if line_index == matrix else ['.', '.', '.']
        current_matrix.append(line)
    winning_matrix.append(current_matrix)

winning_matrix.extend(
    [[['X' if elem == y else '.' for elem in range(3)] for x in range(3)] for y in range(3)]
)
winning_matrix.extend(
    [[['X' if elem == x else '.' for elem in range(3)] for x in range(3)] for y in range(1)]
)
winning_matrix.extend(
    [[['X' if x == 3 - 1 - elem else '.' for elem in range(3)] for x in range(3)] for y in range(1)]
)


# Изящности хватило только на однострочное создание нужных полей.
# Но чую, что можно как-то в yield обернуть, и тест в цикле прогнать, например,
# чтобы не городить столько строк. Буду рад подсказке
@pytest.mark.parametrize('field, expected',
                         [
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True),
                             (winning_matrix.pop(), True)
                         ])
def test__check_if_win__success(field, expected):
    test_playground = Playground(len(field))
    test_playground.field = field

    assert test_playground.check_if_win() == expected


@pytest.mark.parametrize('field, expected',
                         [
                             (base_3x3_field_matrix, False),
                             (some_3x3_field_matrix, False),
                         ])
def test__check_if_win__fail(field, expected):
    test_playground = Playground(len(field))
    test_playground.field = field

    assert test_playground.check_if_win() == expected


@pytest.mark.parametrize('move,  sign, expected',
                         [
                             ((1, 1), 'X', 'X'),
                             ((2, 0), '0', '0')
                         ])
def test__make_move_success(move, sign, expected):
    test_playground = Playground(len(base_3x3_field_matrix))
    test_playground.field = base_3x3_field_matrix
    y, x = move

    test_playground.make_move(move, sign)

    assert test_playground.field[y][x] == expected
