
'''
Array compression (logic-heavy)

Q6.
Compress consecutive duplicates.

nums = [1,1,1,2,2,3,1,1]
# output: [(1,3), (2,2), (3,1), (1,2)]

'''

import sys
from typing import List
nums = [1,1,1,2,2,3,1,1]
def Solution(nums:List[int]):
    nums.append(0)
    ans = [nums[x] - nums[x+1] for x in range(len(nums)-1)]
    ans1=[]
    add =0
    # print(ans)
    for x in range(len(ans)):
        if ans[x]!=0:
            # print(ans[x])
            ans1.append([nums[x],x+1-add])
            add = x +1
    return(ans1)

print(Solution(nums))