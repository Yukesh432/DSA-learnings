# def factorial(n):
#     if n==0:
#         return 1

#     return n*factorial(n-1)

# print(factorial(6))

# print(factorial.__doc__)


# print(dir(factorial))

# print(factorial.__dict__)
"""
Closures:: Closures are the function with the extended scope that can access non-global variables referenced in thee body of the function
but not defined there.

"""
import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' %person