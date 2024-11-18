from PySide6.QtWidgets import QWidget
from sympy import sympify
from constants import ACCOUNTING_FUNCTIONS

class AccountingCalculator(QWidget):
    def __init__(self):
        self.functions = ACCOUNTING_FUNCTIONS

        super().__init__()

    def evaluate(self, expression):
        try:
            result = sympify(expression).evalf()
            return float(result)
        except Exception as e:
            return f"Ошибка: {e}"
        
    def calculate_depreciation(self, initial_value, residual_value, years):
        try:
            depreciation = (float(initial_value) - float(residual_value)) / float(years)
            return depreciation
        except Exception as e:
            return f"Ошибка: {e}"
        
    def calculate_pv(self, future_value, rate, periods):
        """Метод для расчета настоящей стоимости (PV)"""
        try:
            rate = float(rate) / 100
            periods = int(periods)
            pv = float(future_value) / ((1 + rate) ** periods)
            return pv
        except Exception as e:
            return f"Ошибка: {e}"

    def calculate_fv(self, present_value, rate, periods):
        """Метод для расчета будущей стоимости (FV)"""
        try:
            rate = float(rate) / 100
            periods = int(periods)
            fv = float(present_value) * ((1 + rate) ** periods)
            return fv
        except Exception as e:
            return f"Ошибка: {e}"

    def calculate_irr(self, cashflows):
        """Метод для расчета IRR (внутренней нормы доходности)"""
        try:
            cashflows = [float(x) for x in cashflows]
            irr = sympify('irr(cashflows)')
            return irr
        except Exception as e:
            return f"Ошибка: {e}"

    def calculate_npv(self, rate, cashflows):
        """Метод для расчета NPV"""
        try:
            rate = float(rate) / 100
            cashflows = [float(x) for x in cashflows]
            npv = sum(cashflows[i] / ((1 + rate) ** i) for i in range(len(cashflows)))
            return npv
        except Exception as e:
            return f"Ошибка: {e}"
