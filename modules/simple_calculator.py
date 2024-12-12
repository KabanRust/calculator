from PySide6.QtWidgets import QWidget
from sympy import sympify
import json
with open("data/constants.json", "r") as file:
    constants = json.load(file)

SIMPLE_OPERATORS = constants["SIMPLE_OPERATORS"]
SIMPLE_FUNCTIONS = constants["SIMPLE_FUNCTIONS"]

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
