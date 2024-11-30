from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QHBoxLayout, QLabel, QPushButton, QGridLayout, QLineEdit

class Matrix_tab:
    def __init__(self, matrix_size_instance):
        self.matrix_size_instance = matrix_size_instance  # Экземпляр класса Matrix_size
        self.matrices = []

    def matrix_calculator_tab(self):
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
        # Привязка метода set_matrix_size из Matrix_size
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

        self.add_button = QPushButton('Сложение')
        buttons_layout.addWidget(self.add_button)

        self.subtract_button = QPushButton('Вычитание')
        buttons_layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton('Умножение')
        buttons_layout.addWidget(self.multiply_button)

        self.transpose_button = QPushButton('Транспонирование')
        buttons_layout.addWidget(self.transpose_button)

        self.determinant_button = QPushButton('Детерминант')
        buttons_layout.addWidget(self.determinant_button)

        self.inverse_button = QPushButton('Инверсия')
        buttons_layout.addWidget(self.inverse_button)

        layout.addLayout(buttons_layout)
        tab.setLayout(layout)

        return tab

    def set_matrix_size(self):
        # Проксирование вызова к Matrix_size
        self.matrix_size_instance.rows_spinbox = self.rows_spinbox
        self.matrix_size_instance.cols_spinbox = self.cols_spinbox
        self.matrix_size_instance.matrices_count_spinbox = self.matrices_count_spinbox
        self.matrix_size_instance.matrix_layouts = self.matrix_layouts
        self.matrix_size_instance.set_matrix_size()
