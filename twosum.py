"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
# def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         num_list= nums
#         target= target
#         # iterate through the list of numbers
#         for i in range(len(num_list)):
#             # iterate through the list starting from the next element after nums[i]
#             for j in range(i+1, len(num_list)):
#                 # creating a combination tuple of indices (i, j)
#                 combination= (i, j)
#                 # create a tuple of values from nums at indices i and j
#                 valuess= (num_list[i], num_list[j])

#                 # check if the sum of two values equals the target
#                 if sum(valuess)== target:
#                     print(combination)
           
#  # calling the function          
# twoSum([2,7,11,15], 9)

# def twosum(arr, targett):
#     for i in (arr):
#         print(arr[i])
#         # if arr[i]+ arr[i-1]== targett:
#         #     print(arr[i], arr[i-1])


arr= [10,20,39,49,58]
targett= 7
# twosum(arr, targett)


for i in (arr):
    print(arr[i-1])
    print("//////////////////")
    print(i)
    print(".............................")
    print("..")