import pytest
from funkcje import UnitTests


@pytest.fixture
def f():
    return UnitTests


def test_is_palindrome(f):
    assert f.is_palindrome('kajak') == True
    assert f.is_palindrome('Kobyła ma mały bok') == True
    assert f.is_palindrome('python') == False
    assert f.is_palindrome('') == True
    assert f.is_palindrome('A') == True


'''
@pytest.mark.parametrize("tekst, wynik", [
    ('Kobyła ma mały bok', True),
    ('Python', False),
    ('', True),
    ('A', True)
])

def test_is_palindrome(f, tekst, wynik):
    assert f.is_palindrome(tekst) == wynik
'''


def test_fibonacci(f):
    assert f.fibonacci(f, 0) == 0
    assert f.fibonacci(f, 1) == 1
    assert f.fibonacci(f, 5) == 5
    assert f.fibonacci(f, 10) == 55
    assert f.fibonacci(f, -1) == ValueError


def test_count_volwels(f):
    assert f.count_volwels('Python') == 2
    assert f.count_volwels('AEIOUY') == 6
    assert f.count_volwels('bcd') == 0
    assert f.count_volwels('') == 0
    assert f.count_volwels('Próba żółwia"') == 5


def test_calculate_discount(f):
    assert f.calculate_discount(100, 0.2) == 80.0
    assert f.calculate_discount(50, 0) == 50.0
    assert f.calculate_discount(200, 1) == 0.0
    assert f.calculate_discount(100, -0.1) == ValueError
    assert f.calculate_discount(100, 1.5) == ValueError


def test_flatten_list(f):
    assert f.flatten_list(f, [1, 2, 3]) == [1, 2, 3]
    assert f.flatten_list(f, [1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert f.flatten_list(f, []) == []
    assert f.flatten_list(f, [[[1]]]) == [1]
    assert f.flatten_list(f, [1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_word_frequencies(f):
    assert f.word_frequencies('To be or not to be') == {"to": 2, "be": 2, "or": 1, "not": 1}
    assert f.word_frequencies('Hello, hello!') == {"hello": 2}
    assert f.word_frequencies('') == {}
    assert f.word_frequencies('Python Python python') == {"python": 3}
    assert f.word_frequencies('Ala ma kota, a kot ma Ale.') == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1,
                                                                "ale": 1}


def test_is_prime(f):
    assert f.is_prime(2) == True
    assert f.is_prime(3) == True
    assert f.is_prime(4) == False
    assert f.is_prime(0) == False
    assert f.is_prime(1) == False
    assert f.is_prime(5) == True
    assert f.is_prime(97) == True
