
'''
Real brain-bender (🔥)

Given a list, return squares of even numbers that come immediately after an odd number.

nums = [1, 2, 4, 3, 6, 8, 5, 10]
# output: [4, 36, 100]


Explanation:

2 after 1

6 after 3

10 after 5

Rule:

map + filter

No loops

No list comprehension

'''
from typing import List
nums = [1, 2, 4, 3, 6, 8, 5, 10]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return(
            list(
                map(lambda x:x[1]**2,
                    filter(lambda x:True if x[0]%2!=0 and x[1]%2==0 else False,
                           zip(nums,nums[1:])))))

print(Solution().findDisappearedNumbers(nums))