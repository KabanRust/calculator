from PySide6.QtWidgets import QWidget
import sympy as sp
import math
import json
with open("data/constants.json", "r") as file:
    constants = json.load(file)

ENGINEERING_OPERATORS = constants["ENGINEERING_OPERATORS"]
ENGINEERING_FUNCTIONS = constants["ENGINEERING_FUNCTIONS"]
PI = constants["PI"]
E = constants["E"]
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
            expression = expression.replace('^', '**')
            
            while '∫(' in expression or 'd/dx(' in expression:
                if '∫(' in expression:
                    start = expression.index('∫(')
                    end = self.find_matching_parenthesis(expression, start + 2)
                    integral_expr = expression[start+2:end]
                    integral_result = self.integrate(integral_expr)
                    expression = expression[:start] + str(integral_result) + expression[end+1:]
                
                if 'd/dx(' in expression:
                    start = expression.index('d/dx(')
                    end = self.find_matching_parenthesis(expression, start + 5)
                    diff_expr = expression[start+5:end]
                    diff_result = self.differentiate(diff_expr)
                    expression = expression[:start] + str(diff_result) + expression[end+1:]
            
            result = sp.sympify(expression).evalf()
            return result
        
        except sp.SympifyError as e:
            return f"Ошибка: Невозможно преобразовать выражение ({e})"
        except Exception as e:
            return f"Ошибка: {e}"

    def find_matching_parenthesis(self, s, start):
        count = 1
        for i in range(start + 1, len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
                if count == 0:
                    return i
        raise ValueError("Несбалансированные скобки")