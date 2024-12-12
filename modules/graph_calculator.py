from PySide6.QtWidgets import QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import json
with open("data/constants.json", "r") as file:
    constants = json.load(file)
ENGINEERING_OPERATORS = constants["ENGINEERING_OPERATORS"]
ENGINEERING_FUNCTIONS = constants["ENGINEERING_FUNCTIONS"]
PI = constants["PI"]
E = constants["E"]
GRAPHING_FUNCTIONS = constants["GRAPHING_FUNCTIONS"]
MATH_CONSTANTS = constants["MATH_CONSTANTS"]

class MathParser:
    def __init__(self):
        self.safe_functions = {
            'sqrt': np.sqrt,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'sinh': np.sinh,
            'cosh': np.cosh,
            'tanh': np.tanh,
            'exp': np.exp,
            'log': np.log,
            'log10': np.log10,
            'sqrt': np.sqrt,
            'abs': np.abs,
        }
        self.safe_functions.update(MATH_CONSTANTS)
        
    def validate_function(self, function_name):
        return function_name in GRAPHING_FUNCTIONS, ENGINEERING_FUNCTIONS
        
    def evaluate(self, expression, x):
        namespace = {
            'x': x,
            **self.safe_functions
        }
        return eval(expression, {"__builtins__": {}}, namespace)

class GraphCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.valid_functions = GRAPHING_FUNCTIONS
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.math_parser = MathParser()
        
    def preprocess_expression(self, expression):
        expression = expression.replace('^', '**')
        
        for func in GRAPHING_FUNCTIONS:
            if func in expression and not self.math_parser.validate_function(func):
                raise ValueError(f"Неподдерживаемая функция: {func}")
                
        return expression
        
    def plot_function(self, expression, x_range=(-10, 10), step=0.1):
        try:
            self.ax.clear()
            x = np.arange(x_range[0], x_range[1], step)
            
            expression = self.preprocess_expression(expression)
            
            y = self.math_parser.evaluate(expression, x)
            
            self.ax.plot(x, y, label=f"y = {expression}")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.set_title("График функции")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()
            return True
            
        except Exception as e:
            return f"Ошибка построения графика: {e}"
    
    def plot_multiple_functions(self, expressions, x_range=(-10, 10), step=0.1):
        try:
            self.ax.clear()
            x = np.arange(x_range[0], x_range[1], step)
            
            for expr in expressions:
                expr = self.preprocess_expression(expr)
                
                y = self.math_parser.evaluate(expr, x)
                self.ax.plot(x, y, label=f"y = {expr}")
            
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.set_title("Графики функций")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()
            return True
            
        except Exception as e:
            return f"Ошибка построения графиков: {e}"

    def clear_plot(self):
        self.ax.clear()
        self.ax.grid(True)
        self.canvas.draw()

    def set_plot_range(self, x_min, x_max, y_min, y_max):
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.canvas.draw()

    def get_canvas(self):
        return self.canvas
    
    import numpy as np

def test_sqrt(x):
    return np.sqrt(x)
