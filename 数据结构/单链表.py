
# 反转单链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def add(head,listnode):
    cur = head.next
    head.next = listnode
    listnode.next = cur

def showAll(head):
    cur = head
    print(cur.val)
    while cur.next !=None:
        cur = cur.next
        print(cur.val)

class Solution:
    def ReverseList(self,pHead):
        if pHead is None:
            return pHead
        last = None # 指向上一节点
        while pHead:
            tmp = pHead.next #保存下一节点信息
            pHead.next = last #保存完next,就可以让pHead的nex指向last了
            last = pHead
            pHead = tmp
        return last

# 递归实现
# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         # write code here
#         if not pHead or not pHead.next:
#             return pHead
#         else:
#             newHead = self.ReverseList(pHead.next)
#             pHead.next.next=pHead
#             pHead.next=None
#             return newHead

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

add(l1,l2)
add(l2,l3)
add(l3,l4)
add(l2,l5)
showAll(l1)

s1= Solution()
r_l1 = s1.ReverseList(l1)

showAll(r_l1)




