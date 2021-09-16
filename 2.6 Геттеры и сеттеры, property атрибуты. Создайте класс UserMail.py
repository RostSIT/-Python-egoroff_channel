'''Создайте класс UserMail, у которого есть:

конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
Их необходимо сохранить в экземпляр как атрибуты login и __email
(обратите внимание, защищенный атрибут)
метод геттер get_email, которое возвращает защищенный атрибут __email ;
метод сеттер set_email, которое принимает в виде строки новую почту.
Метод должен проверять, что в новой почте есть только один символ @ и
после нее есть точка. Если данные условия выполняются, новая почта
сохраняется в атрибут __email, в противном случае выведите сообщение
"Ошибочная почта";
создайте свойство email, у которого геттером будет метод get_email,
а сеттером - метод set_email
k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait'''

class UserMail:
    def __init__(self, login, __email):
        self.login = login
        self.__email = __email

    def get_email(self,):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str)\
            and new_email.count('@') == 1\
            and '.' in new_email[new_email.find('@'):]:
            self.__email = new_email
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)
