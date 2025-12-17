
'''
Add elements of two lists index-wise.

a = [1, 2, 3]
b = [4, 5, 6]
# output: [5, 7, 9]


Rule:

map

One lambda

Use multiple iterables

'''
from typing import List
a = [1, 2, 3]
b = [4, 5, 6]
class Solution:
    def findDisappearedNumbers(self, nums: List[int],nums_: List[int]) -> List[int]:
        return(list(map(lambda x,y:x+y,a,b)))

print(Solution().findDisappearedNumbers(a,b))