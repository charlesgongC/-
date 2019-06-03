# 非递归实现
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self,pHead):
        if pHead is None:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            pHead = tmp
        return last

# 递归实现
class Solution:
    def ReverseList(self,pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return newHead
