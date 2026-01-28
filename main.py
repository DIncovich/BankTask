from BankAccount import BankAccount
from errors import AccountFrozenError, InvalidOperationError, InsufficientFundsError

def main():
    print("тест1")
    try:
        user_account = BankAccount(owner_data="Иван Иванькин", currency="RUB")

        print(user_account)

        user_account.deposit(15000)

        user_account.withdraw(5000)

        print(f"Текущий остаток: {user_account.get_account_info()['Balance']} RUB\n")

    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}\n")


    print("тест2")
    try:
        frozen_account = BankAccount(
            owner_data="Я Мита",
            currency="USD",
            status="frozen",
            account_id="999999"
        )

        frozen_account.deposit(1000)

    except AccountFrozenError as e:
        print(f"Операция заблокирована. Ошибка: \"{e}\"\n")
    except Exception as e:
        print(f"Ошибка: {e}\n")


    print("тест3")
    try:
        test_account = BankAccount("Дада Нетнет", "EUR")

        test_account.withdraw(-500)

    except InvalidOperationError as e:
        print(f"Неверная сумма. Ошибка: \"{e}\"")

    try:
        test_account.withdraw(1000)

    except InsufficientFundsError as e:
        print(f"Нехватка средств. Ошибка: \"{e}\"")


if __name__ == "__main__":
    main()