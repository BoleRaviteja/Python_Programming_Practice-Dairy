
from hello_world import greet


def test_greet_returns_expected_message():
    assert greet("Raviteja") == "Hello, Raviteja!"


def test_greet_with_different_name():
    assert greet("Python") == "Hello, Python!"
