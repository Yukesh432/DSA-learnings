"""
Container Sequence: list, tuple, collections.deque can hold items of different types of sequence

Flat Sequence: str, byte, bytearray, memoryview, array.array can hold items of one type only
"""

# Defining and using namedtuple type
from collections import namedtuple

Food= namedtuple('FoodItems', 'name ingredients chemicalcomposition weight')

oats= Food('Instant-oats', 'barley', "protein fibers", 100)

print(oats)

