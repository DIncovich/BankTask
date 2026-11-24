from AbstractAccount import AbstractAccount
from errors import AccountFrozenError, AccountClosedError, InvalidOperationError, InsufficientFundsError
import random

class BankAccount(AbstractAccount):
    ALLOWED_CURRENCIES = ["RUB", "USD", "EUR", "KZT", "CNY"]

    def __init__(self, owner_data, currency, status='active', account_id=None):
        if account_id is None:
            account_id = str(random.randint(100000, 999999))
        super().__init__(owner_data, status, account_id)

        if currency not in self.ALLOWED_CURRENCIES:
            raise InvalidOperationError(f"Валюта {currency} не поддерживается")
        self.currency = currency

    def _check_status(self):
        if self.status == 'frozen':
            raise AccountFrozenError("Счет заморожен")
        if self.status == 'closed':
            raise AccountClosedError("Счет закрыт")

    def deposit(self, amount):
        self._check_status()
        if amount <= 0:
            raise InvalidOperationError("Сумма должна быть положительной")
        self._balance += amount
        print(f"Пополнено: {amount} {self.currency}. Баланс: {self._balance}")

    def withdraw(self, amount):
        self._check_status()
        if amount <= 0:
            raise InvalidOperationError("Сумма должна быть положительной")
        if amount > self._balance:
            raise InsufficientFundsError(f"Недостаточно средств. Баланс: {self._balance}")
        self._balance -= amount
        print(f"[Withdraw] Снято: {amount} {self.currency}. Баланс: {self._balance}")

    def get_account_info(self):
        return {"Type": "Basic", "Balance": self._balance}

    def __str__(self):
        return f"Счет {self.account_id} | Баланс: {self._balance} {self.currency}"