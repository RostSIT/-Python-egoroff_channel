class Cat:
    #  Создаем словарь
    __share_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):   #  При каждой инициализации атрибута класса
         self.__dict__ = Cat.__share_attr   #  __dict__ присваиваем значения __share_attr
        # И так ка это словарь, а словарь изменяемий атребут, его значения можно изменять
        # в любом экземпляре класса для всех экземпляров класса.
#  __dict__ это словарь в котором хранятся атребуты экземпляра класса

a = Cat()
b = Cat()
a.breed = 'siam'
b.color = 'black'
c = Cat()
c.color = 'green'
c.breed = 'sphinx'

