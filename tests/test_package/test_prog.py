
from test_package.prog import sum_numbers

def test_sum_ok():
    assert sum_numbers(5, 6) == 11

def test_sum_ok2():
    assert sum_numbers(6, 6) == 12

def test_sum_ok3():
    assert sum_numbers(-6, 6) == 0

'''
def test_fails():
    assert sum_numbers(1, 3) == 42
'''
