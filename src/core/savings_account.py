from src.core.bank_account import BankAccount
from src.core.investment import Investment

class SavingAccount(BankAccount):
    def __init__(self, cardholder_name: str, password: str,  account_type: str = 'Saving Account'):
        super().__init__(account_type, cardholder_name, password)
        self._debit = 0.0
        self._investments = []

    def withdraw(self, value: float | int):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value error.')
        
        if value <= 0:
            raise ValueError('Invalid value error.')
        
        if self._debit < value:
            raise ValueError('insufficient balance.')
        
        self._debit -= value
        self.transaction_history(transaction_type='withdraw', value=value)
    
    def deposit(self, value: float | int):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value error.')
        
        if value <= 0:
            raise ValueError('Invalid value error.')
        
        self._debit += value
        self.transaction_history(transaction_type='deposit', value=value)

    def invest(self, value: float | int, duration_days: int):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value.')
        
        if value <= 0:
            raise ValueError('Invalid value.')

        if value > self._debit:
            raise ValueError('Insufficient balance.')
        
        if not isinstance(duration_days, int) or duration_days <= 0:
            raise ValueError('Invalid duration.')
        
        self._debit -= value
        self._investments.append(Investment(value=value, duration_days=duration_days))
        self.transaction_history(transaction_type='invest', value=value)

    def redeem_investment(self):
        if not self._investments:
            raise ValueError('Error: No investments found.')

        matured_investments = [i for i in self._investments if i.is_mature]

        if not matured_investments:
            raise ValueError('Error: It is not possible to redeem any investments.')
        
        for investment in matured_investments:
            self._debit += investment.current_value
            self._investments.remove(investment)
            self.transaction_history(transaction_type='redeem', value=investment.current_value)

    def to_dict(self):
        return {
            '_id': self._id,
            'account_number': self._account_number,
            'account_type': self._account_type,
            'cardholder_name': self._cardholder_name,
            'password': self._password,
            'debit': self._debit,
            'investments': [
                {
                    'value': i._value,
                    'rate': i._rate,
                    'duration_days': i._duration_days,
                    'start_date': i._start_date.isoformat(),
                    'end_date': i.end_date.isoformat(),
                    'current_value': i.current_value,
                    'is_mature': i.is_mature
                }
                for i in self._investments
            ],
            'transaction_history': self._transaction_history
        }
