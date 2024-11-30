from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QGroupBox, QGridLayout, QPushButton, QLabel


class Programmable_tab:
    def programmable_calculator_tab(self):
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