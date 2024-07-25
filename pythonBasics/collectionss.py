"""
Container Sequence: list, tuple, collections.deque can hold items of different types of sequence

Flat Sequence: str, byte, bytearray, memoryview, array.array can hold items of one type only

Ordered dict:: they are similar to dict() type , but has additional features related to ordering

OrderedDict algorithm can handle frequent reordering operation better than normal dict(). Suitable for implementing various
kinds of LRU caches.

"""

# Defining and using namedtuple type
from collections import namedtuple

'''Here the first argument should be the name of the namedtuple type and second 
argument should be a string contatining the names of the fields separated by 
spaces or commas
'''
Food= namedtuple('FoodItems', 'name ingredients chemicalcomposition weight')

oats= Food('Instant-oats', 'barley', "protein fibers", 100)


Car= namedtuple("CarBrands", 'name no_of_tyres no_of_sitter mileage speed')

car_one= Car('tesla-x1', 4, 2, 45, 50 )

print(car_one)
print(oats)


