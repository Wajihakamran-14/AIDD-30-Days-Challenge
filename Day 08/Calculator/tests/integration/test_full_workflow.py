import pytest
import subprocess
import sys

# Helper function to run the calculator as a subprocess
def run_calculator(input_sequence):
    process = subprocess.Popen(
        [sys.executable, 'src/main.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate("\n".join(input_sequence) + "\nexit")
    return stdout.strip(), stderr.strip()

def test_basic_addition():
    stdout, stderr = run_calculator(["5 + 3"])
    assert "Result: 8" in stdout
    assert not stderr

def test_basic_subtraction():
    stdout, stderr = run_calculator(["10 - 4"])
    assert "Result: 6" in stdout
    assert not stderr

def test_basic_multiplication():
    stdout, stderr = run_calculator(["7 * 6"])
    assert "Result: 42" in stdout
    assert not stderr

def test_basic_division():
    stdout, stderr = run_calculator(["12 / 3"])
    assert "Result: 4" in stdout
    assert not stderr

def test_floating_point_operations():
    stdout, stderr = run_calculator(["2.5 + 1.5"])
    assert "Result: 4.0" in stdout
    assert not stderr

def test_floating_point_division():
    stdout, stderr = run_calculator(["9 / 2"])
    assert "Result: 4.5" in stdout
    assert not stderr

def test_order_of_operations():
    stdout, stderr = run_calculator(["5 + 3 * 2"])
    assert "Result: 11" in stdout
    assert not stderr

def test_clear_all_command():
    stdout, stderr = run_calculator(["5 + 5", "clear"])
    assert "Display cleared." in stdout
    assert not stderr

def test_clear_entry_command():
    stdout, stderr = run_calculator(["10", "ce"])
    assert "Display cleared." in stdout
    assert not stderr

def test_division_by_zero_error():
    stdout, stderr = run_calculator(["10 / 0"])
    assert "Error: Division by zero" in stdout
    assert not stderr # The error is handled and printed to stdout in main.py, not stderr
