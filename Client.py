import random
from errors import AgeRestrictionError, AuthenticationError

class Client:
    def __init__(self, full_name, age, password, contacts):
        if age < 18:
            raise AgeRestrictionError(f"Регистрация отклонена: {full_name} младше 18 лет.")

        self.client_id = str(random.randint(1000, 9999))
        self.full_name = full_name
        self.password = password
        self.contacts = contacts
        self.status = 'active'
        self.accounts = []
        self.failed_login_attempts = 0

    def authenticate(self, password):
        if self.status == 'blocked':
            raise AuthenticationError("Вход запрещен: аккаунт заблокирован.")

        if self.password == password:
            self.failed_login_attempts = 0
            print(f"Успешный вход. Здравствуйте, {self.full_name}!")
            return True
        else:
            self.failed_login_attempts += 1
            print(f"Неверный пароль! Попытка {self.failed_login_attempts} из 3.")
            if self.failed_login_attempts >= 3:
                self.status = 'blocked'
                print(f"Аккаунт {self.full_name} заблокирован.")
            return False

    def add_account(self, account_id):
        """добавление айди счета в список клиента"""
        self.accounts.append(account_id)

    def __str__(self):
        return f"Клиент: {self.full_name} | ID: {self.client_id} | Статус: {self.status}"