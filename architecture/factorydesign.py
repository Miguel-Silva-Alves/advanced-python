from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):
    def __init__(self) -> None:
        self.name = "Basic Student Name"

    def person_method(self):
        print('I am Student')

class PersonFactory:
    @staticmethod
    def build_person(persontype: str):
        if persontype == "Student":
            return Student()
        raise Exception("Invalid Type")
        

if __name__ == "__main__":
    choice = input("What kind of person do you want to create? ")
    person = PersonFactory.build_person(choice)
    person.person_method() 