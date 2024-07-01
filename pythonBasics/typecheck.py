# REF:: https://realpython.com/python-type-checking/

# Static Typing vs. Dynamic Typing

# Static Typing:
# In statically typed languages, the type of a variable is known at compile time.
# Python supports static typing through the use of type hints introduced in Python 3.5.
# However, these type hints are not enforced at runtime and are mainly for documentation
# and type checking tools like mypy.

def add_numbers_static(a: int, b: int) -> int:
    """
    Function to add two integers with static typing.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b

# Dynamic Typing:
# In dynamically typed languages like Python, the type of a variable is known at runtime.
# This allows for more flexibility, but can also lead to runtime errors if not handled properly.

def add_numbers_dynamic(a, b):
    """
    Function to add two numbers with dynamic typing.

    Args:
        a: The first number (type can be any).
        b: The second number (type can be any).

    Returns:
        The sum of the two numbers.
    """
    return a + b

if __name__ == "__main__":
    # Static Typing Example
    result_static = add_numbers_static(10, 20)
    print(f"Static Typing Result: {result_static}")

    # Dynamic Typing Example
    result_dynamic = add_numbers_dynamic(10, 20)
    print(f"Dynamic Typing Result (int + int): {result_dynamic}")

    result_dynamic_str = add_numbers_dynamic("hello", "world")
    print(f"Dynamic Typing Result (str + str): {result_dynamic_str}")

    
    # The following will cause a runtime error since you can't add int and str
    result_dynamic_error = add_numbers_dynamic(10, "world")
    print(f"Dynamic Typing Result (int + str): {result_dynamic_error}")
