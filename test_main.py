import pytest


from main import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
