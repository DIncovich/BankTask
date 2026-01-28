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
            raise AccountFrozenError("Операция невозможна: Счет заморожен")
        if self.status == 'closed':
            raise AccountClosedError("Операция невозможна: Счет закрыт")

    def deposit(self, amount):
        self._check_status()

        if amount <= 0:
            raise InvalidOperationError("Сумма пополнения должна быть положительной")

        self._balance += amount
        print(f"Пополнено: {amount} {self.currency}. Баланс: {self._balance}")

    def withdraw(self, amount):
        self._check_status()

        if amount <= 0:
            raise InvalidOperationError("Сумма снятия должна быть положительной")

        if amount > self._balance:
            raise InsufficientFundsError(f"Недостаточно средств. Баланс: {self._balance}")

        self._balance -= amount
        print(f"Снято: {amount} {self.currency}. Баланс: {self._balance}")

    def get_account_info(self):
        return {
            "ID": self.account_id,
            "Owner": self.owner_data,
            "Balance": self._balance,
            "Currency": self.currency,
            "Status": self.status
        }

    def __str__(self):
        last_4_digits = str(self.account_id)[-4:]

        return (
            f"--- Информация о счете ---\n"
            f"Тип счета: Банковский счет\n"
            f"Клиент: {self.owner_data}\n"
            f"Номер: ****{last_4_digits}\n"
            f"Статус: {self.status}\n"
            f"Баланс: {self._balance} {self.currency}\n"
            f"--------------------------"
        )