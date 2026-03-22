from datetime import datetime
from errors import AuthenticationError

class Bank:
    def __init__(self):
        self.clients = {}
        self.all_accounts = {}
        self.suspicious_limit = 500000

    def add_client(self, client):
        self.clients[client.client_id] = client
        print(f"Зарегистрирован клиент: {client.full_name} (ID: {client.client_id})")

    def authenticate_client(self, client_id, password):
        if client_id not in self.clients:
            raise AuthenticationError("Клиент с таким ID не найден.")

        client = self.clients[client_id]
        return client.authenticate(password)

    def open_account(self, client_id, account_obj):
        """привязка счета к клиенту и добавление в банк"""
        if client_id not in self.clients:
            print("Клиент не найден.")
            return

        self.all_accounts[account_obj.account_id] = account_obj

        client = self.clients[client_id]
        client.add_account(account_obj.account_id)

        print(f"Счет {account_obj.account_id} успешно привязан к клиенту {client.full_name}.")

    def close_account(self, account_id):
        if account_id in self.all_accounts:
            self.all_accounts[account_id].status = 'closed'
            print(f"Счет {account_id} закрыт.")

    def freeze_account(self, account_id):
        if account_id in self.all_accounts:
            self.all_accounts[account_id].status = 'frozen'
            print(f"Счет {account_id} заморожен.")

    def unfreeze_account(self, account_id):
        if account_id in self.all_accounts:
            self.all_accounts[account_id].status = 'active'
            print(f"Счет {account_id} разморожен.")

    def search_accounts(self, client_id):
        client = self.clients.get(client_id)
        if client:
            print(f"Найдены счета для {client.full_name}: {client.accounts}")
            return client.accounts
        return []

    def process_withdrawal(self, account_id, amount):
        acc = self.all_accounts.get(account_id)
        if not acc:
            print("Счет не найден.")
            return

        if amount >= self.suspicious_limit:
            print(f"Попытка снять крупную сумму ({amount}) со счета {account_id}.")

        acc.withdraw(amount)
        self._send_notification(f"Со счета {account_id} успешно снято {amount}.")

    def _send_notification(self, message):
        """отправка смски с учетом ночного времени"""
        current_hour = datetime.now().hour
        if 0 <= current_hour < 5:
            print("Уведомление отложено. Действует запрет сообщений с 00:00 - 05:00.")
        else:
            print(f"СМС: {message}")