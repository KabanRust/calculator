from PySide6.QtWidgets import QWidget
import math
from constants import FINANCIAL_FUNCTIONS

class FinancialCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.functions = FINANCIAL_FUNCTIONS
    
    def calculate_pv(self, fv, rate, periods):
        """
        Расчет текущей стоимости (Present Value)
        fv: будущая стоимость
        rate: процентная ставка (в долях)
        periods: количество периодов
        """
        try:
            return fv / ((1 + rate) ** periods)
        except Exception as e:
            return f"Ошибка в расчете PV: {e}"

    def calculate_fv(self, pv, rate, periods):
        """
        Расчет будущей стоимости (Future Value)
        pv: текущая стоимость
        rate: процентная ставка (в долях)
        periods: количество периодов
        """
        try:
            return pv * ((1 + rate) ** periods)
        except Exception as e:
            return f"Ошибка в расчете FV: {e}"

    def calculate_npv(self, initial_investment, cash_flows, rate):
        """
        Расчет чистой приведенной стоимости (Net Present Value)
        initial_investment: начальные инвестиции (отрицательное число)
        cash_flows: список денежных потоков
        rate: процентная ставка (в долях)
        """
        try:
            npv = initial_investment
            for t, cf in enumerate(cash_flows, 1):
                npv += cf / ((1 + rate) ** t)
            return npv
        except Exception as e:
            return f"Ошибка в расчете NPV: {e}"

    def calculate_irr(self, cash_flows, guess=0.1, tolerance=0.0001, max_iterations=100):
        """
        Расчет внутренней нормы доходности (Internal Rate of Return)
        cash_flows: список денежных потоков (первый - начальные инвестиции)
        guess: начальное предположение для ставки
        tolerance: допустимая погрешность
        max_iterations: максимальное число итераций
        """
        try:
            rate = guess
            for i in range(max_iterations):
                npv = sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
                if abs(npv) < tolerance:
                    return rate
                
                # Производная NPV по ставке
                dnpv = sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cash_flows))
                
                # Метод Ньютона-Рафсона
                new_rate = rate - npv / dnpv
                
                if abs(new_rate - rate) < tolerance:
                    return new_rate
                
                rate = new_rate
            
            return rate
        except Exception as e:
            return f"Ошибка в расчете IRR: {e}"