from PyQt6.QtWidgets import QWidget
from sympy import symbols, sympify
from constants import PROGRAMMABLE_FUNCTIONS


class ProgrammableCalculator(QWidget):
    def __init__(self):
        self.functions = {}
        self.valid_functions = PROGRAMMABLE_FUNCTIONS

        super().__init__()

    def define_function(self, name, expression, variables):
        try:
            variables = symbols(variables)
            parsed_expression = sympify(expression)
            self.functions[name] = (parsed_expression, variables)
            return f"Функция '{name}' успешно определена."
        except Exception as e:
            return f"Ошибка при определении функции: {e}"

    def call_function(self, name, *args):
        if name not in self.functions:
            return f"Ошибка: Функция '{name}' не найдена."

        try:
            expression, variables = self.functions[name]
            if len(args) != len(variables):
                return "Ошибка: Неверное количество аргументов."

            substitutions = {var: val for var, val in zip(variables, args)}
            return float(expression.evalf(subs=substitutions))
        except Exception as e:
            return f"Ошибка выполнения функции '{name}': {e}"

    def list_functions(self):
        if not self.functions:
            return "Нет сохраненных функций."
        return [f"{name}({', '.join(map(str, vars))}): {expr}" for name, (expr, vars) in self.functions.items()]

    def delete_function(self, name):
        if name in self.functions:
            del self.functions[name]
            return f"Функция '{name}' успешно удалена."
        return f"Ошибка: Функция '{name}' не найдена."
