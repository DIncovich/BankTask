from SavingAccount import SavingsAccount
from  PremiumAccount import PremiumAccount
from InvestmentAccount import InvestmentAccount
from errors import InsufficientFundsError


def main():
    print("--- Тест SavingsAccount ---")
    try:
        saver = SavingsAccount("Анна Смирнова", "RUB", min_balance=2000)
        saver.deposit(5000)

        print("Попытка снять 4000 (остаток будет 1000, а минимум 2000)...")
        saver.withdraw(4000)
    except InsufficientFundsError as e:
        print(f"Ошибка поймана: {e}")

    saver.calculate_monthly_profit()
    print(saver)

    print("\n--- Тест PremiumAccount ---")
    try:
        vip = PremiumAccount("Илон Маск", "USD", overdraft_limit=1000)
        vip.deposit(500)

        print("Снимаем 1000 (баланс 500)...")
        vip.withdraw(1000)
        print(vip)

        print("Попытка снять еще 1000...")
        vip.withdraw(1000)
    except InsufficientFundsError as e:
        print(f"Ошибка поймана: {e}")


    print("\n--- Тест InvestmentAccount ---")
    inv = InvestmentAccount("Уоррен Баффет", "USD")
    inv.deposit(10000)

    inv.buy_asset("Apple Stock", quantity=10, price=150, yearly_yield=0.08)  # 8% годовых
    inv.buy_asset("US Bonds", quantity=20, price=100, yearly_yield=0.04)  # 4% годовых

    inv.project_yearly_growth()

    print(inv)


if __name__ == "__main__":
    main()