from abc import ABCMeta, abstractclassmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, employees: int) -> None:
        """ Implement in child class """
    
    @abstractstaticmethod
    def print_department(self) -> None:
        """ Implement in child class """

class Accounting(IDepartment):
    
    def __init__(self, employees: int):
        self.employees = employees
    
    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):
    
    def __init__(self, employees: int):
        self.employees = employees
    
    def print_department(self):
        print(f"Development Department: {self.employees}")
    
class ParentDepartment(IDepartment):
    
    def __init__(self, employees: int):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []
    
    def add(self, dept: IDepartment):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")

dept = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept)
parent_dept.add(dept2)

parent_dept.print_department()