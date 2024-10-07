class MyBankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Недостаточно средств')

    def get_balance(self):
        return self.__balance

account = MyBankAccount(1000000)
account.deposit(5)
print(account.get_balance())

#Так как это класс личный баланс, он приватный так как нельзя изменить его значение вне класса. Поменять баланс можно
#только если положить деньги на счет или потратить, или если это сделают мошенники, именно по этому он приватный