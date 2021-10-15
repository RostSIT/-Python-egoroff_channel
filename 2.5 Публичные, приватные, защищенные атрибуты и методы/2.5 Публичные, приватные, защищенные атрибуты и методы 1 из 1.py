class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    #  метод  protected обозначается, как _ одно нижнее подчеркивание
    #  Работает на уровне договоренности между разрабботчиками (не использовать вне класса)
    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    #  Метод private не дает использовать вне класса.
    #  можно обойти строки 8, 9 и 22 (инкапскляция)
    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 100000, 4549843875)
account1.print_public_data()
account1._BankAccount__print_private_data()
print(dir(account1))
# print(account1.__name)    Нет доступа вне класса.
# print(account1.__balance)    Нет доступа вне класса.
# print(account1.__passport)    Нет доступа вне класса.

# Посмотреть модуль accessify внутри него есть два декоратора protected и private
