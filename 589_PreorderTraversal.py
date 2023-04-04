"""
    589. N-ary Tree Preorder Traversal
    Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value

    :type root: Node
    :rtype: List[int]

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def preorder(self, root):
    result = []
    self.traverse(root, result)
    return result
def traverse(self, root, result):
    if root is None: return
    result.append(root.val)
    for child in root.children:
        self.traverse(child, result)
