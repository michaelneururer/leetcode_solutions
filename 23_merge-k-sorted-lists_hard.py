import math
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        pass

    def mergeKLists(self, lists) -> ListNode:
        head = ListNode(0)
        res = head
        heap = []
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i))
                l = l.next
        while heap:
            min_val, i = heapq.heappop(heap)
            head.next = lists[i]
            head = head.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i))
        return res.next




"""
Testing
s = Solution()
L1 = ListNode(1)
L1.next = ListNode(4)
L1.next.next = ListNode(5)
L2 = ListNode(1)
L2.next = ListNode(3)
L2.next.next = ListNode(4)
L3 = ListNode(2)
L3.next = ListNode(6)
print(s.mergeKLists([L1,L2,L3]).next.next.next.next.next.next.val)
"""
