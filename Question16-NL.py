
'''
Filter → Map chain

Square only odd numbers.

nums = [1, 2, 3, 4, 5]
# output: [1, 9, 25]


Rule:

No list comprehension

filter then map

'''
from typing import List
nums = [1, 2, 3, 4, 5]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return(list(map(lambda x:x**2,filter(lambda x:x%2!=0,nums))))

print(Solution().findDisappearedNumbers(nums))