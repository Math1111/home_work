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

#создаётся объект класа(MyBankAccount), устанавливается приватная переменная __balance
#Функция deposit увеличивает баланс на заданную сумму (если выполняется условие)
#Функция withdraw отвечает за списание средств с аккаунта
# Функция get_balance  возвращает текущий баланс.