# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l = []
        dummy = head
        while dummy != None:
            l.append(dummy.val)            
            dummy = dummy.next

        if not l:
            return None

        head = dummy = ListNode()
        for i in l[:0:-1]:
            dummy.val = i
            dummy.next = ListNode()
            dummy = dummy.next
        dummy.val = l[::-1][-1]

        return head