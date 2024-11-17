from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from modules import SimpleCalculator, EngineeringCalculator, MatrixCalculator, ProgrammableCalculator, AccountingCalculator, CurrencyCalculator, NumberCalculator, GraphCalculator, FinancialCalculator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 800, 600)

        # Создание центрального виджета
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем QTabWidget для переключения между калькуляторами
        self.tab_widget = QTabWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(self.tab_widget)

        # Инициализация калькуляторов
        self.simple_calculator = SimpleCalculator()
        self.engineering_calculator = EngineeringCalculator()
        self.matrix_calculator = MatrixCalculator()
        self.financial_calculator = FinancialCalculator()
        self.graph_calculator = GraphCalculator()
        self.number_calculator = NumberCalculator()
        self.accounting_calculator = AccountingCalculator()
        self.programmable_calculator = ProgrammableCalculator()
        self.currency_calculator = CurrencyCalculator()

        # Добавляем вкладки для каждого калькулятора
        self.tab_widget.addTab(self.simple_calculator, "Простой калькулятор")
        self.tab_widget.addTab(self.engineering_calculator, "Инженерный калькулятор")
        self.tab_widget.addTab(self.matrix_calculator, "Матрицы")
        self.tab_widget.addTab(self.financial_calculator, "Финансовый калькулятор")
        self.tab_widget.addTab(self.graph_calculator, "Графики")
        self.tab_widget.addTab(self.number_calculator, "Системы счисления")
        self.tab_widget.addTab(self.accounting_calculator, "Бухгалтерия")
        self.tab_widget.addTab(self.programmable_calculator, "Программируемый калькулятор")
        self.tab_widget.addTab(self.currency_calculator, "Валютный калькулятор")

        # По умолчанию, открываем первый калькулятор
        self.tab_widget.setCurrentIndex(0)


class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Пример UI для простого калькулятора
        self.result_label = QLabel("Результат: 0", self)
        layout.addWidget(self.result_label)

        self.button = QPushButton("Пример кнопки", self)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def calculate(self, expression):
        # Логика для вычислений, например, использование SymPy
        pass


