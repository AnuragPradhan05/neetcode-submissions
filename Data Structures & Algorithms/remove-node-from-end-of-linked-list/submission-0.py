# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head

        for i in range(n):
            if first is None:
                return None
            first = first.next

        # If first became None, remove head
        if first is None:
            return head.next

        second = head

        while first.next is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head