import calculator


def test_add():
    assert calculator.add(3, 9) == 12
    assert calculator.add(1, 1) == 2
    assert calculator.add(10, 5) == 15


def test_multiply():
    assert calculator.multiply(2, 2) == 4

def test_subtraction():
    assert calculator.subtraction(5, 3) == 2

def test_divide():
    assert calculator.divide(20, 4) == 5