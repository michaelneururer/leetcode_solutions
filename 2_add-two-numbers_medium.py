# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2, i = 0, 0, 0
        while l1:
            s1 += 10**i * l1.val
            l1 = l1.next
            i+=1
        i = 0
        while l2:
            s2 += 10**i * l2.val
            l2 = l2.next
            i+=1

        l1pl2 = s1 + s2
        res = tmp = ListNode(0)
        for i in range(len(str(l1pl2))):
            tmp.next = ListNode(l1pl2%10)
            l1pl2 = l1pl2//10
            tmp = tmp.next
        return res.next
