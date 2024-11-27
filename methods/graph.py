from PySide6.QtWidgets import QMessageBox

class Graph_methods:
    def plot_graph(self):
        expression = self.function_input.text()
        result = self.graph_calculator.plot_function(
            expression,
            x_range=(self.x_min.value(), self.x_max.value()),
            step=0.1
        )
        if result is not True:
            QMessageBox.warning(self, "Ошибка", str(result))

    def clear_graph(self):
        self.graph_calculator.clear_plot()
        self.function_input.clear()

    def apply_graph_range(self):
        self.graph_calculator.set_plot_range(
            self.x_min.value(),
            self.x_max.value(),
            self.y_min.value(),
            self.y_max.value()
        )