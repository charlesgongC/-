class Stack(object):

    def __init__(self):
        self.pTop = None
        self.pBottom = None

class Node(object):

    def __init__(self,data=None,pNext = None):
        self.data = data
        self.pNext = pNext

def push(s,new):
    new.pNext = s.pTop
    s.pTop = new

def pop(s):
    cur = s.pTop
    while cur != s.pBottom:
        s.pTop = cur.pNext
        print("出栈的元素是：%d"%cur.data)
        cur = cur.pNext
    else:
        print("出栈结束")

def getAll(s):
    cur = s.pTop
    while cur != s.pBottom:
        print(cur.data)
        cur = cur.pNext

head = Node()

s = Stack()

s.pTop = s.pBottom = head

n1 = Node(1)
push(s,n1)

n2 = Node(3)
push(s,n2)

n3 = Node(5)
push(s,n3)

pop(s)