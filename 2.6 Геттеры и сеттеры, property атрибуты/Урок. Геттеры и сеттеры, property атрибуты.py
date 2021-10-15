'''
Геттеры и сеттеры, property атрибуты
 http://egoroffartem.pythonanywhere.com/course/oop-python/gettery-i-settery-property-atributy

'''


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')  # индикатор работы метода
        return self.__balance

    def set_balance(self, value):
        print('set balance')  # индикатор работы метода
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числовым')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')  # индикатор работы метода
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

b = BankAccount('Misha', 400)
b.balance = 777
b.balance

a = BankAccount('Masha', 300)
a.balance
a.balance = 555
a.balance

del a.balance
print(a.balance, b.balance)
