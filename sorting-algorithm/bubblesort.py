import numpy as np
import time
import random

def bubble_sort(arr):
    """
    Perform Bubble Sort on an array.

    This function sorts an array in ascending order using the Bubble Sort algorithm.
    It iteratively compares adjacent elements and swaps them if they are in the wrong order,
    ensuring that the largest unsorted element is moved to its correct position in each iteration.

    Parameters
    ----------
    arr : ndarray
        The numpy array to be sorted in place.

    Returns
    -------
    None
        The function sorts the array in place and returns nothing.
        """
    
    n = len(arr)
    # this loop is used as outer loop to check iteratively whether sorting is completed or not
    for i in range(n-1):
        # inner loop to swap adjacent elements
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_early_termination(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    # creating a list of random numbers
    np.random.seed(42)
    list1 = np.random.randint(1, 10, size=10000)
    print("Before sorting:\n", list1)
    

    start_time = time.time()
    # Sorting the list
    bubble_sort(list1)
    # bubble_sort_early_termination(list1)
    algo_run_time = time.time() - start_time

    print("List after Bubble sort:\n", list1)
    print(f"Completed in {algo_run_time}")

