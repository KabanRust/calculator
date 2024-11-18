from PySide6.QtWidgets import QWidget
from constants import BASES

class NumberCalculator(QWidget):
    def __init__(self):
        self.bases = BASES

        super().__init__()

    def convert(self, number: str, from_base: str, to_base: str):
        try:
            if from_base not in self.bases or to_base not in self.bases:
                raise ValueError("Неверно указана система счисления")
            
            decimal_value = int(number, self.bases[from_base])

            if to_base == 'BIN':
                return bin(decimal_value)[2:]
            elif to_base == 'OCT':
                return oct(decimal_value)[2:]
            elif to_base == 'DEC':
                return str(decimal_value)
            elif to_base == 'HEX':
                return hex(decimal_value)[2:].upper()
        except ValueError as ve:
            return f"Ошибка: {ve}"
        except Exception as e:
            return f"Ошибка: {e}"

    def is_valid_number(self, number: str, base: str):
        try:
            if base not in self.bases:
                raise ValueError("Неверно указана система счисления")
            int(number, self.bases[base])
            return True
        except ValueError:
            return False
