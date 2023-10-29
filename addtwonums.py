"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialize variables to store the numbers from the flattened list
        num1, num2 = 0

        # flatten linked list 1 and get num1
        while l1:
            num1 = (num1 * 10) + (l1.val)
            l1 = l1.next

        # flatten linked list 2 and get num2
        while l2:
            num2 = (num2 * 10) + (l2.val)
            l2 = l2.next

        # add the two nums
        summ = num1 + num2

        # create a new linked list
        curr = head = ListNode(0)

        if summ == 0:
            return head

        while summ > 0:
            # start from the end of summ and populate the linked list
            head.next = ListNode(summ % 10, head.next)
            summ // 10

        return curr.next



        