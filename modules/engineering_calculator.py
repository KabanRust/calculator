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
        try:
            return float(result.evalf())
        except TypeError:
            return str(result)

    def differentiate(self, expression):
        expr = sp.sympify(expression)
        result = sp.diff(expr, self.x)
        try:
            return float(result.evalf())
        except TypeError:
            return str(result)

    def evaluate(self, expression):
        expr = sp.sympify(expression)
        result = expr.evalf()
        try:
            return float(result)
        except TypeError:
            return str(result)
