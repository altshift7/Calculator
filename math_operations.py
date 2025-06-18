import math
from logger import logger 

def evaluate_expression(expression: str) -> str:
    try:
        expression = expression.strip()
        logger.info(f"Evaluating expression: {expression}")
        
        if is_basic(expression):
            result = str(eval_basic(expression))
        elif is_advanced(expression):
            result = str(evaluate_advanced(expression))
        elif is_permutation_combination(expression):
            result = str(evaluate_permutation_combination(expression))
        elif is_number_conversion(expression):
            result = str(evaluate_number_conversion(expression))
        elif is_vector_operation(expression):
            result = str(evaluate_vector_operation(expression))
        else:
            result = "Unsupported expression"
        
        logger.info(f"Result: {result}")
        return result

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        logger.error(error_msg)
        return error_msg

# Expression Type Checks
def is_basic(expr): 
    return any(op in expr for op in "+-*/^") and not is_vector_operation(expr)

def is_advanced(expr): 
    return any(func in expr for func in [
        "sin", "cos", "tan", "log", "sqrt", "π"
    ])

def is_permutation_combination(expr): 
    return 'P' in expr or 'C' in expr

def is_number_conversion(expr): 
    return any(conv in expr.lower() for conv in ["bin", "hex", "dec"])

def is_vector_operation(expr): 
    return any(op in expr for op in ['dot', 'cross', 'magnitude'])

# Basic Operations
def eval_basic(expr):
    expr = expr.replace("^", "**").replace("π", str(math.pi))
    return eval(expr)

# Advanced Math
def evaluate_advanced(expr):
    expr = expr.replace("π", str(math.pi))
    if "sin(" in expr:
        return evaluate_trig(expr, "sin")
    if "cos(" in expr:
        return evaluate_trig(expr, "cos")
    if "tan(" in expr:
        return evaluate_trig(expr, "tan")

    if "log(" in expr:
        return evaluate_log(expr)
    if "sqrt(" in expr:
        return evaluate_sqrt(expr)
    raise ValueError("Unsupported advanced expression")

def evaluate_trig(expr, func):
    val = extract_number(expr, func)
    func_map = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan
    }
    return func_map[func](math.radians(val))

def evaluate_log(expr):
    val = extract_number(expr, "log")
    if val <= 0:
        raise ValueError("log input must be > 0")
    return math.log10(val)

def evaluate_sqrt(expr):
    val = extract_number(expr, "sqrt")
    if val < 0:
        raise ValueError("sqrt input must be >= 0")
    return math.sqrt(val)

def extract_number(expr, func):
    prefix = func + "("
    if expr.startswith(prefix) and expr.endswith(")"):
        return float(expr[len(prefix):-1])
    raise ValueError(f"Invalid format for {func}: {expr}")

# Permutation / Combination
def evaluate_permutation_combination(expr):
    if 'P' in expr:
        n, r = map(int, expr.split('P'))
        return math.perm(n, r)
    elif 'C' in expr:
        n, r = map(int, expr.split('C'))
        return math.comb(n, r)
    raise ValueError("Invalid P/C expression")

# Number Conversion
def evaluate_number_conversion(expr):
    expr = expr.lower()
    try:
        if 'bin' in expr:
            return bin(int(expr.split('bin')[0].strip()))
        elif 'hex' in expr:
            return hex(int(expr.split('hex')[0].strip()))
        elif 'dec' in expr:
            return str(int(expr.split('dec')[0].strip(), 2))
    except Exception:
        raise ValueError("Invalid number format")
    raise ValueError("Unsupported number conversion")

# Vector Operations
def evaluate_vector_operation(expr):
    try:
        if "dot" in expr:
            v1, v2 = extract_vectors(expr, "dot")
            return sum(a * b for a, b in zip(v1, v2))
        elif "cross" in expr:
            v1, v2 = extract_vectors(expr, "cross")
            return cross_product(v1, v2)
        elif "magnitude(" in expr:
            v = list(map(float, expr.replace("magnitude(", "").replace(")", "").split(',')))
            return math.sqrt(sum(a**2 for a in v))
    except Exception:
        raise ValueError("Invalid vector operation")
    raise ValueError("Unsupported vector expression")

def extract_vectors(expr, op):
    try:
        v1_str, v2_str = expr.replace(op, "").split('|')
        v1 = list(map(float, v1_str.strip().split(',')))
        v2 = list(map(float, v2_str.strip().split(',')))
        if len(v1) != 3 or len(v2) != 3:
            raise ValueError("Vectors must have 3 components")
        return v1, v2
    except Exception:
        raise ValueError("Vector format must be: x1,y1,z1" + op + "x2,y2,z2")

def cross_product(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]
