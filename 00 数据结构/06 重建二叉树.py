# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        preLen = len(pre)
        tinLen = len(tin)
        if preLen <= 0 or tinLen <= 0 or preLen != tinLen:
            return None
        orderLen = preLen

        root = TreeNode(pre[0])
        rootInd = tin.index(root.val)
        if rootInd != 0:
            # has left
            tinLeft = tin[0:rootInd]
            preLeft = pre[1:rootInd+1]
            # note: self.
            root.left = self.reConstructBinaryTree(preLeft, tinLeft)
        if rootInd != orderLen-1:
            # has right
            tinRight = tin[rootInd+1:]
            preRight = pre[rootInd+1:]
            root.right = self.reConstructBinaryTree(preRight, tinRight)
        return root

        # the fastest solution
        def reConstructBinaryTreeTop(self, pre, tin):
            # write code here
            if len(pre) == 0:
                return None
            if len(pre) == 1:
                return TreeNode(pre[0])
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTreeTop(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTreeTop(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
            return flag 
