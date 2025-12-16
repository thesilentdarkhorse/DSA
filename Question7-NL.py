
'''
Two-pointer thinking

Q4.
Reverse a list in-place (no slicing, no extra list).

nums = [1, 2, 3, 4, 5]
# output: [5, 4, 3, 2, 1]
'''

import sys
from typing import List
nums = [1, 2, 3, 4, 5,6]
def Solution(nums:List[int]):
    for x in range(len(nums)//2):
        temp = nums[x]
        nums[x]=nums[len(nums)-1-x]
        nums[len(nums)-1-x]=temp
    return(nums)

print(Solution(nums))