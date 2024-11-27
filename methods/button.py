import sympy as sp

class Button:
    def percent(self, input_line):
        try:
            result = str(float(input_line.text()) / 100)
            input_line.setText(result)
        except ValueError:
            input_line.setText("Ошибка")
    
    def sumbols_but(self, input_line):
        expression = input_line.text()
        try:
            if expression.startswith('∫(') or expression.startswith('d/dx('):
                result = self.engineering_calculator.evaluate(expression)
                # Преобразуем символьный результат в строку
                input_line.setText(str(result))
            else:
                result = sp.sympify(expression).evalf()
                # Проверяем, является ли результат числом
                if isinstance(result, (float, int)):
                    if float(result).is_integer():
                        input_line.setText(str(int(result)))
                    else:
                        input_line.setText(f"{float(result):.10f}".rstrip('0').rstrip('.'))
                else:
                    input_line.setText(str(result))
        except Exception as e:
            input_line.setText(f"Ошибка: {e}")