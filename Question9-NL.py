
'''
Q6.
Given a list and an integer k, find the maximum sum of any contiguous subarray of size k.

nums = [2, 1, 5, 1, 3, 2]
k = 3
# output: 9  (subarray [5,1,3])
'''

import sys
from typing import List
nums = [2, 1, 5, 1, 3, 2]
k = 3
def Solution(nums:List[int],k:int):
    return(max([(nums[x:x+k],sum(nums[x:x+k])) for x in range(len(nums))],key=lambda x:x[1]))

print(Solution(nums,k))