from PySide6.QtWidgets import QWidget
from sympy import sympify
from constants import SIMPLE_OPERATORS, SIMPLE_FUNCTIONS

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.operators = SIMPLE_OPERATORS
        self.functions = SIMPLE_FUNCTIONS

    def evaluate(self, expression):
        try:
            result = sympify(expression).evalf()
            return float(result)
        except Exception as e:
            return f"Ошибка: {e}"
