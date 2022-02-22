class Vector:

    def __init__(self, *args):
        self.values = list(''.join([str(i) for i in args if isinstance(i, int)]))

    def __str__(self):
        if len(self.values) == 0:
            return f'Пустой вектор'
        else:
            result = ', '.join(map(str, sorted(self.values)))
            return str(f'Вектор({result})')


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"


class Vector:

    def __init__(self, *args):
        self.values = [i for i in args if isinstance(i, int)]

    def __str__(self):
        return f"Вектор{tuple(sorted(self.values))}" if self.values else 'Пустой вектор'


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"

# """3.1 Магические методы. Методы __str__ и __repr__
# 3 из 3 шагов пройдено
# 2 из 2 баллов  получено
#   Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
#
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо
# оставить только целые числа и сохранить их в атрибут values в виде списка; переопределить метод __str__ так,
# чтобы экземпляр класса Vector выводился следующим образом: "Вектор(<value1>, <value2>, <value3>, ...)", если вектор
# не пустой. При этом значения должны быть упорядочены по возрастанию (будьте аккуратнее с пробелами,
# они стоят только после запятых, см. пример ниже); "Пустой вектор", если наш вектор не хранит в себе значения
#
#
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2) # печатает "Пустой вектор""""
