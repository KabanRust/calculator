from PyQt6.QtWidgets import QWidget
import sympy as sp
import math
from constants import ENGINEERING_OPERATORS, ENGINEERING_FUNCTIONS, PI, E
from modules.simple_calculator import SimpleCalculator

class EngineeringCalculator(SimpleCalculator, QWidget):
    def __init__(self):
        super().__init__()
        self.operators = ENGINEERING_OPERATORS
        self.functions = ENGINEERING_FUNCTIONS
        self.PI = PI
        self.E = E
        self.x = sp.symbols('x')

    def power(self, a, b):
        return float(a) ** float(b)

    def root(self, a):
        expr = sp.sympify(a)
        result = sp.sqrt(expr)
        try:
            return float(result.evalf())
        except (TypeError, ValueError):
            return str(result)

    def log(self, a, base=math.e):
        return math.log(float(a), base)

    def ln(self, a):
        return math.log(float(a))

    def sin(self, angle):
        return math.sin(float(angle))

    def cos(self, angle):
        return math.cos(float(angle))

    def tan(self, angle):
        return math.tan(float(angle))

    def reciprocal(self, a):
        return 1 / float(a)

    def factorial(self, a):
        return math.factorial(int(a))

    def integrate(self, expression, a=None, b=None):
        expr = sp.sympify(expression)
        if a is not None and b is not None:
            result = sp.integrate(expr, (self.x, a, b))
        else:
            result = sp.integrate(expr, self.x)
        return result

    def differentiate(self, expression):
        expr = sp.sympify(expression)
        result = sp.diff(expr, self.x)
        return result

    def evaluate(self, expression):
        try:
            if '∫' in expression:
                # Обработка интегралов
                parts = expression.split('∫')
                if '|' in parts[1]:
                    expr, bounds = parts[1].split('|')
                    a, b = map(float, bounds.split(','))
                    result = self.integrate(expr, a, b)
                else:
                    expr = parts[1]
                    result = self.integrate(expr)
            elif 'd/dx' in expression:
                # Обработка производных
                parts = expression.split('d/dx')
                expr = parts[1]
                result = self.differentiate(expr)
            else:
                result = sp.sympify(expression).evalf()
            return float(result.evalf())
        except Exception as e:
            return f"Ошибка: {e}"