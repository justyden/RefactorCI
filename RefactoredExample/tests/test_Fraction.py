import sys
sys.path.append("./RefactoredExample/src/")
from main import Fraction


def test_get_num():
    x = Fraction(1, 2)
    assert x.get_num() == 1


def test_get_den():
    y = Fraction(2, 3)
    assert y.get_den() == 3


def test_sub():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = x - y
    assert z == Fraction(-1, 6)


def test_mul():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = x * y
    assert z == Fraction(1, 3)


def test_truediv():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = x / y
    assert z == Fraction(3, 4)


def test_comparison_operations():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    assert (x > y) is False
    assert (x >= y) is False
    assert (x < y) is True
    assert (x <= y) is True
    assert (x != y) is True


def test_negative_fraction():
    beta = Fraction(3, -5)
    assert beta == Fraction(-3, 5)


def test_radd():
    x = Fraction(1, 2)
    assert (x + 1) == Fraction(3, 2)
    assert (1 + x) == Fraction(3, 2)


def test_iadd():
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    for i in range(y.get_den()):
        x += i
    assert x == Fraction(7, 2)
