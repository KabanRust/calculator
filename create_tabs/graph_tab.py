from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QHBoxLayout, QLabel, QPushButton, QGridLayout, QLineEdit

class Graph_tab:
    def graph_calculator_tab(self):
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