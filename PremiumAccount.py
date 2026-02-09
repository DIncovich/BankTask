from BankAccount import BankAccount
from errors import InvalidOperationError, InsufficientFundsError

class PremiumAccount(BankAccount):
    def __init__(self, owner_data, currency, overdraft_limit=5000, commission=50):
        super().__init__(owner_data, currency)
        self.overdraft_limit = overdraft_limit
        self.commission = commission

    def withdraw(self, amount):
        self._check_status()
        if amount <= 0:
            raise InvalidOperationError("Сумма должна быть положительной")

        total_withdraw = amount + self.commission

        if (self._balance - total_withdraw) < -self.overdraft_limit:
            raise InsufficientFundsError(f"Превышен лимит овердрафта ({self.overdraft_limit})")

        self._balance -= total_withdraw
        print(f"[Premium] Снято: {amount} + Комиссия: {self.commission}. Баланс: {self._balance}")

    def get_account_info(self):
        info = super().get_account_info()
        info.update({
            "Type": "Premium",
            "Overdraft Limit": self.overdraft_limit,
            "Commission": self.commission
        })
        return info

    def __str__(self):
        return f"[Premium] {self.account_id} | Овердрафт до: -{self.overdraft_limit} | Баланс: {self._balance} {self.currency}"