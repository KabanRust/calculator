class Number_func:
    def convert_number(self):
        number = self.number_input.text()
        from_base = self.from_base_combo.currentData()
        to_base = self.to_base_combo.currentData()
        
        # Проверяем валидность введенного числа
        if not self.number_calculator.validate_number(number, from_base):
            self.result_display.setText("Ошибка: Неверный формат числа")
            return
            
        result = self.number_calculator.convert_number(number, from_base, to_base)
        self.result_display.setText(result)

    def on_number_button_click(self, text):
        current_text = self.number_input.text()
        self.number_input.setText(current_text + text)

    def clear_number_input(self):
        self.number_input.clear()
        self.result_display.clear()