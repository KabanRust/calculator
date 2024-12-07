from PySide6.QtWidgets import QWidget
from decimal import Decimal, ROUND_HALF_UP

class AccountingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        
    def calculate_depreciation(self, initial_cost, salvage_value, useful_life, method='straight'):
        """
        Рассчитывает амортизацию актива.
        
        Args:
            initial_cost (float): Начальная стоимость актива
            salvage_value (float): Ликвидационная стоимость
            useful_life (int): Срок полезного использования в годах
            method (str): Метод расчета амортизации ('straight' или 'declining')
            
        Returns:
            dict: Результаты расчета амортизации по годам
        """
        try:
            initial_cost = Decimal(str(initial_cost))
            salvage_value = Decimal(str(salvage_value))
            useful_life = int(useful_life)
            
            if method == 'straight':
                annual_depreciation = (initial_cost - salvage_value) / useful_life
                results = {}
                
                for year in range(1, useful_life + 1):
                    book_value = initial_cost - (annual_depreciation * year)
                    results[year] = {
                        'depreciation': round(annual_depreciation, 2),
                        'book_value': round(book_value, 2)
                    }
                    
            elif method == 'declining':
                rate = 2 / useful_life  # Коэффициент ускоренной амортизации
                results = {}
                current_value = initial_cost
                
                for year in range(1, useful_life + 1):
                    depreciation = current_value * Decimal(str(rate))
                    if current_value - depreciation < salvage_value:
                        depreciation = current_value - salvage_value
                    current_value -= depreciation
                    results[year] = {
                        'depreciation': round(depreciation, 2),
                        'book_value': round(current_value, 2)
                    }
                    
            return results
            
        except Exception as e:
            return f"Ошибка при расчете амортизации: {str(e)}"

    def calculate_loan_amortization(self, principal, annual_rate, years, payments_per_year=12):
        """
        Рассчитывает амортизацию кредита.
        
        Args:
            principal (float): Сумма кредита
            annual_rate (float): Годовая процентная ставка (в процентах)
            years (int): Срок кредита в годах
            payments_per_year (int): Количество платежей в год
            
        Returns:
            dict: График платежей
        """
        try:
            principal = Decimal(str(principal))
            rate_per_period = Decimal(str(annual_rate / 100 / payments_per_year))
            total_payments = years * payments_per_year
            
            # Расчет ежемесячного платежа
            payment = principal * (rate_per_period * (1 + rate_per_period)**total_payments) / ((1 + rate_per_period)**total_payments - 1)
            payment = payment.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            
            schedule = {}
            balance = principal
            
            for period in range(1, total_payments + 1):
                interest = balance * rate_per_period
                principal_part = payment - interest
                balance -= principal_part
                
                schedule[period] = {
                    'payment': float(payment),
                    'principal': float(principal_part),
                    'interest': float(interest),
                    'balance': float(balance)
                }
                
            return schedule
            
        except Exception as e:
            return f"Ошибка при расчете амортизации кредита: {str(e)}"

    def calculate_vat(self, amount, rate=20):
        """
        Рассчитывает НДС
        
        Args:
            amount (float): Сумма без НДС
            rate (float): Ставка НДС в процентах
            
        Returns:
            dict: Результаты расчета НДС
        """
        try:
            amount = Decimal(str(amount))
            rate = Decimal(str(rate))
            
            vat = amount * rate / Decimal('100')
            total = amount + vat
            
            return {
                'amount': float(amount),
                'vat': float(vat),
                'total': float(total)
            }
            
        except Exception as e:
            return f"Ошибка при расчете НДС: {str(e)}"

    def calculate_salary(self, gross_salary, tax_rate=13, insurance_rate=2.9):
        """
        Рассчитывает зарплату с учетом налогов и отчислений
        
        Args:
            gross_salary (float): Грязная зарплата
            tax_rate (float): Ставка подоходного налога в процентах
            insurance_rate (float): Ставка страховых взносов в процентах
            
        Returns:
            dict: Результаты расчета зарплаты
        """
        try:
            gross = Decimal(str(gross_salary))
            
            tax = gross * Decimal(str(tax_rate)) / Decimal('100')
            insurance = gross * Decimal(str(insurance_rate)) / Decimal('100')
            net_salary = gross - tax - insurance
            
            return {
                'gross': float(gross),
                'tax': float(tax),
                'insurance': float(insurance),
                'net': float(net_salary)
            }
            
        except Exception as e:
            return f"Ошибка при расчете зарплаты: {str(e)}"