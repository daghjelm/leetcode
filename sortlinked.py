# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Given the head of a sorted linked list,\
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
# ex [1,1,2] -> [1,2]
# [1,1,2,3,3] -> [1,2,3]
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if head == None:
            return head

        start = head
        last = ListNode(None)
        while head.next:
            if head.val == last.val:
                last.next = head.next
            else:
                last = head
            head = head.next

        if head.val == last.val:
            last.next = None

        return start

def print_list(head):
    current = head
    while head.next:
        print(head.val)
        head = head.next
    print(head.val)

def main():
    # a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3))))))
    a = ListNode(1, ListNode(1, ListNode(2)))
    s = Solution()
    s.deleteDuplicates(a)
    print_list(a)

main()



