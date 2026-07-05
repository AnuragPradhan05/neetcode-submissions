# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        
        t1 = l1
        t2 = l2
        carry = 0

        while (t1 or t2) or carry:

            x = t1.val if t1 else 0
            y = t2.val if t2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10  

            new_node = ListNode(digit)
            temp.next = new_node
            temp = temp.next
            if t1:
                t1 = t1.next

            if t2:
                t2 = t2.next

        return dummy.next

        
