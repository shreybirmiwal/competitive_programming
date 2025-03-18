# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        sPoint = head
        fPoint = head.next

        while fPoint and fPoint.next:
            sPoint = sPoint.next
            fPoint = fPoint.next.next

        second_half = sPoint.next
        sPoint.next = None




        #6->8
        prev = None
        cur = second_half
        while cur:
            oldNext = cur.next #8, none
            cur.next = prev #none, 6

            #move pointers
            prev = cur #6, 8
            cur = oldNext #8, None

        #start w prev now
       
        
        x = head
        while x:
            print(x.val)
            x = x.next

        print("now on second half")
                    
        x = prev
        while x:
            print(x.val)
            x = x.next

        #2->4->8->6

        # this our new last node
        #now we gotta make our final output

        finalOut = ListNode() #remember to remove the first element

        lPointer = head
        rPointer = prev

        while lPointer and rPointer:
            old_rightPointer_next = rPointer.next
            next_t = lPointer.next
            lPointer.next = rPointer
            rPointer.next = next_t

            lPointer = rPointer.next
            rPointer = old_rightPointer_next
            print("new pointer", lPointer)

            print("printing r 1 $#######")
            x = head
            while x:
                print(x.val)
                x = x.next




#2 4 6 8 10
#2 10 4 8 6


