"""
对于A和B两棵二叉树，判断B是不是A的子结构

约定空树不是任意一个树的子结构
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if (not pRoot1) or (not pRoot2):
            return False
        return self._isSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def _isSubtree(self, pRoot1, pRoot2):
        '''
        when find that pRoot2.val=node_pRoot1.val
        '''
        if not pRoot2:
            # reach leaf of B
            return True
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self._isSubtree(pRoot1.left, pRoot2.left) and self._isSubtree(pRoot1.right, pRoot2.right)