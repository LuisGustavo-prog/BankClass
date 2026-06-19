from src.core.bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, cardholder_name: str, password: str,  account_type: str = 'Checking Account'):
        super().__init__(account_type, cardholder_name, password)
        self._debit = 0.0
        self._credit = 100.0
    
    def withdraw(self, value: float | int, transaction_type: str = 'withdraw'):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value error.')
        
        if value <= 0:
            raise ValueError('Invalid value error.')
        
        if self._debit < value:
            raise ValueError('insufficient balance.')
        
        self._debit -= value
        self.transaction_history(transaction_type=transaction_type, value=value)
    
    def deposit(self, value: float | int):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value error.')
        
        if value <= 0:
            raise ValueError('Invalid value error.')
        
        self._debit += value
        self.transaction_history(transaction_type='deposit', value=value)
    
    def debit_payment(self, value: float | int):
        self.withdraw(value=value, transaction_type='debit_payment')
        
    def credit_payment(self, value: float | int):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value error.')
        
        if value <= 0:
            raise ValueError('Invalid value error.')
        
        if self._credit < value:
            raise ValueError('insufficient balance.')
        
        self._credit -= value
        self.transaction_history(transaction_type='credit_payment', value=value)
    
    def to_dict(self):
        return {
            '_id': self._id,
            'account_number': self._account_number,
            'account_type': self._account_type,
            'cardholder_name': self._cardholder_name,
            'password': self._password,
            'debit': self._debit,
            'credit': self._credit,
            'transaction_history': self._transaction_history
        }
