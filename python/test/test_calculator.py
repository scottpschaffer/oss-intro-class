import calculator


def test_add():
    assert calculator.add(3, 9) == 12

def test_add_bad():
    assert calculator.add(3, 9) == 13

def test_multiply():
    assert calculator.multiply(2, 2) == 4
