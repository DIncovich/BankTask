from SavingAccount import SavingsAccount
from PremiumAccount import PremiumAccount
from InvestmentAccount import InvestmentAccount
from errors import InsufficientFundsError, AgeRestrictionError, AuthenticationError
from Client import Client
from Bank import Bank


def main():
    print("--- Тест SavingsAccount ---")
    try:
        saver = SavingsAccount("Анна Смирнова", "RUB", min_balance=2000)
        saver.deposit(5000)
        print("Попытка снять 4000")
        saver.withdraw(4000)
    except InsufficientFundsError as e:
        print(f"Ошибка: {e}")
    saver.calculate_monthly_profit()
    print(saver)

    print("\n--- Тест PremiumAccount ---")
    try:
        vip = PremiumAccount("Илон Маск", "USD", overdraft_limit=1000)
        vip.deposit(500)
        print("Снимаем 1000")
        vip.withdraw(1000)
        print(vip)
        print("Попытка снять еще 1000")
        vip.withdraw(1000)
    except InsufficientFundsError as e:
        print(f"Ошибка: {e}")

    print("\n--- Тест InvestmentAccount ---")
    inv = InvestmentAccount("Уоррен Баффет", "USD")
    inv.deposit(10000)
    inv.buy_asset("Apple Stock", quantity=10, price=150, yearly_yield=0.08)
    inv.buy_asset("US Bonds", quantity=20, price=100, yearly_yield=0.04)
    inv.project_yearly_growth()
    print(inv)

    print("\n--- 3 задание ---")

    bank = Bank()

    print("\n--- Регистрация клиентов ---")
    try:
        client1 = Client("Иван Иванов", 25, "pass123", "+79991234567")
        bank.add_client(client1)

        client2 = Client("Петя Школьник", 16, "qwerty", "+79990000000")
        bank.add_client(client2)
    except AgeRestrictionError as e:
        print(f"Поймана ошибка: {e}")

    print("\n--- Открытие счетов ---")
    new_vip_account = PremiumAccount(client1.full_name, "RUB")
    bank.open_account(client1.client_id, new_vip_account)

    bank.search_accounts(client1.client_id)

    print("\n--- Защита и операции ---")
    new_vip_account.deposit(1_000_000)

    bank.process_withdrawal(new_vip_account.account_id, 600_000)

    print("\n--- Авторизация и блокировка ---")
    bank.authenticate_client(client1.client_id, "wrong_password")
    bank.authenticate_client(client1.client_id, "wrong_password")
    bank.authenticate_client(client1.client_id, "wrong_password")

    try:
        bank.authenticate_client(client1.client_id, "pass123")
    except AuthenticationError as e:
        print(f"Поймана ошибка: {e}")

    print("\n--- Заморозка счета ---")
    bank.freeze_account(new_vip_account.account_id)
    try:
        bank.process_withdrawal(new_vip_account.account_id, 1000)
    except Exception as e:
        print(f"Операция отклонена: {e}")


if __name__ == "__main__":
    main()