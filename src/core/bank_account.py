from abc import ABC, abstractmethod
from src.utils.id_generator import create_id
from src.utils.account_number import account_number
from src.security.password_security import creating_hash

class BankAccount(ABC):
    _transaction_types = ['withdraw', 'deposit', 'debit_payment', 'credit_payment', 'invest', 'redeem']

    def __init__(self, account_type: str, cardholder_name: str, password: str):
        self._id = create_id()
        self._cardholder_name = cardholder_name
        self._password = creating_hash(password=password)
        self._account_number = account_number()
        self._account_type = account_type
        self._transaction_history = [] 

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    def transaction_history(self, transaction_type: str, value: float | int):
        if not isinstance(transaction_type, str):
            raise TypeError('Error: Transaction type must be a string.')
        
        if not isinstance(value, (float, int)):
            raise TypeError('Error: Value must be a number.')
        
        if value <= 0:
            raise ValueError('Invalid value error.')

        transaction_type = transaction_type.lower()

        if transaction_type not in self._transaction_types:
            raise ValueError('Error: Invalid transaction type.')

        self._transaction_history.append({
            'type': transaction_type,
            'transaction value': value
        })
        