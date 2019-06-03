import re
pts=[]


# 落子后加入落子列表
def add_line(chess):
    if chess in pts:
        print("已存在")
        return pts

    if not re.findall('([A-T][0-1][0-9])|([A-T][0-9])',chess):
        print('格式不正确')

        return pts
    pts.append(chess)
    return pts

# # 检测列表
# def check_line(pts):
#     # 五步以后开始检索
#     if len(pts) < 5:
#         return None
#
#     try:
#         # 获取最近白或黑的三步
#         one,two,tree = pts[-5:len(pts):2]
#         # 第一步
#         one_x = ord(one[0])
#         one_y = eval(one[1:])
#
#         # 第二步
#         two_x = ord(two[0])
#         two_y = eval(two[1:])
#
#         # 第三步
#         tree_x = ord(tree[0] )
#         tree_y = eval(tree[1:])
#
#         # x轴相等，检测y轴三步是否间距是否相同
#         if one_x == two_x == tree_x and tree_y - two_y == two_y - one_y:
#             # 检测是否相邻
#             if abs(tree_y - two_y) == 1:
#                 return True
#
#         # y轴相等，检测x轴三步是否间距是否相同
#         if tree_y == two_y == one_y and one_x - two_x == two_x - tree_x:
#             if abs(one_x - two_x) == 1:
#                 return True
#     except Exception as e:
#         print(e)

# 检测所有

def check_line(pts):
    # 列表长度操过5开始检测
    if len(pts) < 5:
        return None
    for i in range(len(pts)-4):
        # 获取黑或白连续三步进行匹配
        one,two,tree,*_=pts[i::2]

        # 第一步，分离x y 轴
        one_x = ord(one[0])
        one_y = eval(one[1:])

        # 第二步
        two_x = ord(two[0])
        two_y = eval(two[1:])

        # 第三步
        tree_x = ord(tree[0])
        tree_y = eval(tree[1:])

        if one_x == two_x == tree_x and tree_y - two_y == two_y - one_y:
            # 检测是否相邻
            if abs(tree_y - two_y) == 1:
                return True

        # y轴相等，检测x轴三步是否间距是否相同
        if tree_y == two_y == one_y and one_x - two_x == two_x - tree_x:
            if abs(one_x - two_x) == 1:
                return True


# if __name__== "__main__":
#     temp = None
#     while not temp:
#         chess = input("请落子：")
#         add_line(chess)
#         temp = check_line(pts)

def reverse(x):
    if x>0:
        return int(str(x)[::-1])
    else:
        x = 0-x
        return -int(str(x)[::-1])

# print(reverse(-120))

# print(ord('a'),ord('z'),False)
# print([1,2] is list

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList

    def next(self):
        """
        :rtype: int
        """
        for j in self.nestedList:
            yield j

    def hasNext(self):
        """
        :rtype: bool
        """
        if type(self.nestedList) is list:
            return True
        else:
            return False

nestedList=[[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
    print(v)
