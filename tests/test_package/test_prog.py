
from test_package.prog import sum_numbers

def test_sum_ok():
    assert sum_numbers(5, 6) == 11

def test_fails():
    assert sum_numbers(1, 3) == 42
