# def mydecorator(function):

#     def wrapper(*args, **kwargs):
#         return_value = function(*args, **kwargs)

#         print('I am decorating your function')

#         return return_value
#     return wrapper

# @mydecorator
# def hello_word(person: str) -> str:
#     return f"Hello Word: {person}"


# # fun = mydecorator(hello_word)
# # fun()

# print(hello_word("Miguel"))

# ======================== LOG ===================

# def logged(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args, **kwargs)

#         with open('logfile.txt', 'a+') as f:
#             fname = function.__name__
#             f.write(f"{fname}: returned value {value}\n")
#         return value
#     return wrapper

# @logged
# def add(x, y):
#     return x + y

# print(add(10,20))

# ======================== Timing ===================
import time

def timed(function):
    def wrapper(*args, **kwargs):
        init = time.time()
        value = function(*args, **kwargs)
        finish = time.time()
        fname = function.__name__
        print(f"{fname} - Time of executing: {finish - init}s")
        return value
    return wrapper

@timed
def exponetion(x, y):
    result = x
    for i in range(y-1):
        result *= x
    return result

print(exponetion(10,3))