from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def print_data():
        """ Implement in child class """

class PersonSingleton(IPerson):
    __instance = None
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age) -> None:
        if self.__instance != None:
            raise Exception("Singleton cannot be instatiated more than once")
        self.name = name
        self.age = age
        PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name} - Age: {PersonSingleton.__instance.age}")
    

p = PersonSingleton("Miguel", 10)
print(p)
p.print_data()


p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()