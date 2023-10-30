# import sys

# def mygenerator(n):
#     for x in range(n):
#         yield x ** 3

# values = mygenerator(30000)



# for x in values:
#     print(x)

# print(sys.getsizeof(values))

# ================= INFINITY =================
def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

for x in range(100):
    print(next(values))