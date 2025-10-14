from functools import reduce


def even_sum(list):
    even =  [x for x in list if x %2==0]
    return reduce((lambda x, y: x + y), even)

list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even_sum(list))

