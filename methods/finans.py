class Finans_methods:
    def calculate_pv(self):
        try:
            fv = float(self.pv_fv_input.text())
            rate = float(self.pv_rate_input.text()) / 100
            periods = float(self.pv_periods_input.text())
            
            result = self.financial_calculator.calculate_pv(fv, rate, periods)
            self.pv_result.setText(f"{result:.2f}")
        except Exception as e:
            self.pv_result.setText(f"Ошибка: {str(e)}")

    def calculate_fv(self):
        try:
            pv = float(self.fv_pv_input.text())
            rate = float(self.fv_rate_input.text()) / 100
            periods = float(self.fv_periods_input.text())
            
            result = self.financial_calculator.calculate_fv(pv, rate, periods)
            self.fv_result.setText(f"{result:.2f}")
        except Exception as e:
            self.fv_result.setText(f"Ошибка: {str(e)}")

    def calculate_npv(self):
        try:
            investment = float(self.npv_investment_input.text())
            flows = [float(x.strip()) for x in self.npv_flows_input.text().split(',')]
            rate = float(self.npv_rate_input.text()) / 100
            
            result = self.financial_calculator.calculate_npv(investment, flows, rate)
            self.npv_result.setText(f"{result:.2f}")
        except Exception as e:
            self.npv_result.setText(f"Ошибка: {str(e)}")

    def calculate_irr(self):
        try:
            flows = [float(x.strip()) for x in self.irr_flows_input.text().split(',')]
            result = self.financial_calculator.calculate_irr(flows)
            self.irr_result.setText(f"{result * 100:.2f}%")
        except Exception as e:
            self.irr_result.setText(f"Ошибка: {str(e)}")