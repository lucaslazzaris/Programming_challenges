'''
Level: Medium
Frequency: High
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Note: Nice to remember linked lists
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbersGenericSolution(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time Complexity: O(max(n, m))
        # Space Complexity: O(max(n, m))
        v1 = 0
        v2 = 0
        n1 = l1
        n2 = l2
        p1 = 1
        p2 = 1
        while n1 is not None:
            v1 += n1.val * p1
            n1 = n1.next
            p1 *= 10
        while n2 is not None:
            v2 += n2.val * p2
            n2 = n2.next
            p2 *= 10            
        v = v1 + v2
        v = str(v)
        
        node = ListNode(int(v[0]), None)
        
        for letter in v[1:]:
            node = ListNode(int(letter), node)
        
        return node

        def addTwoNumbersOnlineSolution(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time Complexity: O(max(n, m))
        # Space Complexity: O(max(n, m))    
        dummyHead = ListNode()
        carry = 0
        current = dummyHead
        while l1 is not None or l2 is not None:
            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0
            s = x1 + x2 + carry
            carry = s // 10
            current.next = ListNode(s % 10)
            
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        return dummyHead.next