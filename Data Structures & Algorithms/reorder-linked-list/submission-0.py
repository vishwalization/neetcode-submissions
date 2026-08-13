# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        prev, cur = None, slow
        while cur: 
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp

        # "prev" holds the last node    
        first, second = head, prev
        while second.next:
            temp1 = first.next
            temp2 = second.next 

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        

         

        