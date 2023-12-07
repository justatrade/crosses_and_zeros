import pytest

from functions.move import Move


COMMON = pytest.mark.parametrize('field_size, first, second',
                                 [
                                     (3, 'X', '0'),
                                     (4, '0', 'X')
                                 ])


@pytest.mark.parametrize(COMMON.mark.args[0] + ', expected',
                         [
                             (*COMMON.mark.args[1][0],
                              ['X', '0', 'X', '0', 'X',
                               '0', 'X', '0', 'X']),
                             (*COMMON.mark.args[1][1],
                              ['X', '0', 'X', '0', 'X', '0', 'X', '0',
                               'X', '0', 'X', '0', 'X', '0', 'X', '0'])
                         ])
def test__init__success(field_size, first, second, expected):
    move = Move(field_size, first, second)

    assert move.queue == expected


@pytest.mark.parametrize(COMMON.mark.args[0] + ', expected',
                         [
                             (*COMMON.mark.args[1][0], 'X'),
                             (*COMMON.mark.args[1][1], '0')
                         ])
def test__next_move__success(field_size, first, second, expected):
    move = Move(field_size, first, second)

    assert move.next_move() == expected


@pytest.mark.parametrize(COMMON.mark.args[0] + ', expected',
                         [
                             (*COMMON.mark.args[1][0],
                              ['X', '0', 'X', '0', 'X',
                               '0', 'X', '0']),
                             (*COMMON.mark.args[1][1],
                              ['X', '0', 'X', '0', 'X', '0', 'X', '0',
                               'X', '0', 'X', '0', 'X', '0', 'X'])
                         ])
def test__move_done__success(field_size, first, second, expected):
    move = Move(field_size, first, second)
    move.move_done()

    assert move.queue == expected
