"""
ООП 12 Property Вычисляемые свойства (Calculated properties python)

https://www.youtube.com/watch?v=CksCRU5SiK4
"""


class Square:

    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        print(self.__side)
        return self.__side


    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print(f'self.area = {self.__area}, calculate area ')
            self.__area = self.side**2
        print(self.__area)


a = Square(7)
a.side
a.area
a.side = 4
a.side
a.area
