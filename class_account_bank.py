class Account():                                                    # класс Аккаунт
    def __init__(self, id, balance=0):                              # создание аккаунта
        self.id = id                                                # инициализация счёта
        self.balance = balance                                      # инициализация баланса

    def deposit(self, money):                                       # функция пополнения депозита
        if money > 0:                                               # если сумма начисления больше 0 то
            self.balance += money                                   # к нашему балансу прибавляем эту сумму
            print(f"Вы успешно пополнили баланс. Сумма на счёту - {self.balance}")  # выводим сообщение о пополнении

    def withdraw(self, money):                                      # функция снятия денег
        if money > self.balance:                                    # если снимаемая сумма больше депозита то
            print(f"Не достаточно средств на счёте")                # выводим сообщение
        elif money <= self.balance:                                 # если денег достаточно
            self.balance -= money                                   # снимаем сумму со счёта
            print(f"Вы успешно сняли {money} рублей. Остаток на счёте: {self.balance}")

    def all_balance(self):                                          # функция просмотра баланса
        print(f"Текущий баланс - {self.balance}")

man = Account(id= "1010", balance= 800)                             # создание счёта

man.all_balance()                                                   # вызов функции баланса
man.withdraw(500)                                                   # вызов функции снятия денег
man.withdraw(400)                                                   # вызов функции снятия денег
man.deposit(1500)                                                   # вызов функции пополнения депозита
man.all_balance()                                                   # вызов функции баланса