import pytest
from src.calculator_core import CalculatorCore

@pytest.fixture
def calculator():
    return CalculatorCore()

def test_add(calculator):
    assert calculator.calculate(["5", "+", "3"]) == 8

def test_subtract(calculator):
    assert calculator.calculate(["10", "-", "4"]) == 6

def test_multiply(calculator):
    assert calculator.calculate(["7", "*", "6"]) == 42

def test_divide(calculator):
    assert calculator.calculate(["12", "/", "3"]) == 4

def test_floating_point_operations(calculator):
    assert calculator.calculate(["2.5", "+", "1.5"]) == 4.0
    assert calculator.calculate(["9", "/", "2"]) == 4.5

def test_order_of_operations(calculator):
    # Current calculator_core uses eval, which handles order of operations.
    # Once custom parsing is implemented, this test will become more critical.
    assert calculator.calculate(["5", "+", "3", "*", "2"]) == 11
    assert calculator.calculate(["(", "10", "+", "2", ")", "/", "3"]) == 4

def test_clear_command(calculator):
    calculator.calculate(["5", "+", "5"])
    assert calculator.calculate(['clear']) == 0
    assert calculator.result == 0

def test_clear_entry_command(calculator):
    calculator.calculate(["5", "+", "5"])
    assert calculator.calculate(['ce']) == 0
    assert calculator.result == 0

def test_division_by_zero(calculator):
    with pytest.raises(ValueError, match="Error: Division by zero"):
        calculator.calculate(["10", "/", "0"])


