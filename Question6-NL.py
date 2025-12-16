
'''
Q3.
Count how many times each element appears and return a dictionary.

nums = [1, 2, 2, 3, 1, 1]
# output: {1: 3, 2: 2, 3: 1}
'''
import sys
from typing import List
nums = [1, 2, 2, 3, 1, 1]
def Solution(nums:List[int]):
    lst = [[n, 0] for n in list(set(nums))]
    for x in nums:
        lst[x-1][1]+=1
    return lst
print(Solution(nums))
