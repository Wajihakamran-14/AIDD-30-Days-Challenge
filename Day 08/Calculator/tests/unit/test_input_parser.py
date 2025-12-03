import pytest
from src.input_parser import InputParser

@pytest.fixture
def parser():
    return InputParser()

def test_parse_numbers_and_operators(parser):
    tokens = parser.parse("5 + 3 * 2")
    assert tokens == ["5", "+", "3", "*", "2"]

def test_parse_floating_point_numbers(parser):
    tokens = parser.parse("2.5 / 1.5")
    assert tokens == ["2.5", "/", "1.5"]

def test_parse_negative_numbers(parser):
    tokens = parser.parse("-5 + 10")
    assert tokens == ["-", "5", "+", "10"]

def test_parse_clear_command(parser):
    tokens = parser.parse("clear")
    assert tokens == ["clear"]

def test_parse_clear_entry_command(parser):
    tokens = parser.parse("ce")
    assert tokens == ["ce"]

def test_parse_with_extra_spaces(parser):
    tokens = parser.parse("  10   +   5  ")
    assert tokens == ["10", "+", "5"]

def test_parse_empty_input(parser):
    tokens = parser.parse("   ")
    assert tokens == []

def test_parse_complex_expression(parser):
    tokens = parser.parse("(10 + 5) * 2 - 1")
    assert tokens == ["(", "10", "+", "5", ")", "*", "2", "-", "1"]
