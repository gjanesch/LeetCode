class Solution:
    # A pretty standard recursion solution.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            left_inverted = self.invertTree(root.left)
            right_inverted = self.invertTree(root.right)
            return TreeNode(root.val, right_inverted, left_inverted)
