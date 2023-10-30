class Person:
    def __init__(self, name, age, gender) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender # Privaty Attributes

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def mymethod():
        print('Static method')

    def __str__(self) -> str:
        return f'{self.__name} - {self.__age}'


Person.mymethod()

p1 = Person('miguel', 19, 'M')
p1.__age = 12 # This is not working

print(p1)

p1.Name = 'Bob'

print(p1)

