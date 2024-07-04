"""
REF:: https://stackoverflow.com/questions/27392402/what-is-first-class-function-in-python
https://www.geeksforgeeks.org/first-class-functions-python/

First-class functions are functions treated as first-class citizens (FCC) in a programming language.

FCC are "objects" which:
- Can be used as parameters
- Can be used as return values
- Can be assigned to variables
- Can be stored in data structures such as hashtables and lists
"""

def html_tag(tag):
    def wrap_text(msg):
        return f'<{tag}>{msg}</{tag}>'
    return wrap_text

# ..............................................................................................

"""
Implementing a custom map function in python

The built in map function in python applies a given function to each item of an iterable
and returns an iterator

"""

def custom_map(func, iterable):

    results= []

    for item in iterable:
        results.append(func(item))

    return results


def square(x):
    return x* x

# ..................................................................................................................

"""
Implemeting custom zip function

"""
def custom_zip(*iterables):
    iterators= [iter(it) for it in iterables]
    while True:
        try:
            yield tuple([next(it) for it in iterators])
        except StopIteration:
            return





if __name__=='__main__':
    # Here we are assigning the variable 'func1' to the function returned by 'html_tag'
    # Now the variable 'func1' is a function waiting to be called with the argument expected by 'wrap_text'
    # We use the 'wrap_text' function without being explicitly called
    # i.e., instead of calling 'wrap_text' explicitly, we're calling that function using the assigned variable 'func1'

    func1 = html_tag('p')
    print(func1("This is working"))  # Output: <p>This is working</p>


    numbers= [1,2,3,4,5]
    res= custom_map(square, numbers)
    print(res)

    ## trying out custom zip function
    list1= [1,2,3]
    list2= ['a', 'b', 'c']
    zipped= custom_zip(list1, list2)
    print(list(zipped))

    # or we can use next() to yield each element
    # print(next(zipped))
    # print(next(zipped))