'''
You are given a string s containing only lowercase English letters.

Remove all adjacent duplicate characters using a stack.
Repeat the process until no duplicates remain.

Example:
Input: s = "abbaca"
Output: "ca"
'''


from typing import List
s = "abbaca"
class Solution:
    def evalRPN(self, s: List[str]) -> int:
        stack=[]
        stack.append(s[0])
        print(stack)
        for x in s[1:]:
            if x != stack[-1]:
                stack.append(x)
            else:
                stack.pop()
        return("".join(stack))
                


print(Solution().evalRPN(s))



