# def factorial(n):
#     if n==0:
#         return 1

#     return n*factorial(n-1)

# print(factorial(6))

# print(factorial.__doc__)


# print(dir(factorial))

# print(factorial.__dict__)
"""
Closures:: Closures are the function with the extended scope that can access non-global variables 
referenced in thee body of the function but not defined there.

"""
# import bobo

# @bobo.query('/')
# def hello(person):
#     return 'Hello %s!' %person

from typing import Any


class Average():

    def __init__(self):
        self.series= []

    def __call__(self, new_value):
        self.series.append(new_value)
        total= sum(self.series)
        return total/len(self.series)
    


avg= Average()
print(avg(10))
print(avg(15))
print(avg(20))

# ............................................................................

# Now implementation of averge with higher order function

def make_averager():
    series= []
 
    def averager(new_value):
        series.append(new_value)
        total= sum(series)
       
        return total/len(series)
    
    return averager   # It is returning the function object

# when called , the make_averager returns an averager function object. Each time an averager 
# is called, it appends the passed argument to the series, and computes the curent average.


avg= make_averager()
print(avg(10))
print(avg(20))

print(avg.__code__.co_varnames)

"""
 A closure is a function that retains the bindings of the free variables
 that exist when the function is defined., so that they can be used later when the function is
 invoked and the defining scope is no longer available.
"""

"""
The nonlocal declaration::

UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
"""

def make_averager():
     count = 0 
     total = 0 
     def averager(new_value): 
        count += 1 
        total += new_value 
        return total / count 
     return averager

avgg= make_averager()
avgg(12)