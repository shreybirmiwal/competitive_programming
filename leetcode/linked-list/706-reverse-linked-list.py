# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head
        # 1 -> 2 -> 3 -> 4
        # null <- 1
        # 1 <- 2
        # 2 <- 3
        # 3 <- 4

        while cur:
            old_next = cur.next
            cur.next = prev
            #moving pointers
            prev = cur
            cur = old_next
        
        return prev

      