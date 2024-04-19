import numpy as np

def sum_consecutive_elements(original_list):
    """
    Calculate the sum of consecutive elements in a list.

    Parameters:
    original_list : list
        The original list of numbers.

    Returns:
    list
        A new list containing the sum of consecutive elements from the original list.
    """
    # Create an empty list to store the sum of consecutive elements
    new_list = []

    # Iterate through the original list up to the second-to-last element
    for i in range(len(original_list) - 1):
        # Add the sum of consecutive elements to the new list
        new_list.append(original_list[i] + original_list[i + 1])

    return new_list

def same_list(original_list):
    for i in range(len(original_list)-1):
        original_list.append(original_list[i]+original_list[i+1])
    return original_list




# Example usage
original_list = [1, 2, 3, 4, 5]
# result = sum_consecutive_elements(original_list)

appended_list= same_list(original_list)
# print("Original list:", original_list)
print("New list:", appended_list)
