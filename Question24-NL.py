'''
You are given a string s consisting of characters '(', ')', '{', '}', '[' and ']'.

You have an empty stack.

Determine if the input string is valid.

A string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket.

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "(]"
Output: False
'''


from typing import List
s = "()"
class Solution:
    def evalRPN(self, s: List[str]) -> int:
        stack=[]
        for x in s:
            try:
                if x in ("{","(","["):
                    stack.append(x)
                else:
                    stack.pop()
                return(len(stack)==0)
            except:
                return(False)


print(Solution().evalRPN(s))



