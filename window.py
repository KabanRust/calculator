from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from sympy import sympify
from constants import SIMPLE_OPERATORS, SIMPLE_FUNCTIONS, ENGINEERING_OPERATORS, ENGINEERING_FUNCTIONS, MATRIX_OPERATIONS, FINANCIAL_FUNCTIONS, ACCOUNTING_FUNCTIONS, GRAPHING_FUNCTIONS, CURRENCY_SYMBOLS, PROGRAMMABLE_FUNCTIONS
import modules

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
        self.tab_widget.addTab(self.create_matrix_calculator_tab(), "Матрицы")
        self.tab_widget.addTab(self.create_financial_calculator_tab(), "Финансовый калькулятор")
        self.tab_widget.addTab(self.create_graph_calculator_tab(), "Графики")
        self.tab_widget.addTab(self.create_number_calculator_tab(), "Системы счисления")
        self.tab_widget.addTab(self.create_accounting_calculator_tab(), "Бухгалтерия")
        self.tab_widget.addTab(self.create_programmable_calculator_tab(), "Программируемый калькулятор")
        self.tab_widget.addTab(self.create_currency_calculator_tab(), "Валютный калькулятор")

        # По умолчанию, открываем первый калькулятор
        self.tab_widget.setCurrentIndex(0)

    def create_calculator_tab(self, operators, functions, include_extra_buttons=False):
        tab = QWidget()
        layout = QVBoxLayout()

        input_line = QLineEdit()
        layout.addWidget(input_line)

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
            extra_buttons = ('x', 'y', 'z', 'a', 'b', '|')
            base_buttons[4] += extra_buttons

        for row in base_buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.make_button_callback(button_text, input_line))
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
        return self.create_calculator_tab(MATRIX_OPERATIONS, [], include_extra_buttons=True)

    def create_financial_calculator_tab(self):
        return self.create_calculator_tab([], FINANCIAL_FUNCTIONS)

    def create_graph_calculator_tab(self):
        return self.create_calculator_tab([], GRAPHING_FUNCTIONS, include_extra_buttons=True)

    def create_number_calculator_tab(self):
        return self.create_calculator_tab([], [])

    def create_accounting_calculator_tab(self):
        return self.create_calculator_tab([], ACCOUNTING_FUNCTIONS)

    def create_programmable_calculator_tab(self):
        return self.create_calculator_tab([], PROGRAMMABLE_FUNCTIONS, include_extra_buttons=True)

    def create_currency_calculator_tab(self):
        return self.create_calculator_tab([], CURRENCY_SYMBOLS)

    def make_button_callback(self, text, input_line):
        def callback():
            self.on_button_click(text, input_line)
        return callback

    def on_button_click(self, text, input_line):
        if text == 'C':
            input_line.clear()
        elif text == '←':
            current_text = input_line.text()
            input_line.setText(current_text[:-1])
        elif text == '%':
            try:
                result = str(float(input_line.text()) / 100)
                input_line.setText(result)
            except ValueError:
                input_line.setText("Ошибка")
        elif text == '=':
            expression = input_line.text()
            try:
                result = sympify(expression).evalf()

                if '∫' in expression:
                    parts = expression.split('∫')
                    if '|' in parts[1]:
                        expr, bounds = parts[1].split('|')
                        a, b = map(float, bounds.split(','))
                        result = self.integrate(expr, a, b)
                        input_line.setText(str(result))
                    else:
                        expr = parts[1]
                        result = self.integrate(expr)
                        input_line.setText(str(result))
                elif 'd/dx' in expression:
                    parts = expression.split('d/dx')
                    expr = parts[1]
                    result = self.differentiate(expr)
                    input_line.setText(str(result))
                else:
                    if '.' in expression:
                        decimal_places = max(
                            len(part.split('.')[1]) for part in expression.split() if '.' in part
                        )
                        input_line.setText(f"{result:.{decimal_places}f}")
                    else:
                        input_line.setText(f"{int(result)}")
            except Exception as e:
                input_line.setText("Ошибка")
        else:
            input_line.setText(input_line.text() + text)



    def keyPressEvent(self, event):
        key = event.key()
        key_map = {
            Qt.Key.Key_0: '0', Qt.Key.Key_1: '1', Qt.Key.Key_2: '2', Qt.Key.Key_3: '3',
            Qt.Key.Key_4: '4', Qt.Key.Key_5: '5', Qt.Key.Key_6: '6', Qt.Key.Key_7: '7',
            Qt.Key.Key_8: '8', Qt.Key.Key_9: '9', Qt.Key.Key_Plus: '+', Qt.Key.Key_Minus: '-',
            Qt.Key.Key_Asterisk: '*', Qt.Key.Key_Slash: '/', Qt.Key.Key_ParenLeft: '(',
            Qt.Key.Key_ParenRight: ')', Qt.Key.Key_Period: '.', Qt.Key.Key_Backspace: '←',
            Qt.Key.Key_C: 'C', Qt.Key.Key_Enter: '=', Qt.Key.Key_Return: '=', Qt.Key.Key_Percent: '%'
        }

        additional_keys = {
            Qt.Key.Key_S: 'sin(', Qt.Key.Key_O: 'cos(', Qt.Key.Key_T: 'tan(',
            Qt.Key.Key_L: 'log(', Qt.Key.Key_AsciiCircum: '^', Qt.Key.Key_Q: 'sqrt(',
            Qt.Key.Key_I: '∫(', Qt.Key.Key_D: 'd/dx', Qt.Key.Key_X: 'x', Qt.Key.Key_Y: 'y', Qt.Key.Key_Z: 'z', Qt.Key.Key_A: 'a', Qt.Key.Key_B: 'b'
        }

        key_map.update(additional_keys)

        if key in key_map:
            current_tab = self.tab_widget.currentWidget()
            input_line = current_tab.findChild(QLineEdit)
            self.on_button_click(key_map[key], input_line)