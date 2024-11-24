from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox
from constants import BASES

class NumberCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.bases = BASES
        
    def convert_number(self, number: str, from_base: int, to_base: int) -> str:
        """Конвертирует число из одной системы счисления в другую"""
        try:
            # Сначала преобразуем в десятичное число
            decimal = int(number, from_base)
            # Затем конвертируем в целевую систему счисления
            if to_base == 2:
                return bin(decimal)[2:]  # Убираем префикс '0b'
            elif to_base == 8:
                return oct(decimal)[2:]  # Убираем префикс '0o'
            elif to_base == 16:
                return hex(decimal)[2:].upper()  # Убираем префикс '0x'
            else:
                return str(decimal)
        except ValueError:
            return "Ошибка конвертации"
            
    def validate_number(self, number: str, base: int) -> bool:
        """Проверяет, является ли строка допустимым числом в заданной системе счисления"""
        try:
            int(number, base)
            return True
        except ValueError:
            return False