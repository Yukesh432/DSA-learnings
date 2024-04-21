import numpy as np
import random

list1= np.random.randint(1,10, 7)
list2= np.random.randint(1,10, 7)
# result= []

def merge_sort(left, right):
    #if the first array is empty do nothing and pass simply the second array as the result
    if(len(left)==0):
        return right
    # similarly, if the 2nd array is empty , return the 1st array as it is
    if(len(right)==0):
        return left
    
    result= []
    left_index, right_index= 0
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
            result.append(left[left_index:])
            break

        if left_index== len(left):
            result.append(right[right_index:])
            break
    return result



