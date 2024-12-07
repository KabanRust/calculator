from PySide6.QtWidgets import QWidget
from decimal import Decimal

class CurrencyCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.92,
            'GBP': 0.79,
            'JPY': 151.68,
            'KZT': 449.50
        }
        self.currency_symbols = {
            'USD': '$',
            'EUR': '€',
            'GBP': '£',
            'JPY': '¥',
            'KZT': '₸'
        }
        
    def convert_currency(self, amount, from_currency, to_currency):
        try:
            amount = Decimal(str(amount))
            
            # Если валюты одинаковые, возвращаем исходную сумму
            if from_currency == to_currency:
                return float(amount)
            
            # Конвертируем в USD как промежуточную валюту, если исходная валюта не USD
            if from_currency != 'USD':
                amount = amount / Decimal(str(self.exchange_rates[from_currency]))
            
            # Конвертируем из USD в целевую валюту, если целевая валюта не USD
            if to_currency != 'USD':
                amount = amount * Decimal(str(self.exchange_rates[to_currency]))
            
            return float(amount)
        except Exception as e:
            return f"Ошибка конвертации: {str(e)}"
    
    def update_exchange_rates(self):
        """
        Метод для обновления курсов валют.
        В реальном приложении здесь был бы API запрос к сервису курсов валют.
        """
        try:
            # Здесь можно добавить реальный API запрос
            # Например, используя API exchangerate-api.com или подобный сервис
            pass
        except Exception as e:
            return f"Ошибка обновления курсов: {str(e)}"

    def get_currency_symbol(self, currency_code):
        """Возвращает символ валюты по её коду"""
        return self.currency_symbols.get(currency_code, currency_code)

    def get_available_currencies(self):
        """Возвращает список доступных валют"""
        return list(self.exchange_rates.keys())

    def format_currency(self, amount, currency):
        """Форматирует сумму с символом валюты"""
        symbol = self.get_currency_symbol(currency)
        return f"{symbol}{amount:.2f}"