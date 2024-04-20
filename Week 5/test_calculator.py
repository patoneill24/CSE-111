from calculator import add, multiply
import pytest

def test_multiply():
    assert multiply(2,20) == 40
    assert multiply(-1,2) == -2 


pytest.main("-v","--tb=line","-rN",__file__)