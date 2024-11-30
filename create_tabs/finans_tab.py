from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel, QPushButton, QGridLayout, QLineEdit

class Finans_tab:
    def financial_tab(self):
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