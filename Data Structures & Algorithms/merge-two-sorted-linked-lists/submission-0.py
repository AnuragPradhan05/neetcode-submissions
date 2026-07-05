# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, curr1: Optional[ListNode], curr2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        curr1 = curr1
        curr2 = curr2
        temp = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1
                curr1 = curr1.next

            else:
                temp.next = curr2
                curr2 = curr2.next

            temp = temp.next

        if curr1:
            temp.next = curr1
        else:
            temp.next = curr2

        return dummy.next

