"""
Given two sorted arrays `nums1` and `nums2`, find the median value 
as if they were merged into a single sorted array.

The median is the element that separates the two halves of a sorted 
dataset, where one half is less than or equal to the median and the 
other half is greater than or equal to the median. 

This function aims to find this median value efficiently without 
modifying the original arrays.

**Example:**

Consider arrays `nums1 = [1, 3]` and `nums2 = [2]`. 

If we merge them, we get `[1, 2, 3]`. The median in this case is the 
middle element, which is 2.
"""
import numpy as np

a= [20, 30, 40, 50]
b= [3, 5, 7, 9]

merged_array= a+b
print("The merged unsorted array is ::" , merged_array)

print("The merged sorted array is:: ", sorted(merged_array))

result= np.median(merged_array)
print('THe median of the sorted array is:: ', result)