class AccountFrozenError(Exception):
    """счет заморожен"""
    pass

class AccountClosedError(Exception):
    """счет закрыт"""
    pass

class InvalidOperationError(Exception):
    """недопустимая операция"""
    pass

class InsufficientFundsError(Exception):
    """недостаточно средств"""
    pass

class AgeRestrictionError(Exception):
    """клиенту меньше 18 лет"""
    pass

class AuthenticationError(Exception):
    """неверный логин или аккаунт заблокирован"""
    pass