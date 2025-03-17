# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        pointerList1 = list1
        pointerList2 = list2

        output_list = ListNode() #remember to remove the first node
        cur_positon = output_list

        while pointerList1 or pointerList2:
            if pointerList1 and pointerList2:
                if pointerList1.val <= pointerList2.val:
                    cur_positon.next = ListNode(val=pointerList1.val)
                    pointerList1 = pointerList1.next
                else:
                    cur_positon.next = ListNode(val=pointerList2.val)
                    pointerList2 = pointerList2.next

            elif pointerList1:
                #only list1
                cur_positon.next = ListNode(val=pointerList1.val)
                pointerList1 = pointerList1.next

            else:
                # only list 2
                cur_positon.next = ListNode(val=pointerList2.val)
                pointerList2 = pointerList2.next

            cur_positon = cur_positon.next
        
        return output_list.next



        