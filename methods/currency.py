from PySide6.QtWidgets import QMessageBox

class Currency:
    def perform_currency_conversion(self):
        try:
            amount = float(self.amount_input.text())
            from_curr = self.from_currency.currentText()
            to_curr = self.to_currency.currentText()
            
            result = self.currency_calculator.convert_currency(amount, from_curr, to_curr)
            
            if isinstance(result, float):
                formatted_result = self.currency_calculator.format_currency(result, to_curr)
                self.result_display.setText(formatted_result)
            else:
                self.result_display.setText(str(result))
                
        except ValueError:
            self.result_display.setText("Ошибка: Введите некорректное число")
        except Exception as e:
            self.result_display.setText(f"Ошибка: {str(e)}")

    def update_currency_rates(self):
        result = self.currency_calculator.update_exchange_rates()
        if result:
            QMessageBox.warning(self, "Ошибка", result)
        else:
            QMessageBox.information(self, "Успех", "Курсы валют успешно обновлены")

    def make_button_callback(self, text, input_line):
        def callback():
            self.on_button_click(text, input_line)
        return callback