
'''
6️⃣ Filter with index (tricky)

Keep elements that are greater than their index.

nums = [0, 2, 1, 4, 3]
# output: [2, 4]


Rule:

filter

Use enumerate

'''
from typing import List
nums = [0, 2, 1, 4, 3]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums=list(enumerate(nums))
        return(list(filter(lambda x:x[1]>x[0],nums)))

print(Solution().findDisappearedNumbers(nums))