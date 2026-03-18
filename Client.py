import random
from errors import AgeRestrictionError

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

    def __str__(self):
        return f"Клиент: {self.full_name} | ID: {self.client_id} | Статус: {self.status}"