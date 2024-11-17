from PyQt6.QtWidgets import QWidget
from constants import CURRENCY_SYMBOLS


class CurrencyCalculator(QWidget):
    def __init__(self):
        self.currency_symbols = CURRENCY_SYMBOLS

        super().__init__()

        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.92,
            'GBP': 0.82,
            'JPY': 134.12,
            '₸': 460.0,
        }

    def convert(self, amount, from_currency, to_currency):
        """Конвертация из одной валюты в другую"""
        try:
            if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
                return f"Ошибка: Некорректные валюты {from_currency} или {to_currency}"

            amount_in_usd = float(amount) / self.exchange_rates[from_currency]
            converted_amount = amount_in_usd * self.exchange_rates[to_currency]

            return round(converted_amount, 2)
        except Exception as e:
            return f"Ошибка: {e}"

    def add_exchange_rate(self, currency, rate):
        try:
            self.exchange_rates[currency] = float(rate)
            return f"Курс валюты {currency} обновлен на {rate}"
        except Exception as e:
            return f"Ошибка: {e}"

    def remove_exchange_rate(self, currency):
        try:
            if currency in self.exchange_rates:
                del self.exchange_rates[currency]
                return f"Курс валюты {currency} удален"
            else:
                return f"Ошибка: Валюта {currency} не найдена"
        except Exception as e:
            return f"Ошибка: {e}"

    def list_exchange_rates(self):
        return self.exchange_rates

    def get_currency_symbols(self):
        return self.currency_symbols
