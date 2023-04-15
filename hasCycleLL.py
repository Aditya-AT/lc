# best slution
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional) -> bool:
        visit = set()
        curr = head

        while curr:
            if curr in visit:
                return True
            visit.add(curr)
            curr = curr.next
        return False


class Solution:
    def hasCycle(self, head: Optional) -> bool:
        if head == None:
            return False
        temp = []
        while head.val not in temp:
            temp.append(head.val)
            res = True
            head.val = head.next
            if head.next == None:
                return False
            head.next = head.next.next
        return res