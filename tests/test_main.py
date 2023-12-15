import io

import pytest

from functions.main import choose_first_move, find_line_candidates, \
    best_attack_move, best_defence_move, make_ai_move, make_human_move, main
from functions.move import Move
from functions.playground import Playground
from tests.test_playground import base_3x3_field_matrix, some_3x3_field_matrix


@pytest.mark.parametrize('expected',
                         [
                             ['Human', 'AI']
                         ])
def test__choose_first_move__any(expected):
    assert choose_first_move() in expected


# pre_winning_field = [([['X', 'X', '.'] if x == i else ['.', '0', '.'] for x in range(3)]) for i in range(3)]
pre_winning_field = []
for matrix in range(3):
    current_matrix = []
    for line_index in range(3):
        line = ['X', 'X', '.'] if line_index == matrix else ['.', '0', '.']
        current_matrix.append(line)
    pre_winning_field.append(current_matrix)


@pytest.mark.parametrize('field, expected',
                         [
                             (pre_winning_field.pop(), [(2, 2)]),
                             (pre_winning_field.pop(), [(1, 2)]),
                             (pre_winning_field.pop(), [(0, 2)]),
                             (base_3x3_field_matrix, [])
                         ])
def test__find_line_candidates__success_fail(field, expected):
    test_playground = Playground(3)
    test_playground.field = field
    move = Move(3, 'Human', 'AI')

    assert find_line_candidates(test_playground, move) == expected


@pytest.mark.parametrize('field, expected',
                         [
                             (base_3x3_field_matrix, (1, 1)),
                             (some_3x3_field_matrix, None)
                         ])
def test__best_attack_move__success_fail(field, expected):
    test_playground = Playground(3)
    test_playground.field = field

    assert best_attack_move(test_playground) == expected


#pre_winning_field = [([['X', 'X', '.'] if x == i else ['.', '0', '.'] for x in range(3)]) for i in range(3)]
pre_winning_field = []
for matrix in range(3):
    current_matrix = []
    for line_index in range(3):
        line = ['X', 'X', '.'] if line_index == matrix else ['.', '0', '.']
        current_matrix.append(line)
    pre_winning_field.append(current_matrix)
double_winning_field = [['0', '0', 'X'],
                        ['0', '0', 'X'],
                        ['X', 'X', '.']]


@pytest.mark.parametrize('field, expected',
                         [
                             (pre_winning_field.pop(), (2, 2)),
                             (base_3x3_field_matrix, None),
                             (double_winning_field, (2, 2))
                         ])
def test__best_defence_move__success_one_or_none(field, expected):
    test_playground = Playground(3)
    test_playground.field = field
    move = Move(3, 'Human', 'AI')
    line_candidates = find_line_candidates(test_playground, move)
    print(line_candidates)
    assert best_defence_move(line_candidates) == expected


double_winning = [['.', '.', 'X'],
                  ['.', 'X', '.'],
                  ['0', '0', 'X']]


@pytest.mark.parametrize('field, expected',
                        [
                            (double_winning, [(0, 0), (1, 2)])
                        ])
def test__best_defence_move__success_gt_one_candidate(field, expected):
    test_playground = Playground(3)
    test_playground.field = field
    move = Move(3, 'Human', 'AI')
    line_candidates = find_line_candidates(test_playground, move)

    assert best_defence_move(line_candidates) in expected


@pytest.mark.parametrize('field, expected',
                         [
                             (double_winning, 1),
                             (base_3x3_field_matrix, 1),
                             (some_3x3_field_matrix, 1)
                         ])
def test__make_ai_move__success(field, expected):
    test_playground = Playground(3)
    move = Move(3, 'Human', 'AI')
    avail_moves_cnt = len(test_playground.get_available_moves())
    make_ai_move(test_playground, move)
    avail_moves_cnt = avail_moves_cnt - len(test_playground.get_available_moves())

    assert avail_moves_cnt == expected


@pytest.mark.parametrize('field, human_moves, expected',
                         [
                             (base_3x3_field_matrix, '1 1', 1),
                             (some_3x3_field_matrix, '2 2\n3 3', 1)
                         ])
def test__make_human_move__success(field, human_moves, expected, monkeypatch):
    test_playground = Playground(3)
    test_playground.field = field
    move = Move(3, 'Human', 'AI')

    monkeypatch.setattr('sys.stdin', io.StringIO(human_moves))
    avail_moves_cnt = len(test_playground.get_available_moves())
    make_human_move(test_playground, move)
    avail_moves_cnt = avail_moves_cnt - len(test_playground.get_available_moves())

    assert avail_moves_cnt == expected


@pytest.mark.parametrize('human_moves, expected',
                         [
                             ('2 2\n1 1\n1 2\n1 3\n2 1\n2 3\n3 1\n3 2\n3 3\n',
                              {'  1 2 3 x': ['nd draw\n',
                                             '\nAI wins\n'],
                               'Make your': ['nd draw\n',
                                             '\nAI wins\n',
                                             'man wins\n']}),
                             ('2 2\n1 1\n1 3\n3 3\n3 1\n2 1\n3 2\n2 3\n1 2\n',
                              {'  1 2 3 x': ['nd draw\n',
                                             '\nAI wins\n'],
                               'Make your': ['nd draw\n',
                                             '\nAI wins\n',
                                             'man wins\n']})
                         ])
def test__main__success(human_moves, expected, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO(human_moves))

    main()
    captured = capsys.readouterr()

    assert captured.out[-9:] in expected[captured.out[:9]]
