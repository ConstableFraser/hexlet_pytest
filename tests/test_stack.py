import pytest


def test_stack_add_pop():
    stack = []
    stack.append("element1")
    stack.append("element2")
    stack.pop()
    assert stack.pop() == "element1"
    assert not stack


def test_stack_empty():
    stack = []
    stack.append("first")
    stack.append("second")
    stack.pop()
    stack.pop()
    with pytest.raises(IndexError):
        stack.pop()

