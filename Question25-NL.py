'''
You are given a string s.

You can use a stack and the following operation:
- Pop the top character from the stack.

Reverse the string and return it.

Example:
Input: s = "stack"
Output: "kcats"
'''


from typing import List
s = "stack"
class Solution:
    def evalRPN(self, s: List[str]) -> int:
        ans=""
        stack=[]
        for x in s:
            # print(x)
            stack.append(x)
        while(len(stack)!=0):
            ans +=stack.pop()
        return(ans)


print(Solution().evalRPN(s))



