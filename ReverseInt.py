'''
Level: Easy
Frequency: High
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
TODO: Retake this test pop and push approach
'''

class Solution:
    def reverseString(self, x: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity:O(n)
        if x >= 0:
            result = int(str(x)[::-1]) 
            return result if result < 2147483647 else 0
        else:
            result = -int(str(x)[-1:0:-1])
            return result if result > -2147483648 else 0 
    
    def reversePopPush(self, x: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity:O(n)
        rev = 0
        int_max = 2147483647
        int_min = -2147483648
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False
        while x != 0 :
            
            pop = x % 10
            x = int(x / 10)
            rev = rev * 10 + pop
            if (rev > int_max and not neg) or (rev > int_max + 1 and neg):
                return 0