import datetime # for date time
import uuid # to generate a Universally unique identifier


class BalanceNotSufficient(Exception):
    pass


class LimitExceeded(Exception):
    pass


class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class BankAccount:
    def __init__(self, input_user, input_balance, input_type, input_limit):
        self.user = input_user
        self.__balance = input_balance
        self.type = input_type
        self.limit = input_limit
        self.created = datetime.datetime.now()
        self.number = str(uuid.uuid4())

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount <= self.limit:
            self.__balance = amount
        else:
            raise LimitExceeded

    def debit(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise BalanceNotSufficient

    def credit(self, amount):
        self.balance += amount

    def transfer(self, recipient, amount):
        self.debit(amount)
        recipient.credit(amount)


ayo = User("ayo", "ayo@mumswhocode.com", "Washington DC")
folake = User("James", "folake@mumswhocode.com", "12 Helsinki")
ayo_account = BankAccount(ayo, 0, "savings", 100)
folake_account = BankAccount(folake, 740, "savings", 2500)

# print(ayo_account.user.email)
# ayo_account.credit(50)
# print(ayo_account.balance)
# ayo_account.credit(23)
# print(ayo_account.balance)
# ayo_account.debit(1)
# print(ayo_account.balance)
# ayo_account.debit(100)
# print(ayo_account.balance)
# print(folake_account.balance)
# ayo_account.credit(500)
# print(ayo_account.__balance)
# folake_account.transfer(ayo_account, 50)
# print(ayo_account.balance)
# print(folake_account.balance)