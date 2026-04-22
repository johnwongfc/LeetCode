class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time: o(n) worse case iterate over entire LL
# perfect use case for sentinel node as we are always removing first node
# iterate LL and attach even nodes
    # at each even node, check if node.val is odd, skip

def removeOddsAtOddsLL(head):
    sentinel = ListNode(-1, head)
    prev = sentinel
    curr = head
    Position = 1
    
    while curr:
        if Position % 2 == 1 and curr.val % 2 == 1:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next 
        Position += 1

    return sentinel.next

# test cases
# empty LL
# single node LL

def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1: Given example
head1 = list_to_linked([1, 2, 3, 7, 5, 2])
result1 = removeOddsAtOddsLL(head1)
assert linked_to_list(result1) == [2, 7, 2], f"Test 1 failed: {linked_to_list(result1)}"

# Test Case 2: Empty list
result2 = removeOddsAtOddsLL(None)
assert result2 is None, "Test 2 failed"

# Test Case 3: Single odd element (removed)
head3 = list_to_linked([5])
result3 = removeOddsAtOddsLL(head3)
assert linked_to_list(result3) == [], f"Test 3 failed: {linked_to_list(result3)}"

# Test Case 4: Single even element (kept)
head4 = list_to_linked([4])
result4 = removeOddsAtOddsLL(head4)
assert linked_to_list(result4) == [4], f"Test 4 failed: {linked_to_list(result4)}"

# Test Case 5: All even numbers (no removals)
head5 = list_to_linked([2, 4, 6, 8])
result5 = removeOddsAtOddsLL(head5)
assert linked_to_list(result5) == [2, 4, 6, 8], f"Test 5 failed: {linked_to_list(result5)}"

# Test Case 6: All odd numbers
head6 = list_to_linked([1, 3, 5, 7])
result6 = removeOddsAtOddsLL(head6)
assert linked_to_list(result6) == [3, 7], f"Test 6 failed: {linked_to_list(result6)}"

# Test Case 7: Odd numbers only at even positions (no removals)
head7 = list_to_linked([2, 1, 4, 3, 6, 5])
result7 = removeOddsAtOddsLL(head7)
assert linked_to_list(result7) == [2, 1, 4, 3, 6, 5], f"Test 7 failed: {linked_to_list(result7)}"

print("All tests passed!")
