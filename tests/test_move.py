import pytest

from functions.move import Move

three_X_0 = 3, 'X', '0'
four_0_X = 4, '0', 'X'
COMMON_PARAMS = 'field_size, first, second'

@pytest.mark.parametrize(COMMON_PARAMS + ', expected',
                         [
                             (*three_X_0,
                              ['X', '0', 'X', '0', 'X',
                               '0', 'X', '0', 'X']),
                             (*four_0_X,
                              ['X', '0', 'X', '0', 'X', '0', 'X', '0',
                               'X', '0', 'X', '0', 'X', '0', 'X', '0'])
                         ])
def test__init__success(field_size: int, first: str,
                        second: str, expected: list[str]):
    move = Move(field_size, first, second)

    assert move.queue == expected


@pytest.mark.parametrize(COMMON_PARAMS + ', expected',
                         [
                             (*three_X_0, 'X'),
                             (*four_0_X, '0')
                         ])
def test__next_move__success(field_size: int, first: str,
                             second: str, expected: str):
    move = Move(field_size, first, second)

    assert move.next_move() == expected


@pytest.mark.parametrize(COMMON_PARAMS + ', expected',
                         [
                             (*three_X_0,
                              ['X', '0', 'X', '0', 'X',
                               '0', 'X', '0']),
                             (*four_0_X,
                              ['X', '0', 'X', '0', 'X', '0', 'X', '0',
                               'X', '0', 'X', '0', 'X', '0', 'X'])
                         ])
def test__move_done__success(field_size: int, first: str,
                             second: str, expected: list[str]):
    move = Move(field_size, first, second)
    move.move_done()

    assert move.queue == expected
