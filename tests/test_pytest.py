import pytest
import requests

#from .. import task1
from task1 import solution

@pytest.mark.parametrize(
    'a,b,c,expected',
    (
            [1, 8, 15, (-3.0, -5.0)],
            [1, -13, 12, (12.0, 1.0)],
            [-4, 28, -49, 3.5],
            [1, 1, 1, 'корней нет']
    )
)
def test_discriminant(a, b, c, expected):
    actual = solution(a, b, c)
    assert actual == expected

from task2 import vote

@pytest.mark.parametrize(
    'a,b,c,d,e,expected',
    (
            [1, 1, 1, 2, 3, 1],
            [1, 2, 3, 2, 2, 2],
    )
)
def test_vote(a, b, c, d, e, expected):
    actual = vote([a, b, c, d, e])
    assert actual == expected


from task3 import get_name, get_directory

@pytest.mark.parametrize(
    'doc_number,expected',
    (
            ['10006', 'Аристарх Павлов'],
            ['101', 'Документ не найден'],
    )
)
def test_get_name(doc_number, expected):
    actual = get_name(doc_number)
    assert actual == expected

@pytest.mark.parametrize(
    'doc_number,expected',
    (
            ['311 020204', 'Полки с таким документом не найдено'],
    )
)
def test_get_directory(doc_number, expected):
    actual = get_directory(doc_number)
    assert actual == expected