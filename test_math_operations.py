from math_operations import evaluate_expression
import math

# === Basic Arithmetic ===
def test_basic_addition():
    result = evaluate_expression("5+3")
    assert math.isclose(float(result), 8.0, rel_tol=1e-3)

def test_power_operation():
    result = evaluate_expression("2^3")
    assert math.isclose(float(result), 8.0, rel_tol=1e-3)

# === Number Conversions ===
def test_binary_to_decimal():
    result = evaluate_expression("1010dec")
    assert result == "10"

def test_decimal_to_binary():
    result = evaluate_expression("10bin")
    assert result == "0b1010"

def test_decimal_to_hex():
    result = evaluate_expression("15hex")
    assert result == "0xf"

def test_invalid_conversion():
    result = evaluate_expression("invalidbin")
    assert "Error" in result

# === Trigonometry ===
def test_sin():
    result = evaluate_expression("sin(30)")
    assert math.isclose(float(result), 0.5, rel_tol=1e-3)

def test_cos():
    result = evaluate_expression("cos(60)")
    assert math.isclose(float(result), 0.5, rel_tol=1e-3)

def test_tan():
    result = evaluate_expression("tan(45)")
    assert math.isclose(float(result), 1.0, rel_tol=1e-2)


# === Log and Square Root ===
def test_log10():
    result = evaluate_expression("log(1000)")
    assert math.isclose(float(result), 3.0, rel_tol=1e-3)

def test_sqrt():
    result = evaluate_expression("sqrt(49)")
    assert math.isclose(float(result), 7.0, rel_tol=1e-3)

# === Permutation & Combination ===
def test_permutation():
    result = evaluate_expression("5P2")
    assert int(result) == 20

def test_combination():
    result = evaluate_expression("5C3")
    assert int(result) == 10

# === Vectors ===
def test_vector_dot():
    result = evaluate_expression("1,2,3|4,5,6dot")
    assert math.isclose(float(result), 32.0, rel_tol=1e-3)

def test_vector_cross():
    result = evaluate_expression("1,0,0|0,1,0cross")
    assert result == "[0.0, 0.0, 1.0]"

def test_vector_magnitude():
    result = evaluate_expression("magnitude(3,4)")
    assert math.isclose(float(result), 5.0, rel_tol=1e-3)
