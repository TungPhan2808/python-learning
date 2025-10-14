from functools import reduce

a = {1,2,3,4}
b = {2,4,6,8}

c = {
    "a": 1,
    "b": 2,
    "c": 3
}
d = {
    "d": 1,
    "a": 2,
    "f": 3,
    "c": 4
}

try:
    result = 10/0
except ZeroDivisionError as e:
    print("Error: ", e)
else:
    print(result)
finally:
    print("Always executed")