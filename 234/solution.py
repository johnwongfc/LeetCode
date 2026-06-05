# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        def reverse_helper(head):
            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_head = reverse_helper(slow)

        curr = head
        while curr:
            if curr.val != second_head.val:
                return False
            curr = curr.next
            second_head = second_head.next

        return True
