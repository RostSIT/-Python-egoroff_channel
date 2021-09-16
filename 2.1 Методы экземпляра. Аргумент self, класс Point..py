'''Создайте класс Lion. В нем должен быть метод roar,
который печатает на экран "Rrrrrrr!!!"

Пример работы с классом Lion

simba = Lion()
simba.roar() # печатает Rrrrrrr!!!'''


import math


class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print(f'Передана не точка')
