from PySide6.QtWidgets import QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from constants import GRAPHING_FUNCTIONS


class GraphCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.valid_functions = GRAPHING_FUNCTIONS
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        
    def plot_function(self, expression, x_range=(-10, 10), step=0.1):
        try:
            self.ax.clear()
            x = np.arange(x_range[0], x_range[1], step)
            # Безопасное выполнение математических выражений
            y = eval(f"lambda x: {expression}")(x)
            
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
                y = eval(f"lambda x: {expr}")(x)
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