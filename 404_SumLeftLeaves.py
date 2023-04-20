"""
        :type root: TreeNode
        :rtype: int
"""

def sumOfLeftLeaves(self, root):
    if root != None:
        if (root.left != None):
            if (root.left.left == None and root.left.right == None):
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        elif root.right != None:
            return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        else:
            return 0
    else:
        return 0
