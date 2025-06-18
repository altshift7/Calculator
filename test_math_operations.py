import math
import pytest
from math_operations import evaluate_expression
from logger import logger  

def log_test(name, result):
    logger.info(f"{name} passed → Result: {result}")

# Basic Arithmetic
def test_basic_addition():
    result = evaluate_expression("5+3")
    assert math.isclose(float(result), 8.0, rel_tol=1e-3)
    log_test("test_basic_addition", result)

def test_power_operation():
    result = evaluate_expression("2^3")
    assert math.isclose(float(result), 8.0, rel_tol=1e-3)
    log_test("test_power_operation", result)

# Number Conversions
def test_binary_to_decimal():
    result = evaluate_expression("1010dec")
    assert result == "10"
    log_test("test_binary_to_decimal", result)

def test_decimal_to_binary():
    result = evaluate_expression("10bin")
    assert result == "0b1010"
    log_test("test_decimal_to_binary", result)

def test_decimal_to_hex():
    result = evaluate_expression("15hex")
    assert result == "0xf"
    log_test("test_decimal_to_hex", result)

def test_invalid_conversion():
    result = evaluate_expression("invalidbin")
    assert "Error" in result
    log_test("test_invalid_conversion", result)

#  Trigonometry
def test_sin():
    result = evaluate_expression("sin(30)")
    assert math.isclose(float(result), 0.5, rel_tol=1e-3)
    log_test("test_sin", result)

def test_cos():
    result = evaluate_expression("cos(60)")
    assert math.isclose(float(result), 0.5, rel_tol=1e-3)
    log_test("test_cos", result)

def test_tan():
    result = evaluate_expression("tan(45)")
    assert math.isclose(float(result), 1.0, rel_tol=1e-2)
    log_test("test_tan", result)

# Logarithm and Square Root
def test_log10():
    result = evaluate_expression("log(1000)")
    assert math.isclose(float(result), 3.0, rel_tol=1e-3)
    log_test("test_log10", result)

def test_sqrt():
    result = evaluate_expression("sqrt(49)")
    assert math.isclose(float(result), 7.0, rel_tol=1e-3)
    log_test("test_sqrt", result)

# Permutation & Combination
def test_permutation():
    result = evaluate_expression("5P2")
    assert int(result) == 20
    log_test("test_permutation", result)

def test_combination():
    result = evaluate_expression("5C3")
    assert int(result) == 10
    log_test("test_combination", result)

# Vectors
def test_vector_dot():
    result = evaluate_expression("1,2,3|4,5,6dot")
    assert math.isclose(float(result), 32.0, rel_tol=1e-3)
    log_test("test_vector_dot", result)

def test_vector_cross():
    result = evaluate_expression("1,0,0|0,1,0cross")
    assert result == "[0.0, 0.0, 1.0]"
    log_test("test_vector_cross", result)

def test_vector_magnitude():
    result = evaluate_expression("magnitude(3,4)")
    assert math.isclose(float(result), 5.0, rel_tol=1e-3)
    log_test("test_vector_magnitude", result)
