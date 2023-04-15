class Solution:
    # A recursive solution, which uses an auxiliary function to get
    # around the fact that the main function can only return a boolean
    # value.  The auxiliary function is meant to return a tuple of
    # whether the tree is known to be unbalanced and the node's depth
    # (though if we know it's unbalanced below the current node, we
    # return -1 since we no longer care about the depth). The
    # conditions inside the top-level else clause in get_depth() were
    # originally a bit more lengthy, but checking ldepth[0] and
    # rdepth[0] upfront seems to save some computation time.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_depth(node):
            if not node:
                return (True, 0)
            else:
                ldepth = get_depth(node.left)
                rdepth = get_depth(node.right)
                if ldepth[0] and rdepth[0]:
                    return ((ldepth[1] - rdepth[1]) in [-1, 0, 1], 1 + max(ldepth[1], rdepth[1]))
                else:
                    return (False, -1)

        return get_depth(root)[0]
