class Solution:
    """
    Recursive solution that relies on zip_longest (from the itertools
    library) to keep the lists of node values the same.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left_path = self.levelOrder(root.left)
        right_path = self.levelOrder(root.right)
        combined = [x + y for x, y in zip_longest(left_path, right_path, fillvalue=[])]
        return [[root.val]] + combined
