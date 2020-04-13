import math
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        x = self
        L = []
        while x:
            L.append(x.val)
            x = x.next
        return(str(L))

class Solution:
    def __init__(self):
        pass

    def swapPairs(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            first = curr.val
            second = curr.next.val
            curr.val = second
            curr.next.val = first
            curr = curr.next.next
        return head



#Testing
s = Solution()
L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(3)
L1.next.next.next = ListNode(4)
print(s.swapPairs(L1))
