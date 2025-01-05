import pytest

@pytest.mark.one
def test_method1():
    x = 2
    y = 5
    assert x == y

@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a+5 == b
    

