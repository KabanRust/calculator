from sympy import sympify
import math

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def safe_eval(expression):
    try:
        result = sympify(expression).evalf()
        return float(result)
    except Exception as e:
        return f"Ошибка: {e}"

def to_power(base, exponent):
    try:
        return math.pow(float(base), float(exponent))
    except ValueError as e:
        return f"Ошибка: {e}"

def factorial(value):
    try:
        value = int(value)
        if value < 0:
            return "Ошибка: Факториал отрицательного числа не определён"
        return math.factorial(value)
    except ValueError:
        return "Ошибка: Неверное значение для факториала"

def convert_base(number, from_base, to_base):
    try:
        decimal_value = int(str(number), from_base)
        if to_base == 10:
            return str(decimal_value)
        digits = "0123456789ABCDEF"
        result = ""
        while decimal_value > 0:
            result = digits[decimal_value % to_base] + result
            decimal_value //= to_base
        return result if result else "0"
    except ValueError:
        return "Ошибка: Неверное значение или база"
    
def validate_expression(expression, allowed_operators):
    try:
        for char in expression:
            if char.isalnum() or char.isspace() or char in allowed_operators:
                continue
            return f"Ошибка: Неверный символ '{char}'"
        return None
    except Exception as e:
        return f"Ошибка: {e}"
