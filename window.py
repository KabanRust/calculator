from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel, QSpinBox
from PySide6.QtCore import Qt
from sympy import sympify
import sympy as sp
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

        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        # Изначально скрываем строки для пределов интегралов
        self.lower_bound = QLineEdit()
        self.lower_bound.setPlaceholderText("Нижний предел")
        self.upper_bound = QLineEdit()
        self.upper_bound.setPlaceholderText("Верхний предел")
        self.lower_bound.hide()
        self.upper_bound.hide()
        layout.addWidget(self.lower_bound)
        layout.addWidget(self.upper_bound)

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
            extra_buttons = ('x', 'y', 'z', 'a', 'b')
            base_buttons[4] += extra_buttons

        for row in base_buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.make_button_callback(button_text, self.input_line))
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
        tab = QWidget()
        layout = QVBoxLayout()

        # Ввод количества строк, столбцов и матриц
        self.rows_spinbox = QSpinBox()
        self.rows_spinbox.setRange(1, 5)
        self.cols_spinbox = QSpinBox()
        self.cols_spinbox.setRange(1, 5)
        self.matrices_count_spinbox = QSpinBox()
        self.matrices_count_spinbox.setRange(1, 2)

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel('Rows:'))
        size_layout.addWidget(self.rows_spinbox)
        size_layout.addWidget(QLabel('Cols:'))
        size_layout.addWidget(self.cols_spinbox)
        size_layout.addWidget(QLabel('Matrices:'))
        size_layout.addWidget(self.matrices_count_spinbox)

        self.set_size_button = QPushButton('Set Size')
        self.set_size_button.clicked.connect(self.set_matrix_size)
        size_layout.addWidget(self.set_size_button)
        layout.addLayout(size_layout)

        # Макеты для матриц
        self.matrix_layouts = [QGridLayout() for _ in range(2)]
        for matrix_layout in self.matrix_layouts:
            layout.addLayout(matrix_layout)

        # Макет для результата
        self.result_layout = QGridLayout()
        layout.addLayout(self.result_layout)

        # Результат
        self.result_display = QLineEdit()
        layout.addWidget(self.result_display)

        # Кнопки операций
        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.perform_add)
        buttons_layout.addWidget(self.add_button)

        self.subtract_button = QPushButton('Subtract')
        self.subtract_button.clicked.connect(self.perform_subtract)
        buttons_layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton('Multiply')
        self.multiply_button.clicked.connect(self.perform_multiply)
        buttons_layout.addWidget(self.multiply_button)

        self.transpose_button = QPushButton('Transpose')
        self.transpose_button.clicked.connect(self.perform_transpose)
        buttons_layout.addWidget(self.transpose_button)

        self.determinant_button = QPushButton('Determinant')
        self.determinant_button.clicked.connect(self.perform_determinant)
        buttons_layout.addWidget(self.determinant_button)

        self.inverse_button = QPushButton('Inverse')
        self.inverse_button.clicked.connect(self.perform_inverse)
        buttons_layout.addWidget(self.inverse_button)

        layout.addLayout(buttons_layout)
        tab.setLayout(layout)

        return tab

    
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
        elif text in ['sin', 'cos', 'tan', 'log', 'sqrt', '∫', 'd/dx']:
            input_line.setText(input_line.text() + text + '(')
        elif text == '=':
            expression = input_line.text()

            try:
                if expression.startswith('∫(') or expression.startswith('d/dx('):
                    result = self.engineering_calculator.evaluate(expression)
                else:
                    result = sp.sympify(expression).evalf()

                # Проверяем, является ли результат целым числом
                if result == int(result):
                    input_line.setText(str(int(result)))
                else:
                    # Для дробных чисел убираем лишние нули после запятой
                    input_line.setText(f"{result:.10f}".rstrip('0').rstrip('.'))
            except Exception as e:
                input_line.setText(f"Ошибка: {e}")
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
            Qt.Key.Key_S: 'sin', Qt.Key.Key_O: 'cos', Qt.Key.Key_T: 'tan',
            Qt.Key.Key_L: 'log', Qt.Key.Key_AsciiCircum: '^', Qt.Key.Key_Q: 'sqrt',
            Qt.Key.Key_I: '∫', Qt.Key.Key_D: 'd/dx', Qt.Key.Key_X: 'x', Qt.Key.Key_Y: 'y',
            Qt.Key.Key_Z: 'z', Qt.Key.Key_A: 'a', Qt.Key.Key_B: 'b'
        }

        key_map.update(additional_keys)

        if key in key_map:
            current_tab = self.tab_widget.currentWidget()
            input_line = current_tab.findChild(QLineEdit)
            self.on_button_click(key_map[key], input_line)

    def set_matrix_size(self):
        rows = self.rows_spinbox.value()
        cols = self.cols_spinbox.value()
        matrices_count = self.matrices_count_spinbox.value()

        # Очистка макетов матриц
        for matrix_layout in self.matrix_layouts:
            for i in reversed(range(matrix_layout.count())):
                widget = matrix_layout.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

        self.matrices = [[[QLineEdit() for _ in range(cols)] for _ in range(rows)] for _ in range(matrices_count)]

        for k, matrix in enumerate(self.matrices):
            for i in range(rows):
                for j in range(cols):
                    self.matrix_layouts[k].addWidget(matrix[i][j], i, j)

    def get_matrix(self, matrix_layout):
        rows = self.rows_spinbox.value()
        cols = self.cols_spinbox.value()
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                cell_value = matrix_layout.itemAtPosition(i, j).widget().text()
                try:
                    row.append(float(cell_value))
                except ValueError:
                    row.append(0)
            matrix.append(row)
        return matrix

    def perform_add(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        matrix2 = self.get_matrix(self.matrix_layouts[1])
        result = self.matrix_calculator.add(matrix1, matrix2)
        self.display_result(result)

    def perform_subtract(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        matrix2 = self.get_matrix(self.matrix_layouts[1])
        result = self.matrix_calculator.subtract(matrix1, matrix2)
        self.display_result(result)

    def perform_multiply(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        matrix2 = self.get_matrix(self.matrix_layouts[1])
        result = self.matrix_calculator.multiply(matrix1, matrix2)
        self.display_result(result)

    def perform_transpose(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        result = self.matrix_calculator.transpose(matrix1)
        self.display_result(result)

    def perform_determinant(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        result = self.matrix_calculator.determinant(matrix1)
        self.display_result(result)

    def perform_inverse(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        result = self.matrix_calculator.inverse(matrix1)
        self.display_result(result)

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