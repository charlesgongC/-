# 二叉搜索树，左子数比父节点小，右子数比父节点大

class TreeNode(object):
    def __init__(self,left=None,right=None,value=None):
        self.value = value
        self.left = left
        self.right = right

    def getCommonAncestor(root,node1,node2):
        while root:
            if root.data > node1.data and root.data > node2.data:
                root = root.left
            elif root.data < node1.data and root.data < node2.data:
                root = root.right
            else:
                return root
        return None
