# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#https://leetcode.com/problems/middle-of-the-linked-list/solutions/1651600/python-java-c-simple-solution-one-pass-beginner-friendly-detailed-explanation/
class Solution:
    def middleNode(self, head: Optional[ListNode]):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow