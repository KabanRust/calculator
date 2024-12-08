from PySide6.QtWidgets import QWidget
import json
with open("constants.json", "r") as file:
    constants = json.load(file)

FINANCIAL_FUNCTIONS = constants["FINANCIAL_FUNCTIONS"]


class FinancialCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.functions = FINANCIAL_FUNCTIONS
    
    def calculate_pv(self, fv, rate, periods):
        try:
            return fv / ((1 + rate) ** periods)
        except Exception as e:
            return f"Ошибка в расчете PV: {e}"

    def calculate_fv(self, pv, rate, periods):
        try:
            return pv * ((1 + rate) ** periods)
        except Exception as e:
            return f"Ошибка в расчете FV: {e}"

    def calculate_npv(self, initial_investment, cash_flows, rate):
        try:
            npv = initial_investment
            for t, cf in enumerate(cash_flows, 1):
                npv += cf / ((1 + rate) ** t)
            return npv
        except Exception as e:
            return f"Ошибка в расчете NPV: {e}"

    def calculate_irr(self, cash_flows, guess=0.1, tolerance=0.0001, max_iterations=100):
        try:
            if not cash_flows or len(cash_flows) < 2:
                raise ValueError("Требуется как минимум два денежных потока")
            
            rate = guess
            for i in range(max_iterations):
                npv = sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
                if abs(npv) < tolerance:
                    return rate
                
                dnpv = sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cash_flows))
                
                new_rate = rate - npv / dnpv
                
                if abs(new_rate - rate) < tolerance:
                    return new_rate
                
                rate = new_rate
            
            return rate
        
        except Exception as e:
            raise ValueError(f"Ошибка в расчете IRR: {e}")