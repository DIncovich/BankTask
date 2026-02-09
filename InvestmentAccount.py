from BankAccount import BankAccount
from errors import InsufficientFundsError

class InvestmentAccount(BankAccount):
    def __init__(self, owner_data, currency):
        super().__init__(owner_data, currency)
        self.portfolio = {}

    def buy_asset(self, asset_name, quantity, price, yearly_yield):
        cost = quantity * price
        if cost > self._balance:
            raise InsufficientFundsError("Недостаточно средств для покупки активов")

        self._balance -= cost

        if asset_name in self.portfolio:
            self.portfolio[asset_name]['quantity'] += quantity
        else:
            self.portfolio[asset_name] = {
                'quantity': quantity,
                'price': price,
                'yield': yearly_yield
            }
        print(f"[Invest] Куплено {quantity} шт. {asset_name}. Остаток кэша: {self._balance}")

    def project_yearly_growth(self):
        total_growth = 0
        print(f"--- Прогноз доходности портфеля ({self.owner_data}) ---")
        for name, data in self.portfolio.items():
            asset_value = data['quantity'] * data['price']
            growth = asset_value * data['yield']
            total_growth += growth
            print(f"Актив {name}: +{growth:.2f} {self.currency} (Ставка: {data['yield'] * 100}%)")

        print(f"ИТОГО прогноз за год: +{total_growth:.2f} {self.currency}")
        return total_growth

    def withdraw(self, amount):
        super().withdraw(amount)

    def get_account_info(self):
        info = super().get_account_info()
        info["Type"] = "Investment"
        info["Portfolio"] = self.portfolio.keys()
        return info

    def __str__(self):
        return f"[Инвестиции] {self.account_id} | Активов в портфеле: {len(self.portfolio)} | Кэш: {self._balance}"