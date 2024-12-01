from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel, QSpinBox, QMessageBox, QGroupBox, QTextEdit, QComboBox, QFormLayout, QDoubleSpinBox
from PySide6.QtCore import Qt
from sympy import sympify
import sympy as sp
from constants import SIMPLE_OPERATORS, SIMPLE_FUNCTIONS, ENGINEERING_OPERATORS, ENGINEERING_FUNCTIONS, FINANCIAL_FUNCTIONS, ACCOUNTING_FUNCTIONS, GRAPHING_FUNCTIONS, CURRENCY_SYMBOLS, PROGRAMMABLE_FUNCTIONS, BASES
import modules
from methods import Buttons, Currency, Matrix_perform, Matrix_size

class Matrix_interface:

    def set_matrix_size(self):
        self.matrix_size = Matrix_size
        return self.matrix_size.local_matrix_size

    def get_matrix(self, matrix_layout):
        return self.matrix_size.local_get_matrix
    
    def Matrix_perform(self):
        return self.perform

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


class Create_tab(Matrix_interface):
    def __init__(self):
        super().__init__()


    class foundation:
        def __init__(self):
            self.currency = Currency

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
                    # Use a lambda that correctly passes the button text
                    button.clicked.connect(lambda checked, text=button_text: 
                                           self.currency.make_button_callback(text)(self.input_line))
                    row_layout.addWidget(button)
                button_layout.addLayout(row_layout)

            layout.addLayout(button_layout)
            tab.setLayout(layout)

            return tab

        def create_simple_calculator_tab(self):
            return self.create_calculator_tab(SIMPLE_OPERATORS, SIMPLE_FUNCTIONS)

        def create_engineering_calculator_tab(self):
            return self.create_calculator_tab(ENGINEERING_OPERATORS, ENGINEERING_FUNCTIONS, include_extra_buttons=True)
        

    class matrix(foundation):
        def __init__(self):
            super().__init__()
            self.perform = Matrix_perform
            self.set_size = Matrix_size
        
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
            self.set_size_button.clicked.connect(self.set_size.local_matrix_size)
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

            self.add_button = QPushButton('Cложение')
            self.add_button.clicked.connect(self.perform.perform_add)
            buttons_layout.addWidget(self.add_button)

            self.subtract_button = QPushButton('Вычитание')
            self.subtract_button.clicked.connect(self.perform.perform_subtract)
            buttons_layout.addWidget(self.subtract_button)

            self.multiply_button = QPushButton('Умножение')
            self.multiply_button.clicked.connect(self.perform.perform_multiply)
            buttons_layout.addWidget(self.multiply_button)

            self.transpose_button = QPushButton('Транспонирование')
            self.transpose_button.clicked.connect(self.perform.perform_transpose)
            buttons_layout.addWidget(self.transpose_button)

            self.determinant_button = QPushButton('Детерминант')
            self.determinant_button.clicked.connect(self.perform.perform_determinant)
            buttons_layout.addWidget(self.determinant_button)

            self.inverse_button = QPushButton('Инверсия')
            self.inverse_button.clicked.connect(self.perform.perform_inverse)
            buttons_layout.addWidget(self.inverse_button)

            layout.addLayout(buttons_layout)
            tab.setLayout(layout)

            return tab
    

    class finans(foundation):
        def __init__(self):
            super().__init__()
            self.local_finans_method()  # Добавлено

        def local_finans_method(self):
            from methods import Finans_methods
            
            self.call_pv = Finans_methods()

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
            pv_calc_button.clicked.connect(self.call_pv.calculate_pv)
            
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
            fv_calc_button.clicked.connect(self.call_pv.calculate_fv)
            
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
            npv_calc_button.clicked.connect(self.call_pv.calculate_npv)
            
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
            irr_calc_button.clicked.connect(self.call_pv.calculate_irr)
            
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


    class graph(foundation):
        def __init__(self):
            super().__init__()
            self.local_graph_method()  # Добавлено

        def local_graph_method(self):
            from methods import Graph_methods
            from modules import GraphCalculator
            self.graph = GraphCalculator
            self.plot = Graph_methods

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
            plot_button.clicked.connect(self.plot.plot_graph)
            clear_button = QPushButton("Очистить")
            clear_button.clicked.connect(self.plot.clear_graph)
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
            apply_range.clicked.connect(self.plot.apply_graph_range)
            range_panel.addWidget(apply_range)
            
            layout.addLayout(range_panel)
            
            # Добавляем холст для графика
            self.graph_calculator = self.graph()
            self.graph_canvas = self.graph_calculator.get_canvas()
            layout.addWidget(self.graph_canvas)
            
            tab.setLayout(layout)
            return tab


    class number(foundation):
        def __init__(self):
            super().__init__()
            self.local_number_method()

        def local_number_method(self):
            from methods import Number_func
            self.number = Number_func

        def create_number_calculator_tab(self):
            tab = QWidget()
            layout = QVBoxLayout()
            
            # Создаем группу для ввода числа и выбора исходной системы счисления
            input_layout = QHBoxLayout()
            self.number_input = QLineEdit()
            self.number_input.setPlaceholderText("Введите число")
            
            self.from_base_combo = QComboBox()
            for base_name, base in BASES.items():
                self.from_base_combo.addItem(base_name, base)
            
            input_layout.addWidget(QLabel("Число:"))
            input_layout.addWidget(self.number_input)
            input_layout.addWidget(QLabel("Из:"))
            input_layout.addWidget(self.from_base_combo)
            
            # Создаем группу для выбора целевой системы счисления и результата
            output_layout = QHBoxLayout()
            self.to_base_combo = QComboBox()
            for base_name, base in BASES.items():
                self.to_base_combo.addItem(base_name, base)
            
            self.result_display = QLineEdit()
            self.result_display.setReadOnly(True)
            
            output_layout.addWidget(QLabel("В:"))
            output_layout.addWidget(self.to_base_combo)
            output_layout.addWidget(QLabel("Результат:"))
            output_layout.addWidget(self.result_display)
            
            # Кнопка конвертации
            convert_button = QPushButton("Конвертировать")
            convert_button.clicked.connect(self.number.convert_number)
            
            # Добавляем все элементы на вкладку
            layout.addLayout(input_layout)
            layout.addLayout(output_layout)
            layout.addWidget(convert_button)
            
            # Добавляем сетку кнопок для ввода чисел
            button_grid = QGridLayout()
            buttons = [
                ['7', '8', '9', 'A'],
                ['4', '5', '6', 'B'],
                ['1', '2', '3', 'C'],
                ['0', 'D', 'E', 'F']
            ]
            
            for i, row in enumerate(buttons):
                for j, text in enumerate(row):
                    button = QPushButton(text)
                    button.clicked.connect(lambda checked, t=text: self.number.on_number_button_click(t))
                    button_grid.addWidget(button, i, j)
            
            layout.addLayout(button_grid)
            
            # Добавляем кнопку очистки
            clear_button = QPushButton("Очистить")
            clear_button.clicked.connect(self.number.clear_number_input)
            layout.addWidget(clear_button)
            
            tab.setLayout(layout)
            return tab


    class account(foundation):
        def __init__(self):
            super().__init__()
            self.local_accounting_method()

        def local_accounting_method(self):
            from methods import Accounting_func
            self.acc = Accounting_func

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
            calculate_depreciation_btn.clicked.connect(self.acc.calculate_depreciation)
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
            calculate_loan_btn.clicked.connect(self.acc.calculate_loan)
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
            calculate_vat_btn.clicked.connect(self.acc.calculate_vat)
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


    class programm(foundation):
        def __init__(self):
            super().__init__()
            self.local_programmable_method()

        def local_programmable_method(self):
            from methods import Programmable_func
            self.mix = Programmable_func

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
            define_button.clicked.connect(self.mix.define_new_function)
            
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
            call_button.clicked.connect(self.mix.call_existing_function)
            
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
            set_var_button.clicked.connect(self.mix.set_variable)
            
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
            update_lists_button.clicked.connect(self.mix.update_function_lists)
            
            # Собираем всё вместе
            layout.addWidget(function_group)
            layout.addWidget(call_group)
            layout.addWidget(var_group)
            layout.addWidget(update_lists_button)
            layout.addWidget(self.functions_list)
            
            tab.setLayout(layout)
            return tab


    class currency(foundation):
        def __init__(self):
            super().__init__()
            self.local_currency_method()

        def local_currency_method(self):
            from methods import Currency
            from modules import CurrencyCalculator
            self.car = CurrencyCalculator
            self.cur = Currency

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
            currencies = self.car().get_available_currencies()  # Создаем экземпляр CurrencyCalculator
            self.from_currency.addItems(currencies)
            self.to_currency.addItems(currencies)
            
            # Поле для вывода результата
            self.result_display = QLineEdit()
            self.result_display.setReadOnly(True)
            
            # Кнопка конвертации
            convert_button = QPushButton("Конвертировать")
            convert_button.clicked.connect(self.cur.perform_currency_conversion)
            
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
            update_rates_button.clicked.connect(self.cur.update_currency_rates)
            layout.addWidget(update_rates_button)
            
            # Добавляем растягивающийся пробел
            layout.addStretch()
            
            tab.setLayout(layout)
            return tab
        

class Button:
    def __init__(self):
        self.hotkey = Buttons
    
    def hotkey_button(self):
        return self.hotkey
    

class MainWindow(QMainWindow, Create_tab):
    def __init__(self):
        QMainWindow.__init__(self)
        Create_tab.__init__(self)

        self.create_tab_instance = Create_tab()
        self.foundation_instance = self.create_tab_instance.foundation()
        self.matrix_instance = self.create_tab_instance.matrix()
        self.finans_instance = self.create_tab_instance.finans()
        self.graph_instance = self.create_tab_instance.graph()
        self.number_instance = self.create_tab_instance.number()
        self.accounting_instance = self.create_tab_instance.account()
        self.programmable_instance = self.create_tab_instance.programm()
        self.currency_instance = self.create_tab_instance.currency()

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
        self.tab_widget.addTab(self.foundation_instance.create_simple_calculator_tab(), "Простой калькулятор")
        self.tab_widget.addTab(self.foundation_instance.create_engineering_calculator_tab(), "Инженерный калькулятор")
        self.tab_widget.addTab(self.matrix_instance.create_matrix_calculator_tab(), "Матрицы")
        self.tab_widget.addTab(self.finans_instance.create_financial_calculator_tab(), "Финансовый калькулятор")
        self.tab_widget.addTab(self.graph_instance.create_graph_calculator_tab(), "Графики")
        self.tab_widget.addTab(self.number_instance.create_number_calculator_tab(), "Системы счисления")
        self.tab_widget.addTab(self.accounting_instance.create_accounting_calculator_tab(), "Бухгалтерия")
        self.tab_widget.addTab(self.programmable_instance.create_programmable_calculator_tab(), "Программируемый калькулятор")
        self.tab_widget.addTab(self.currency_instance.create_currency_calculator_tab(), "Валютный калькулятор")

        # По умолчанию, открываем первый калькулятор
        self.tab_widget.setCurrentIndex(0)