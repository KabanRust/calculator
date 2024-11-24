from PySide6.QtWidgets import QWidget
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

    def integrate(self, expression):
        try:
            expr = sp.sympify(expression)
            result = sp.integrate(expr, self.x)
            return result
        except sp.SympifyError as e:
            return f"Ошибка в интеграле: {e}"
        except Exception as e:
            return f"Ошибка: {e}"

    def differentiate(self, expression):
        try:
            expr = sp.sympify(expression)
            result = sp.diff(expr, self.x)
            return result
        except sp.SympifyError as e:
            return f"Ошибка в производной: {e}"
        except Exception as e:
            return f"Ошибка: {e}"


    def evaluate(self, expression):
        try:
            # Заменяем ^ на ** для совместимости
            expression = expression.replace('^', '**')
            
            # Обработка интегралов
            if expression.startswith('∫') and expression.endswith(')'):
                expr = expression[2:-1]  # Убираем символы '∫(' и ')'
                result = self.integrate(expr)
            # Обработка производных
            elif expression.startswith('d/dx') and expression.endswith(')'):
                expr = expression[5:-1]  # Убираем символы 'd/dx(' и ')'
                result = self.differentiate(expr)
            else:
                # Общая обработка выражений
                result = sp.sympify(expression).evalf()

            return result
        except sp.SympifyError as e:
            return f"Ошибка: Невозможно преобразовать выражение ({e})"
        except Exception as e:
            return f"Ошибка: {e}"