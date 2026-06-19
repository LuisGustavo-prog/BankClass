from src.utils.id_generator import create_id
from src.security.password_security import creating_hash

class EmployeeClass:
    def __init__(self, name: str, email: str, password: str):
        self._id = create_id()
        self._name = name
        self._email = email
        self._password = creating_hash(password=password)
        
    def to_dict(self):
        return {
            '_id': self._id,
            'email': self._email,
            'password': self._password
        }
    