from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QLabel, QPushButton, QGridLayout
from constants import BASES

class Number_tab:
    def number_calculator_tab(self):
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
        convert_button.clicked.connect(self.convert_number)
        
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
                button.clicked.connect(lambda checked, t=text: self.on_number_button_click(t))
                button_grid.addWidget(button, i, j)
        
        layout.addLayout(button_grid)
        
        # Добавляем кнопку очистки
        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.clear_number_input)
        layout.addWidget(clear_button)
        
        tab.setLayout(layout)
        return tab