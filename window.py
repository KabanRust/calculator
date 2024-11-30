from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel, QSpinBox, QMessageBox, QGroupBox, QTextEdit, QComboBox, QFormLayout, QDoubleSpinBox
from PySide6.QtCore import Qt
from sympy import sympify
import sympy as sp
from constants import SIMPLE_OPERATORS, SIMPLE_FUNCTIONS, ENGINEERING_OPERATORS, ENGINEERING_FUNCTIONS
import modules
from methods import Accounting_func, Button_methods, Currency_methods, Finans_methods, Graph_methods, Matrix_perform, Number_func, Programmable_func, Matrix_size, hotkey
from create_tabs import Accounting_tab, Currency_tab, Finans_tab, Graph_tab, Matrix_tab, Number_tab, Programmable_tab

class Matrix_interface:
    def __init__(self):
        self.matrix_size = Matrix_size()
        self.matrix_perform = Matrix_perform()

    def Matrix_size_interface(self):
        self.matrix_size.set_matrix_size()

    def Get_matrix_interface(self):    
        matrix = self.matrix_size.get_matrix()
    
    def per_add(self):
        self.matrix_perform.perform_add()

    def per_subtract(self):
        self.matrix_perform.perform_subtract()

    def per_multiply(self):
        self.matrix_perform.perform_multiply()

    def per_transpose(self):
        self.matrix_perform.perform_transpose()

    def per_determinant(self):
        self.matrix_perform.perform_determinant()

    def per_inverse(self):
        self.matrix_perform.perform_inverse()

    def display_result(self, result):
        if isinstance(result, list):
            # Удалим старые виджеты результата, если они существуют
            for i in reversed(range(self.result_layout.count())):
                widget = self.result_layout.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

            # Отобразим результат в виде матрицы
            rows = len(result)
            cols = len(result[0])
            result_matrix = [[QLineEdit(str(result[i][j])) for j in range(cols)] for i in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    self.result_layout.addWidget(result_matrix[i][j], i, j)
        else:
            # Если результат не матрица, выводим его в виде строки
            self.result_display.setText(str(result))


class Button(Matrix_interface):
    def __init__(self):
        self.button_methods = Button_methods
        self.hotkey = hotkey

    def on_button_click(self, text, input_line):
        if text == 'C':
            input_line.clear()
        elif text == '←':
            current_text = input_line.text()
            input_line.setText(current_text[:-1])
        elif text == '%':
            self.button_methods.percent()
        elif text in ['sin', 'cos', 'tan', 'log', 'sqrt', '∫', 'd/dx']:
            input_line.setText(input_line.text() + text)
        elif text == '=':
            self.button_methods.sumbols_but()
        else:
            input_line.setText(input_line.text() + text)

    def KeyPress(self):
        self.hotkey.keyPressEvent()


class Methods:
    def __init__(self):
        self.accounting_func = Accounting_func
        self.currency_method = Currency_methods
        self.finans_method = Finans_methods
        self.graph_methods = Graph_methods
        self.number_func = Number_func
        self.programmable_func = Programmable_func

    def currency_methods(self):
        self.currency_method.perform_currency_conversion()
        self.currency_method.update_currency_rates()
        self.currency_method.make_button_callback()

    def finans_methods(self):
        self.finans_method.calculate_fv()
        self.finans_method.calculate_irr()
        self.finans_method.calculate_npv()
        self.finans_method.calculate_pv()

    def accounting_methods(self):
        self.accounting_func.calculate_depreciation()
        self.accounting_func.calculate_loan()
        self.accounting_func.calculate_vat()

    def number_methods(self):
        self.number_func.convert_number()
        self.number_func.on_number_button_click()
        self.number_func.clear_number_input()


class Create_tab(Button, Methods):
    def __init__(self):
        self.accounting_tab = Accounting_tab
        self.currency_tab = Currency_tab
        self.finans_tab = Finans_tab
        self.graph_tab = Graph_tab
        self.matrix_tab = Matrix_tab
        self.number_tab = Number_tab
        self.programmable_tab = Programmable_tab

    def create_calculator_tab(self, operators, functions, include_extra_buttons=False):
        tab = QWidget()
        layout = QVBoxLayout()

        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        button_layout = QVBoxLayout()
        base_buttons = [
            ('C', '←', '%', '(', ')'),
            ('7', '8', '9'),
            ('4', '5', '6'),
            ('1', '2', '3'),
            ('0',) + tuple(operators),
            tuple(functions) + ('=',)
        ]

        if include_extra_buttons:
            extra_buttons = ('x', 'y')
            base_buttons[4] += extra_buttons

        for row in base_buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(lambda _, text=button_text: self.currency_method.make_button_callback(text, self.input_line))
                row_layout.addWidget(button)
            button_layout.addLayout(row_layout)

        layout.addLayout(button_layout)
        tab.setLayout(layout)

        return tab


    def create_simple_calculator_tab(self):
        return self.create_calculator_tab(SIMPLE_OPERATORS, SIMPLE_FUNCTIONS)

    def create_engineering_calculator_tab(self):
        return self.create_calculator_tab(ENGINEERING_OPERATORS, ENGINEERING_FUNCTIONS, include_extra_buttons=True)
    
    def create_matrix_calculator_tab(self):
        return self.matrix_tab.matrix_calculator_tab(self)

    def create_finans_calculator_tab(self):
        return self.finans_tab.financial_tab(self)

    def create_graph_calculator_tab(self):
        return self.graph_tab.graph_calculator_tab(self)

    def create_number_calculator_tab(self):
        return self.number_tab.number_calculator_tab(self)

    def create_accounting_calculator_tab(self):
        return self.accounting_tab.accounting_calculator_tab(self)

    def create_programmable_calculator_tab(self):
        return self.programmable_tab.programmable_calculator_tab(self)

    def create_currency_calculator_tab(self):
        return self.currency_tab.currency_calculator_tab(self)


class MainWindow(QMainWindow, Create_tab, Methods):
    def __init__(self):
        super().__init__()

        self.matrix_size_instance = Matrix_size()
        self.matrix_tab = Matrix_tab(self.matrix_size_instance)

        self.setWindowTitle("Калькулятор")
        screen = QApplication.primaryScreen().geometry()
        screen_width, screen_height = screen.width(), screen.height()
        self.setGeometry(100, 100, int(screen_width * 0.5), int(screen_height * 0.5))

        # Создание центрального виджета
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем QTabWidget для переключения между калькуляторами
        self.tab_widget = QTabWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(self.tab_widget)

        # Инициализация калькуляторов
        self.simple_calculator = modules.SimpleCalculator()
        self.engineering_calculator = modules.EngineeringCalculator()
        self.matrix_calculator = modules.MatrixCalculator()
        self.financial_calculator = modules.FinancialCalculator()
        self.graph_calculator = modules.GraphCalculator()
        self.number_calculator = modules.NumberCalculator()
        self.accounting_calculator = modules.AccountingCalculator()
        self.programmable_calculator = modules.ProgrammableCalculator()
        self.currency_calculator = modules.CurrencyCalculator()

        # Добавляем вкладки для калькуляторов
        self.tab_widget.addTab(self.create_simple_calculator_tab(), "Простой калькулятор")
        self.tab_widget.addTab(self.create_engineering_calculator_tab(), "Инженерный калькулятор")
        self.tab_widget.addTab(self.matrix_tab.matrix_calculator_tab(self), "Матрицы")
        self.tab_widget.addTab(self.finans_tab.financial_tab(self), "Финансовый калькулятор")
        self.tab_widget.addTab(self.graph_tab.graph_calculator_tab(self), "Графики")
        self.tab_widget.addTab(self.number_tab.number_calculator_tab(self), "Системы счисления")
        self.tab_widget.addTab(self.accounting_tab.accounting_calculator_tab(self), "Бухгалтерия")
        self.tab_widget.addTab(self.programmable_tab.programmable_calculator_tab(self), "Программируемый калькулятор")
        self.tab_widget.addTab(self.currency_tab.currency_calculator_tab(self), "Валютный калькулятор")

        # По умолчанию, открываем первый калькулятор
        self.tab_widget.setCurrentIndex(0)