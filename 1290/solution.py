# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        curr = head

        while curr:
            val = curr.val
            res = (res * 2) + val
            # bitwise 
            # res = (res << 1) | val
            curr = curr.next

        return res