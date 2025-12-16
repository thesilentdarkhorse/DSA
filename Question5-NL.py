
'''
Q2.
Find the largest and smallest element in a list without using min() or max().

nums = [4, 2, 9, 1, 7]
# output: max=9, min=1
'''

import sys
from typing import List
nums = [4, 2, 9, 1, 7]
def Solution(nums:List[int]):
    small = nums[0]
    big = nums[0]
    for x in nums:
        if x<=small:
            small = x
        if x>=big:
            big=x
    return(small,big)

print(Solution(nums))