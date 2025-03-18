# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        old = []
        cur = head

        while cur:
            old.append(cur)
            cur = cur.next

        print("we need to skip", old[-n].val)
        removeIndex = len(old)-n

        if removeIndex == 0:
            return head.next

        else:
            old[removeIndex-1].next = old[removeIndex].next

        return head