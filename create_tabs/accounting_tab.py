from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QComboBox, QSpinBox, QPushButton, QFormLayout, QDoubleSpinBox, QTabWidget

class Accounting_tab:
    def accounting_calculator_tab(self):
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