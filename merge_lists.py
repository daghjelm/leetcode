# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

    start = ListNode()
    node = start
    y, y, y

    while l1 and l2:
      val = None

      if l1.val < l2.val:
        node.next = l1
        l1 = l1.next
      else:
        node.next = l2
        l2 = l2.next

      node = node.next

    node.next = l1 or l2

    return start.next

  #recursive solution
  def mergeRec(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not (l1 and l2):
      return l1 or l2
    if l1.val < l2.val:
      l1.next = self.mergeRec(l1.next, l2)
      return l1
    else:
      l2.next = self.mergeRec(l1, l2.next)
      return l2
