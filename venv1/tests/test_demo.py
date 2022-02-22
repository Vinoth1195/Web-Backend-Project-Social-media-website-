import pytest

def add(x,y):
    return x+y

def test_add():
    print("testing add function")

    sum = add(3,2)

    assert sum==5