# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# None -> 1 -> 2 -> 3 -> 4
#  prev   h
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    
    def reverse(self, head, prev):
        if not head:
            return prev
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

        self.reverse(head, prev)

