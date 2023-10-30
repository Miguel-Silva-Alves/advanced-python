# class Person():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def __del__(self):
#         print('Object will be deleted!')

# p = Person("Miguel", 22)

# -===========================

from typing import Any


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __len__(self):
        return 10

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Hello I was called!")

v1 = Vector(10, 20)
v2 = Vector(50, 20)
v3 = v1 + v2

print(len(v3))

v3()