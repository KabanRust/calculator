class Accounting_func:
    def calculate_depreciation(self):
        try:
            initial_cost = float(self.initial_cost.text())
            salvage_value = float(self.salvage_value.text())
            useful_life = self.useful_life.value()
            method = 'straight' if self.depreciation_method.currentText() == 'Линейный метод' else 'declining'
            
            result = self.accounting_calculator.calculate_depreciation(
                initial_cost, salvage_value, useful_life, method
            )
            
            if isinstance(result, dict):
                text = "Расчет амортизации:\n\n"
                for year, values in result.items():
                    text += f"Год {year}:\n"
                    text += f"Амортизация: {values['depreciation']:,.2f}\n"
                    text += f"Остаточная стоимость: {values['book_value']:,.2f}\n\n"
                self.depreciation_result.setText(text)
            else:
                self.depreciation_result.setText(str(result))
                
        except ValueError:
            self.depreciation_result.setText("Ошибка: Проверьте правильность введенных данных")

    def calculate_loan(self):
        try:
            amount = float(self.loan_amount.text())
            rate = self.loan_rate.value()
            years = self.loan_years.value()
            
            result = self.accounting_calculator.calculate_loan_amortization(amount, rate, years)
            
            if isinstance(result, dict):
                text = "График платежей:\n\n"
                for period, values in result.items():
                    text += f"Платеж {period}:\n"
                    text += f"Сумма платежа: {values['payment']:,.2f}\n"
                    text += f"Основной долг: {values['principal']:,.2f}\n"
                    text += f"Проценты: {values['interest']:,.2f}\n"
                    text += f"Остаток долга: {values['balance']:,.2f}\n\n"
                self.loan_result.setText(text)
            else:
                self.loan_result.setText(str(result))
                
        except ValueError:
            self.loan_result.setText("Ошибка: Проверьте правильность введенных данных")

    def calculate_vat(self):
        try:
            amount = float(self.vat_amount.text())
            rate = self.vat_rate.value()
            
            result = self.accounting_calculator.calculate_vat(amount, rate)
            
            if isinstance(result, dict):
                text = "Расчет НДС:\n\n"
                text += f"Сумма без НДС: {result['amount']:,.2f}\n"
                text += f"НДС: {result['vat']:,.2f}\n"
                text += f"Итого с НДС: {result['total']:,.2f}"
                self.vat_result.setText(text)
            else:
                self.vat_result.setText(str(result))
                
        except ValueError:
            self.vat_result.setText("Ошибка: Проверьте правильность введенных данных")