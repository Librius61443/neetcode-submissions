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

        second = slow.next
        slow.next = None

        newHead = None
        while second:
            temp = second
            second = second.next
            temp.next = newHead
            newHead = temp

        cur = head
        while newHead:
            temp1 = cur.next
            temp2 = newHead.next

            cur.next = newHead
            newHead.next = temp1

            cur = temp1
            newHead = temp2


        
