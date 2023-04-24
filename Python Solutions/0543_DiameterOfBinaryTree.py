class Solution:
    """
    A recursive solution.  It scores rather poorly on the site, though,
    and I'm not quite sure why -- part of it seems to be that more
    optimal Python solutions get away with tracking just the depth and
    storing a variable as part of the class instead of inside the
    function.
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth_and_diameter(root):
            if not root:
                return 0, 0
            left_depth, left_diameter = depth_and_diameter(root.left)
            right_depth, right_diameter = depth_and_diameter(root.right)

            depth = 1 + max(left_depth, right_depth)
            diameter = max(left_diameter, right_diameter, left_depth + right_depth)

            return depth, diameter
        
        return depth_and_diameter(root)[1]
