# OOP is Object-Oriented Programming, a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes), and code, in the form of procedures (often known as methods).
# OOP allows for encapsulation, inheritance, and polymorphism, making it easier to manage complex software systems.
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, name, balance):
        self.acctName = name
        self.balance = float(balance)
        print(
            "\nAccount '{}' created.\nBalance = ${:.2f}".format(
                self.acctName, self.balance
            )
        )

    def getBalance(self):
        print("\nAccount '{}' balance = ${:.2f}".format(self.acctName, self.balance))
        return self.balance

    def deposite(self, amount):
        self.balance += float(amount)
        print(
            "\nAccount '{}' deposit = ${:.2f}\nNew balance = ${:.2f}".format(
                self.acctName, amount, self.balance
            )
        )
        return self.balance

    def withdraw(self, amount):
        if self.balance >= float(amount):
            self.balance -= float(amount)
            print(
                "\nAccount '{}' withdraw = ${:.2f}\nNew balance = ${:.2f}".format(
                    self.acctName, amount, self.balance
                )
            )
            return True
        else:
            print("\nInsufficient funds in account '{}'".format(self.acctName))
            return False

    def transfer(self, amount, account):
        if self.withdraw(amount):
            account.deposite(amount)
            return True
        return False


class InterestRewardsAcct(BankAccount):
    def deposite(self, amount):
        self.balance += float(amount) * 1.05
        print(
            "\nAccount '{}' deposit = ${:.2f}\nNew balance = ${:.2f}".format(
                self.acctName, amount, self.balance
            )
        )
        return self.balance


class SavingsAcct(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.fee = 5

    def withdraw(self, amount):
        if self.balance >= float(amount) + self.fee:
            self.balance -= float(amount) + self.fee
            print(
                "\nAccount '{}' withdraw = ${:.2f}\nFee = ${:.2f}\nNew balance = ${:.2f}".format(
                    self.acctName, amount, self.fee, self.balance
                )
            )
            return True
        else:
            print("\nInsufficient funds in account '{}'".format(self.acctName))
            return False
