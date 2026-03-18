from BankAccount import BankAccount
from errors import InvalidOperationError, InsufficientFundsError

class SavingsAccount(BankAccount):
    def __init__(self, owner_data, currency, min_balance=1000, interest_rate=0.05):
        super().__init__(owner_data, currency)
        self.min_balance = min_balance
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        self._check_status()
        if amount <= 0:
            raise InvalidOperationError("Сумма должна быть положительной")

        if (self._balance - amount) < self.min_balance:
            raise InsufficientFundsError(
                f"Операция отклонена. Нельзя снижать баланс ниже {self.min_balance} {self.currency}"
            )

        self._balance -= amount
        print(f"[Savings] Снято: {amount}. Остаток: {self._balance} (Мин. остаток: {self.min_balance})")

    def calculate_monthly_profit(self):
        profit = self._balance * self.interest_rate
        print(f"Ожидаемая прибыль за месяц: {profit:.2f} {self.currency}")
        return profit

    def get_account_info(self):
        info = super().get_account_info()
        info.update({
            "Type": "Savings",
            "Min Balance": self.min_balance,
            "Interest Rate": f"{self.interest_rate * 100}%"
        })
        return info

    def __str__(self):
        return f"{self.account_id} | Владелец: {self.owner_data} | Баланс: {self._balance} {self.currency}"