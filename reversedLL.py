# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


#https://www.youtube.com/watch?v=G0_I-ZF0S38
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      previous = None
      current = head
      while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
      return previous
