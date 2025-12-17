
'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

'''
from typing import List
from collections import Counter
nums = [1,2,2,4]
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        y = [x for x, c in Counter(nums).items() if c > 1]
        nums.remove(y[0])
        x = (n*(n+1))/2
        return([y[0],int(x-sum(nums))])

print(Solution(nums))