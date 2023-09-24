"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_list= nums
        target= target
        # iterate through the list of numbers
        for i in range(len(num_list)):
            for j in range(i+1, len(num_list)):
                combination= (i, j)
                valuess= (num_list[i], num_list[j])
                
                if sum(valuess)== target:
                    print(combination)
           
           
twoSum([2,7,11,15], 9)