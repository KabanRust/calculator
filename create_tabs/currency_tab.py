from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLineEdit, QGroupBox, QGridLayout, QPushButton, QLabel


class Currency_tab:
    def currency_calculator_tab(self):
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