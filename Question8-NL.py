
'''
Filtering + transformation

Q5.
Create a new list containing squares of even numbers only.

nums = [1, 2, 3, 4, 5, 6]
# output: [4, 16, 36]
'''

import sys
from typing import List
nums = [1, 2, 3, 4, 5, 6]
def Solution(nums:List[int]):
    return([x**2 for x in nums if x % 2 == 0])

print(Solution(nums))