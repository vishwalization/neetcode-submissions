# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

        # # first attempt
        # # copy the values to a list
        # l = []
        # dummy = head
        # while dummy != None:
        #     l.append(dummy.val)            
        #     dummy = dummy.next

        # # if list is empty return NONE
        # if not l:
        #     return None

        # # create a linked list "save the head" with dummy
        # head = dummy = ListNode()
        # for i in l[:0:-1]:
        #     dummy.val = i
        #     dummy.next = ListNode()
        #     dummy = dummy.next
        # dummy.val = l[::-1][-1]

        # return head