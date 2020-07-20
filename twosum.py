'''
Level: Easy
Frequency: Very High
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        # Run-Time O(n^2)
        # Memory O(1)
        N = len(nums)
        
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def twoSumTwoHash(self, nums: List[int], target: int) -> List[int]:
        # Run-Time O(n)
        # Memory (n)
        d = {}
        N = len(nums)
        for i in range(N):
            d[nums[i]] = i
            
        for i in range(N):
            complement = target - nums[i]
            if complement in d.keys() and d[complement] != i:
                return[i, d[complement]]
        d = {}
        N = len(nums)
        for i in range(N):
            d[nums[i]] = i
            
        for i in range(N):
            complement = target - nums[i]
            if complement in d.keys() and d[complement] != i:
                return[i, d[complement]]

    def twoSumOneHash(self, nums: List[int], target: int) -> List[int]:
        # Run-Time O(n)
        # Memory (n)
        d = {}
        N = len(nums)
        
        for i in range(N):
            complement = target - nums[i]
            if complement in d.keys() and d[complement] != i:
                return [i, d[complement]]
            
            d[nums[i]] = i