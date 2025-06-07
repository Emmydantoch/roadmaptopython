from bank_accounts import *


Dave = BankAccount("Dave", 1000)
Alice = BankAccount("Alice", 500)

Dave.getBalance()
Alice.getBalance()

Alice.deposite(200)
Dave.deposite(300)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Alice)
Dave.transfer(100, Alice)

jim = InterestRewardsAcct("Jim", 1000)
jim.getBalance()

jim.deposite(100)

jim.transfer(100, Dave)

Praise = SavingsAcct("Praise", 1000)

Praise.getBalance()

Praise.deposite(100)

Praise.transfer(10000, Alice)
