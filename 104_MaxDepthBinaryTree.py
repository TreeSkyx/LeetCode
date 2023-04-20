"""
        :type root: TreeNode
        :rtype: int
"""
def maxDepth(self, root):
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0