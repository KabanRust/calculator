from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel, QSpinBox, QMessageBox, QGroupBox, QTextEdit, QComboBox, QFormLayout, QDoubleSpinBox
from PySide6.QtCore import Qt
from sympy import sympify
import sympy as sp
import json
with open("constants.json", "r") as file:
    constants = json.load(file)

SIMPLE_OPERATORS = constants["SIMPLE_OPERATORS"]
SIMPLE_FUNCTIONS = constants["SIMPLE_FUNCTIONS"]
ENGINEERING_OPERATORS = constants["ENGINEERING_OPERATORS"]
ENGINEERING_FUNCTIONS = constants["ENGINEERING_FUNCTIONS"]
PI = constants["PI"]
E = constants["E"]
FINANCIAL_FUNCTIONS = constants["FINANCIAL_FUNCTIONS"]
ACCOUNTING_FUNCTIONS = constants["ACCOUNTING_FUNCTIONS"]
GRAPHING_FUNCTIONS = constants["GRAPHING_FUNCTIONS"]
MATH_CONSTANTS = constants["MATH_CONSTANTS"]
CURRENCY_SYMBOLS = constants["CURRENCY_SYMBOLS"]
PROGRAMMABLE_FUNCTIONS = constants["PROGRAMMABLE_FUNCTIONS"]
import modules

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        screen = QApplication.primaryScreen().geometry()
        screen_width, screen_height = screen.width(), screen.height()
        self.setGeometry(100, 100, int(screen_width * 0.5), int(screen_height * 0.5))
        self.setWindowFlags(self.windowFlags() | Qt.MSWindowsFixedSizeDialogHint)

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
        self.accounting_calculator = modules.AccountingCalculator()
        self.programmable_calculator = modules.ProgrammableCalculator()
        self.currency_calculator = modules.CurrencyCalculator()

        # Добавляем вкладки для калькуляторов
        self.tab_widget.addTab(self.create_simple_calculator_tab(), "Простой калькулятор")
        self.tab_widget.addTab(self.create_engineering_calculator_tab(), "Инженерный калькулятор")
        self.tab_widget.addTab(self.create_matrix_calculator_tab(), "Матрицы")
        self.tab_widget.addTab(self.create_financial_calculator_tab(), "Финансовый калькулятор")
        self.tab_widget.addTab(self.create_graph_calculator_tab(), "Графики")
        self.tab_widget.addTab(self.create_accounting_calculator_tab(), "Бухгалтерия")
        self.tab_widget.addTab(self.create_programmable_calculator_tab(), "Программируемый калькулятор")
        self.tab_widget.addTab(self.create_currency_calculator_tab(), "Валютный калькулятор")

        # По умолчанию, открываем первый калькулятор
        self.tab_widget.setCurrentIndex(0)

    def create_calculator_tab(self, operators, functions, include_extra_buttons=False):
        tab = QWidget()
        layout = QVBoxLayout()

        self.input_line = QLineEdit()
        self.input_line.setReadOnly(True)
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
        size_layout.addWidget(QLabel('Строки:'))
        size_layout.addWidget(self.rows_spinbox)
        size_layout.addWidget(QLabel('Столбцы:'))
        size_layout.addWidget(self.cols_spinbox)
        size_layout.addWidget(QLabel('Матрицы:'))
        size_layout.addWidget(self.matrices_count_spinbox)

        self.set_size_button = QPushButton('Задайте размерность')
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

        # Кнопки операций
        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton('Cложение')
        self.add_button.clicked.connect(self.perform_add)
        buttons_layout.addWidget(self.add_button)

        self.subtract_button = QPushButton('Вычитание')
        self.subtract_button.clicked.connect(self.perform_subtract)
        buttons_layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton('Умножение')
        self.multiply_button.clicked.connect(self.perform_multiply)
        buttons_layout.addWidget(self.multiply_button)

        self.transpose_button = QPushButton('Транспонирование')
        self.transpose_button.clicked.connect(self.perform_transpose)
        buttons_layout.addWidget(self.transpose_button)

        self.determinant_button = QPushButton('Детерминант')
        self.determinant_button.clicked.connect(self.perform_determinant)
        buttons_layout.addWidget(self.determinant_button)

        self.inverse_button = QPushButton('Инверсия')
        self.inverse_button.clicked.connect(self.perform_inverse)
        buttons_layout.addWidget(self.inverse_button)

        layout.addLayout(buttons_layout)
        tab.setLayout(layout)

        return tab
    
    def create_financial_calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Группа для PV (Present Value)
        pv_group = QGroupBox("Расчет текущей стоимости (PV)")
        pv_layout = QGridLayout()
        
        self.pv_fv_input = QLineEdit()
        self.pv_rate_input = QLineEdit()
        self.pv_periods_input = QLineEdit()
        self.pv_result = QLineEdit()
        self.pv_result.setReadOnly(True)
        
        pv_calc_button = QPushButton("Рассчитать PV")
        pv_calc_button.clicked.connect(self.calculate_pv)
        
        pv_layout.addWidget(QLabel("Будущая стоимость (FV):"), 0, 0)
        pv_layout.addWidget(self.pv_fv_input, 0, 1)
        pv_layout.addWidget(QLabel("Ставка (%):"), 1, 0)
        pv_layout.addWidget(self.pv_rate_input, 1, 1)
        pv_layout.addWidget(QLabel("Количество периодов:"), 2, 0)
        pv_layout.addWidget(self.pv_periods_input, 2, 1)
        pv_layout.addWidget(pv_calc_button, 3, 0)
        pv_layout.addWidget(self.pv_result, 3, 1)
        
        pv_group.setLayout(pv_layout)
        
        # Группа для FV (Future Value)
        fv_group = QGroupBox("Расчет будущей стоимости (FV)")
        fv_layout = QGridLayout()
        
        self.fv_pv_input = QLineEdit()
        self.fv_rate_input = QLineEdit()
        self.fv_periods_input = QLineEdit()
        self.fv_result = QLineEdit()
        self.fv_result.setReadOnly(True)
        
        fv_calc_button = QPushButton("Рассчитать FV")
        fv_calc_button.clicked.connect(self.calculate_fv)
        
        fv_layout.addWidget(QLabel("Текущая стоимость (PV):"), 0, 0)
        fv_layout.addWidget(self.fv_pv_input, 0, 1)
        fv_layout.addWidget(QLabel("Ставка (%):"), 1, 0)
        fv_layout.addWidget(self.fv_rate_input, 1, 1)
        fv_layout.addWidget(QLabel("Количество периодов:"), 2, 0)
        fv_layout.addWidget(self.fv_periods_input, 2, 1)
        fv_layout.addWidget(fv_calc_button, 3, 0)
        fv_layout.addWidget(self.fv_result, 3, 1)
        
        fv_group.setLayout(fv_layout)
        
        # Группа для NPV (Net Present Value)
        npv_group = QGroupBox("Расчет чистой приведенной стоимости (NPV)")
        npv_layout = QGridLayout()
        
        self.npv_investment_input = QLineEdit()
        self.npv_flows_input = QLineEdit()
        self.npv_rate_input = QLineEdit()
        self.npv_result = QLineEdit()
        self.npv_result.setReadOnly(True)
        
        npv_calc_button = QPushButton("Рассчитать NPV")
        npv_calc_button.clicked.connect(self.calculate_npv)
        
        npv_layout.addWidget(QLabel("Начальные инвестиции:"), 0, 0)
        npv_layout.addWidget(self.npv_investment_input, 0, 1)
        npv_layout.addWidget(QLabel("Денежные потоки (через запятую):"), 1, 0)
        npv_layout.addWidget(self.npv_flows_input, 1, 1)
        npv_layout.addWidget(QLabel("Ставка (%):"), 2, 0)
        npv_layout.addWidget(self.npv_rate_input, 2, 1)
        npv_layout.addWidget(npv_calc_button, 3, 0)
        npv_layout.addWidget(self.npv_result, 3, 1)
        
        npv_group.setLayout(npv_layout)
        
        # Группа для IRR (Internal Rate of Return)
        irr_group = QGroupBox("Расчет внутренней нормы доходности (IRR)")
        irr_layout = QGridLayout()
        
        self.irr_flows_input = QLineEdit()
        self.irr_result = QLineEdit()
        self.irr_result.setReadOnly(True)
        
        irr_calc_button = QPushButton("Рассчитать IRR")
        irr_calc_button.clicked.connect(self.calculate_irr)
        
        irr_layout.addWidget(QLabel("Денежные потоки (через запятую):"), 0, 0)
        irr_layout.addWidget(self.irr_flows_input, 0, 1)
        irr_layout.addWidget(irr_calc_button, 1, 0)
        irr_layout.addWidget(self.irr_result, 1, 1)
        
        irr_group.setLayout(irr_layout)
        
        # Добавляем все группы в основной layout
        layout.addWidget(pv_group)
        layout.addWidget(fv_group)
        layout.addWidget(npv_group)
        layout.addWidget(irr_group)
        
        tab.setLayout(layout)
        return tab

    # Добавьте следующие методы в класс MainWindow

    def calculate_pv(self):
        try:
            fv = float(self.pv_fv_input.text())
            rate = float(self.pv_rate_input.text()) / 100
            periods = float(self.pv_periods_input.text())
            
            result = self.financial_calculator.calculate_pv(fv, rate, periods)
            self.pv_result.setText(f"{result:.2f}")
        except Exception as e:
            self.pv_result.setText(f"Ошибка: {str(e)}")

    def calculate_fv(self):
        try:
            pv = float(self.fv_pv_input.text())
            rate = float(self.fv_rate_input.text()) / 100
            periods = float(self.fv_periods_input.text())
            
            result = self.financial_calculator.calculate_fv(pv, rate, periods)
            self.fv_result.setText(f"{result:.2f}")
        except Exception as e:
            self.fv_result.setText(f"Ошибка: {str(e)}")

    def calculate_npv(self):
        try:
            investment = float(self.npv_investment_input.text())
            flows = [float(x.strip()) for x in self.npv_flows_input.text().split(',')]
            rate = float(self.npv_rate_input.text()) / 100
            
            result = self.financial_calculator.calculate_npv(investment, flows, rate)
            self.npv_result.setText(f"{result:.2f}")
        except Exception as e:
            self.npv_result.setText(f"Ошибка: {str(e)}")

    def calculate_irr(self):
        try:
            flows = [float(x.strip()) for x in self.irr_flows_input.text().split(',')]
            result = self.financial_calculator.calculate_irr(flows)
            self.irr_result.setText(f"{result * 100:.2f}%")
        except Exception as e:
            self.irr_result.setText(f"Ошибка: {str(e)}")

    def create_graph_calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Верхняя панель с вводом функции и кнопками
        top_panel = QHBoxLayout()
        
        # Поле ввода функции
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Введите функцию (например: x**2)")
        top_panel.addWidget(self.function_input)
        
        # Кнопки управления
        plot_button = QPushButton("Построить график")
        plot_button.clicked.connect(self.plot_graph)
        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.clear_graph)
        top_panel.addWidget(plot_button)
        top_panel.addWidget(clear_button)
        
        layout.addLayout(top_panel)
        
        # Панель настроек диапазона
        range_panel = QHBoxLayout()
        range_panel.addWidget(QLabel("X от:"))
        self.x_min = QSpinBox()
        self.x_min.setRange(-1000, 1000)
        self.x_min.setValue(-10)
        range_panel.addWidget(self.x_min)
        
        range_panel.addWidget(QLabel("до:"))
        self.x_max = QSpinBox()
        self.x_max.setRange(-1000, 1000)
        self.x_max.setValue(10)
        range_panel.addWidget(self.x_max)
        
        range_panel.addWidget(QLabel("Y от:"))
        self.y_min = QSpinBox()
        self.y_min.setRange(-1000, 1000)
        self.y_min.setValue(-10)
        range_panel.addWidget(self.y_min)
        
        range_panel.addWidget(QLabel("до:"))
        self.y_max = QSpinBox()
        self.y_max.setRange(-1000, 1000)
        self.y_max.setValue(10)
        range_panel.addWidget(self.y_max)
        
        apply_range = QPushButton("Применить диапазон")
        apply_range.clicked.connect(self.apply_graph_range)
        range_panel.addWidget(apply_range)
        
        layout.addLayout(range_panel)
        
        # Добавляем холст для графика
        self.graph_canvas = self.graph_calculator.get_canvas()
        layout.addWidget(self.graph_canvas)
        
        tab.setLayout(layout)
        return tab

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

    def create_accounting_calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Создаем вкладки для разных типов расчетов
        sub_tabs = QTabWidget()
        
        # Вкладка расчета амортизации
        depreciation_tab = QWidget()
        depreciation_layout = QFormLayout()
        
        self.initial_cost = QLineEdit()
        self.salvage_value = QLineEdit()
        self.useful_life = QSpinBox()
        self.useful_life.setRange(1, 50)
        self.depreciation_method = QComboBox()
        self.depreciation_method.addItems(['Линейный метод', 'Ускоренный метод'])
        
        depreciation_layout.addRow("Начальная стоимость:", self.initial_cost)
        depreciation_layout.addRow("Ликвидационная стоимость:", self.salvage_value)
        depreciation_layout.addRow("Срок использования (лет):", self.useful_life)
        depreciation_layout.addRow("Метод амортизации:", self.depreciation_method)
        
        calculate_depreciation_btn = QPushButton("Рассчитать амортизацию")
        calculate_depreciation_btn.clicked.connect(self.calculate_depreciation)
        depreciation_layout.addRow(calculate_depreciation_btn)
        
        self.depreciation_result = QTextEdit()
        self.depreciation_result.setReadOnly(True)
        depreciation_layout.addRow("Результат:", self.depreciation_result)
        
        depreciation_tab.setLayout(depreciation_layout)
        
        # Вкладка расчета кредита
        loan_tab = QWidget()
        loan_layout = QFormLayout()
        
        self.loan_amount = QLineEdit()
        self.loan_rate = QDoubleSpinBox()
        self.loan_rate.setRange(0.1, 100)
        self.loan_years = QSpinBox()
        self.loan_years.setRange(1, 30)
        
        loan_layout.addRow("Сумма кредита:", self.loan_amount)
        loan_layout.addRow("Годовая ставка (%):", self.loan_rate)
        loan_layout.addRow("Срок (лет):", self.loan_years)
        
        calculate_loan_btn = QPushButton("Рассчитать график платежей")
        calculate_loan_btn.clicked.connect(self.calculate_loan)
        loan_layout.addRow(calculate_loan_btn)
        
        self.loan_result = QTextEdit()
        self.loan_result.setReadOnly(True)
        loan_layout.addRow("График платежей:", self.loan_result)
        
        loan_tab.setLayout(loan_layout)
        
        # Вкладка расчета НДС
        vat_tab = QWidget()
        vat_layout = QFormLayout()
        
        self.vat_amount = QLineEdit()
        self.vat_rate = QDoubleSpinBox()
        self.vat_rate.setRange(0, 20)
        self.vat_rate.setValue(20)
        
        vat_layout.addRow("Сумма без НДС:", self.vat_amount)
        vat_layout.addRow("Ставка НДС (%):", self.vat_rate)
        
        calculate_vat_btn = QPushButton("Рассчитать НДС")
        calculate_vat_btn.clicked.connect(self.calculate_vat)
        vat_layout.addRow(calculate_vat_btn)
        
        self.vat_result = QTextEdit()
        self.vat_result.setReadOnly(True)
        vat_layout.addRow("Результат:", self.vat_result)
        
        vat_tab.setLayout(vat_layout)
        
        # Добавляем вкладки
        sub_tabs.addTab(depreciation_tab, "Амортизация")
        sub_tabs.addTab(loan_tab, "Кредит")
        sub_tabs.addTab(vat_tab, "НДС")
        
        layout.addWidget(sub_tabs)
        tab.setLayout(layout)
        
        return tab

    def calculate_depreciation(self):
        try:
            initial_cost = float(self.initial_cost.text())
            salvage_value = float(self.salvage_value.text())
            useful_life = self.useful_life.value()
            method = 'straight' if self.depreciation_method.currentText() == 'Линейный метод' else 'declining'
            
            result = self.accounting_calculator.calculate_depreciation(
                initial_cost, salvage_value, useful_life, method
            )
            
            if isinstance(result, dict):
                text = "Расчет амортизации:\n\n"
                for year, values in result.items():
                    text += f"Год {year}:\n"
                    text += f"Амортизация: {values['depreciation']:,.2f}\n"
                    text += f"Остаточная стоимость: {values['book_value']:,.2f}\n\n"
                self.depreciation_result.setText(text)
            else:
                self.depreciation_result.setText(str(result))
                
        except ValueError:
            self.depreciation_result.setText("Ошибка: Проверьте правильность введенных данных")

    def calculate_loan(self):
        try:
            amount = float(self.loan_amount.text())
            rate = self.loan_rate.value()
            years = self.loan_years.value()
            
            result = self.accounting_calculator.calculate_loan_amortization(amount, rate, years)
            
            if isinstance(result, dict):
                text = "График платежей:\n\n"
                for period, values in result.items():
                    text += f"Платеж {period}:\n"
                    text += f"Сумма платежа: {values['payment']:,.2f}\n"
                    text += f"Основной долг: {values['principal']:,.2f}\n"
                    text += f"Проценты: {values['interest']:,.2f}\n"
                    text += f"Остаток долга: {values['balance']:,.2f}\n\n"
                self.loan_result.setText(text)
            else:
                self.loan_result.setText(str(result))
                
        except ValueError:
            self.loan_result.setText("Ошибка: Проверьте правильность введенных данных")

    def calculate_vat(self):
        try:
            amount = float(self.vat_amount.text())
            rate = self.vat_rate.value()
            
            result = self.accounting_calculator.calculate_vat(amount, rate)
            
            if isinstance(result, dict):
                text = "Расчет НДС:\n\n"
                text += f"Сумма без НДС: {result['amount']:,.2f}\n"
                text += f"НДС: {result['vat']:,.2f}\n"
                text += f"Итого с НДС: {result['total']:,.2f}"
                self.vat_result.setText(text)
            else:
                self.vat_result.setText(str(result))
                
        except ValueError:
            self.vat_result.setText("Ошибка: Проверьте правильность введенных данных")

    def create_programmable_calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Создаём виджеты для определения функций
        function_group = QGroupBox("Определение функции")
        function_layout = QGridLayout()
        
        self.func_name_input = QLineEdit()
        self.func_name_input.setPlaceholderText("Имя функции")
        self.func_params_input = QLineEdit()
        self.func_params_input.setPlaceholderText("Параметры (через пробел)")
        self.func_expression_input = QLineEdit()
        self.func_expression_input.setPlaceholderText("Выражение")
        
        define_button = QPushButton("Определить функцию")
        define_button.clicked.connect(self.define_new_function)
        
        function_layout.addWidget(QLabel("Имя:"), 0, 0)
        function_layout.addWidget(self.func_name_input, 0, 1)
        function_layout.addWidget(QLabel("Параметры:"), 1, 0)
        function_layout.addWidget(self.func_params_input, 1, 1)
        function_layout.addWidget(QLabel("Выражение:"), 2, 0)
        function_layout.addWidget(self.func_expression_input, 2, 1)
        function_layout.addWidget(define_button, 3, 0, 1, 2)
        
        function_group.setLayout(function_layout)
        
        # Создаём виджеты для вызова функций
        call_group = QGroupBox("Вызов функции")
        call_layout = QGridLayout()
        
        self.call_name_input = QLineEdit()
        self.call_name_input.setPlaceholderText("Имя функции")
        self.call_args_input = QLineEdit()
        self.call_args_input.setPlaceholderText("Аргументы (через пробел)")
        
        call_button = QPushButton("Вызвать функцию")
        call_button.clicked.connect(self.call_existing_function)
        
        self.call_result = QLineEdit()
        self.call_result.setReadOnly(True)
        
        call_layout.addWidget(QLabel("Функция:"), 0, 0)
        call_layout.addWidget(self.call_name_input, 0, 1)
        call_layout.addWidget(QLabel("Аргументы:"), 1, 0)
        call_layout.addWidget(self.call_args_input, 1, 1)
        call_layout.addWidget(call_button, 2, 0)
        call_layout.addWidget(self.call_result, 2, 1)
        
        call_group.setLayout(call_layout)
        
        # Создаём виджеты для работы с переменными
        var_group = QGroupBox("Переменные")
        var_layout = QGridLayout()
        
        self.var_name_input = QLineEdit()
        self.var_name_input.setPlaceholderText("Имя переменной")
        self.var_value_input = QLineEdit()
        self.var_value_input.setPlaceholderText("Значение")
        
        set_var_button = QPushButton("Установить")
        set_var_button.clicked.connect(self.set_variable)
        
        var_layout.addWidget(QLabel("Переменная:"), 0, 0)
        var_layout.addWidget(self.var_name_input, 0, 1)
        var_layout.addWidget(QLabel("Значение:"), 1, 0)
        var_layout.addWidget(self.var_value_input, 1, 1)
        var_layout.addWidget(set_var_button, 2, 0, 1, 2)
        
        var_group.setLayout(var_layout)
        
        # Добавляем список функций и переменных
        self.functions_list = QTextEdit()
        self.functions_list.setReadOnly(True)
        update_lists_button = QPushButton("Обновить списки")
        update_lists_button.clicked.connect(self.update_function_lists)
        
        # Собираем всё вместе
        layout.addWidget(function_group)
        layout.addWidget(call_group)
        layout.addWidget(var_group)
        layout.addWidget(update_lists_button)
        layout.addWidget(self.functions_list)
        
        tab.setLayout(layout)
        return tab

    def define_new_function(self):
        name = self.func_name_input.text().strip()
        params = self.func_params_input.text().strip().split()
        expression = self.func_expression_input.text().strip()
        
        success, message = self.programmable_calculator.define_function(name, params, expression)
        if success:
            self.update_function_lists()
            QMessageBox.information(self, "Успех", message)
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def call_existing_function(self):
        name = self.call_name_input.text().strip()
        args = [float(arg) for arg in self.call_args_input.text().strip().split()]
        
        success, result = self.programmable_calculator.call_function(name, args)
        if success:
            self.call_result.setText(str(result))
        else:
            self.call_result.setText(str(result))
            QMessageBox.warning(self, "Ошибка", str(result))

    def set_variable(self):
        name = self.var_name_input.text().strip()
        value = self.var_value_input.text().strip()
        
        success, message = self.programmable_calculator.set_variable(name, value)
        if success:
            self.update_function_lists()
            QMessageBox.information(self, "Успех", message)
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def update_function_lists(self):
        functions = self.programmable_calculator.list_functions()
        variables = self.programmable_calculator.list_variables()
        
        text = "Определённые функции:\n"
        text += "\n".join(functions)
        text += "\n\nПеременные:\n"
        text += "\n".join(variables)
        
        self.functions_list.setText(text)

    def create_currency_calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Группа для ввода суммы и выбора валют
        input_group = QGroupBox("Конвертация валют")
        input_layout = QGridLayout()

        # Поле для ввода суммы
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Введите сумму")
        
        # Выпадающие списки для выбора валют
        self.from_currency = QComboBox()
        self.to_currency = QComboBox()
        
        # Заполняем списки доступными валютами
        currencies = self.currency_calculator.get_available_currencies()
        self.from_currency.addItems(currencies)
        self.to_currency.addItems(currencies)
        
        # Поле для вывода результата
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        
        # Кнопка конвертации
        convert_button = QPushButton("Конвертировать")
        convert_button.clicked.connect(self.perform_currency_conversion)
        
        # Добавляем виджеты в layout
        input_layout.addWidget(QLabel("Сумма:"), 0, 0)
        input_layout.addWidget(self.amount_input, 0, 1)
        input_layout.addWidget(QLabel("Из валюты:"), 1, 0)
        input_layout.addWidget(self.from_currency, 1, 1)
        input_layout.addWidget(QLabel("В валюту:"), 2, 0)
        input_layout.addWidget(self.to_currency, 2, 1)
        input_layout.addWidget(convert_button, 3, 0, 1, 2)
        input_layout.addWidget(QLabel("Результат:"), 4, 0)
        input_layout.addWidget(self.result_display, 4, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Кнопка обновления курсов
        update_rates_button = QPushButton("Обновить курсы валют")
        update_rates_button.clicked.connect(self.update_currency_rates)
        layout.addWidget(update_rates_button)
        
        # Добавляем растягивающийся пробел
        layout.addStretch()
        
        tab.setLayout(layout)
        return tab

    def perform_currency_conversion(self):
        try:
            amount = float(self.amount_input.text())
            from_curr = self.from_currency.currentText()
            to_curr = self.to_currency.currentText()
            
            result = self.currency_calculator.convert_currency(amount, from_curr, to_curr)
            
            if isinstance(result, float):
                formatted_result = self.currency_calculator.format_currency(result, to_curr)
                self.result_display.setText(formatted_result)
            else:
                self.result_display.setText(str(result))
                
        except ValueError:
            self.result_display.setText("Ошибка: Введите корректное число")
        except Exception as e:
            self.result_display.setText(f"Ошибка: {str(e)}")

    def update_currency_rates(self):
        result = self.currency_calculator.update_exchange_rates()
        if result:
            QMessageBox.warning(self, "Ошибка", result)
        else:
            QMessageBox.information(self, "Успех", "Курсы валют успешно обновлены")

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
                    input_line.setText(str(result))
                else:
                    result = sp.sympify(expression)
                    result_float = result.evalf()
                    
                    # Проверяем, является ли результат целым числом
                    if result.is_integer:
                        input_line.setText(str(int(result_float)))
                    else:
                        # Для дробных чисел убираем лишние нули после запятой
                        input_line.setText(f"{result_float:.10f}".rstrip('0').rstrip('.'))
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
            Qt.Key.Key_I: '∫', Qt.Key.Key_D: 'd/dx', Qt.Key.Key_X: 'x', Qt.Key.Key_Z: 'sinh',
            Qt.Key.Key_V: 'cosh', Qt.Key.Key_B: 'tanh', Qt.Key.Key_N: 'abs', Qt.Key.Key_Alt: '!'
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