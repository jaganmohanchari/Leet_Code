#LEET CODE QUESTION 7


'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

#Solution

class Solution:
    def reverse(self, x: int) -> int:
        string=str(x)
        c=abs(x)
        a=list(str(c))
        if 0 in a:
            a.remove(0)
        res=a[::-1]
        result=""
        for i in res:
            result=result+str(i)+""
        if "-" in string:
            result="-"+result
        result=int(result)
        if result> -2**31 and result < (2**31)-1 :
            return result
        return 0        

