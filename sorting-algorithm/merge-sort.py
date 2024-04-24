import numpy as np
import random
from random import randint
from timeit import repeat



def merge_sort(left, right):
    #if the first array is empty do nothing and pass simply the second array as the result
    if(len(left)==0):
        return right
    # similarly, if the 2nd array is empty , return the 1st array as it is
    if(len(right)==0):
        return left
    
    result= []
    left_index, right_index= 0, 0
    # now we loop through all the elements in the array to add them to new array i.e results[]
    while(len(result)< len(left)+ len(right)):
        if left[left_index]<right[right_index]:
            result.append(left[left_index])
            left_index+=1
        else:
            result.append(right[right_index])
            right_index+=1

        # now when the element from any either array is finished, then add the remaining elements from the other 
        # array  to the final array

        if right_index== len(right):
            result+=left[left_index:]
            break

        if left_index== len(left):
            result+=right[right_index:]
            break
    return result


def merge_recursive(array):

    if len(array)<2:
        return array
    
    midpoint= len(array)//2

    # now we sort the array by recursively splitting the input into two equal halves
    # sorting each half and merging them together into the final result
    left_array= merge_recursive(array[:midpoint])
    right_array= merge_recursive(array[midpoint:])
    result= merge_sort(left_array, right_array)
    return result
    # return merge_sort(
    #     left=merge_recursive(array[:midpoint]),
    #     right=merge_recursive(array[midpoint:]))
# def run_sorting_algorithm(algorithm, array):
#     # Set up the context and prepare the call to the specified
#     # algorithm using the supplied array. Only import the
#     # algorithm function if it's not the built-in `sorted()`.
#     setup_code = f"from __main__ import {algorithm}" \
#         if algorithm != "sorted" else ""

#     stmt = f"{algorithm}({array})"

#     # Execute the code ten different times and return the time
#     # in seconds that each execution took
#     times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

#     # Finally, display the name of the algorithm and the
#     # minimum time it took to run
#     print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    ARRAY_LENGTH= 10
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print("Before sorting:: ", array)
    # list1= np.random.randint(1,10, 7)
    # list2= np.random.randint(1,10, 7)
    # merge_sort()
    result= merge_recursive(array)
    print(result)
# result= []
    # # Generate an array of `ARRAY_LENGTH` items consisting
    # # of random integer values between 0 and 999
    # array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # # Call the function using the name of the sorting algorithm
    # # and the array you just created
    # run_sorting_algorithm(algorithm="merge_recursive", array=array)