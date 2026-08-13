# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        cur = list1
        while cur:
            l.append(cur.val)
            cur = cur.next
        
        cur = list2
        while cur:
            l.append(cur.val)
            cur = cur.next

        if not l:
            return None
            
        l.sort()
        cur = head = ListNode()
        for i in l[:-1]:
            cur.val = i
            cur.next = ListNode()
            cur = cur.next
        cur.val = l[-1]

        return head