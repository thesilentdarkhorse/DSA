
'''
Return all positive even numbers.

nums = [-3, 4, 7, -2, 6, 1]
# output: [4, 6]


Rule: filter + lambda only.

'''
from typing import List
nums = [-3, 4, 7, -2, 6, 1]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return(list(filter(lambda x: True if x>0 and x%2==0 else False,nums)))

print(Solution().findDisappearedNumbers(nums))