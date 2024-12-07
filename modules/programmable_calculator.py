from PySide6.QtWidgets import QWidget
from sympy import symbols, sympify
from constants import PROGRAMMABLE_FUNCTIONS

class ProgrammableCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.functions = {}
        self.valid_functions = PROGRAMMABLE_FUNCTIONS
        self.variables = {}  # Добавляем хранение переменных
        
    def define_function(self, name, params, expression):
        """
        Определяет новую функцию
        :param name: Имя функции
        :param params: Список параметров
        :param expression: Строка с выражением
        """
        try:
            param_symbols = symbols(params)
            parsed_expression = sympify(expression)
            self.functions[name] = {
                'params': param_symbols,
                'expression': parsed_expression
            }
            return True, f"Функция '{name}' успешно определена"
        except Exception as e:
            return False, f"Ошибка при определении функции: {str(e)}"

    def call_function(self, name, args):
        """
        Вызывает определённую функцию
        :param name: Имя функции
        :param args: Список аргументов
        """
        if name not in self.functions:
            return False, f"Функция '{name}' не найдена"
            
        func = self.functions[name]
        if len(args) != len(func['params']):
            return False, "Неверное количество аргументов"
            
        try:
            # Создаём словарь подстановок параметр:значение
            substitutions = dict(zip(func['params'], args))
            result = func['expression'].evalf(subs=substitutions)
            return True, float(result)
        except Exception as e:
            return False, f"Ошибка при вызове функции: {str(e)}"

    def set_variable(self, name, value):
        """
        Устанавливает значение переменной
        """
        try:
            self.variables[name] = float(value)
            return True, f"Переменная {name} = {value}"
        except ValueError:
            return False, "Неверное значение переменной"

    def get_variable(self, name):
        """
        Получает значение переменной
        """
        return self.variables.get(name)

    def list_functions(self):
        """
        Возвращает список определённых функций
        """
        result = []
        for name, func in self.functions.items():
            params = ', '.join(str(p) for p in func['params'])
            result.append(f"{name}({params}) = {func['expression']}")
        return result

    def list_variables(self):
        """
        Возвращает список определённых переменных
        """
        return [f"{name} = {value}" for name, value in self.variables.items()]