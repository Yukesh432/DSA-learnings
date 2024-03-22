import numpy as np

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
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
if __name__ == "__main__":
    # creating a list of random numbers
    list1 = np.random.randint(1, 10, size=5)
    print("Before sorting:\n", list1)
    
    # Sorting the list
    bubble_sort(list1)
    
    print("List after Bubble sort:\n", list1)

