from abc import ABC, abstractmethod

class AbstractAccount(ABC):
    def __init__(self, owner_data, status='active', account_id=None):
        self.account_id = account_id
        self.owner_data = owner_data
        self.status = status
        self._balance = 0.0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_account_info(self):
        pass