# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def MirrorRec(self, root):
        # write code here
        if not root:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            self.MirrorRec(root.left)
        if root.right:
            self.MirrorRec(root.right)

