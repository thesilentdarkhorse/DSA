
'''
2️⃣ Map only

Square every number.

nums = [1, 2, 3, 4]
# output: [1, 4, 9, 16]


Rule: map + lambda only.

'''
from typing import List
nums = [1, 2, 3, 4]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return(list(map(lambda x:x**2,nums)))

print(Solution().findDisappearedNumbers(nums))