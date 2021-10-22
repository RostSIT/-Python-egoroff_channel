class Example:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')


a = Example()
#a.hello()
a.class_hello()
a.instance_hello()
a.static_hello()
print('\n\n')
#Example.class_hello()
#Example.instance_hello()
Example.static_hello()
Example.hello()

# https://www.patreon.com/posts/classmethod-i-37103841

