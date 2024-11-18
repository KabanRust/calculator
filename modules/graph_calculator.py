from PySide6.QtWidgets import QWidget
import matplotlib.pyplot as plt
import numpy as np
from constants import GRAPHING_FUNCTIONS


class GraphCalculator(QWidget):
    def __init__(self):
        self.valid_functions = GRAPHING_FUNCTIONS

        super().__init__()

    def plot_function(self, expression, x_range=(-10, 10), step=0.1):
        try:
            x = np.arange(x_range[0], x_range[1], step)
            y = [eval(expression, {"x": xi, "np": np}) for xi in x]

            plt.plot(x, y, label=f"y = {expression}")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("График функции")
            plt.grid(True)
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Ошибка построения графика: {e}")

    def scatter_plot(self, x_values, y_values):
        try:
            if len(x_values) != len(y_values):
                raise ValueError("Количество значений X и Y должно совпадать.")

            plt.scatter(x_values, y_values, color='blue', marker='o')
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Точечная диаграмма")
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"Ошибка построения точечной диаграммы: {e}")

    def bar_chart(self, categories, values):
        try:
            if len(categories) != len(values):
                raise ValueError("Количество категорий и значений должно совпадать.")

            plt.bar(categories, values, color='green')
            plt.xlabel("Категории")
            plt.ylabel("Значения")
            plt.title("Столбчатая диаграмма")
            plt.grid(axis='y')
            plt.show()
        except Exception as e:
            print(f"Ошибка построения столбчатой диаграммы: {e}")
