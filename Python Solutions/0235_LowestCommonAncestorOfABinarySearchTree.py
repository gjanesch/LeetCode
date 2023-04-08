class Solution:
    """
    This solution was written in ignorance of the general properties of binary search trees, so it's pretty terrible.  It basically tries a breadth-first search to find the nodes, then cross-checks the lineages to find the first (deepest) overlap.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_lineage, q_lineage = [], []
        found_p, found_q = False, False
        node_lineage_pairs = [(root, [])]

        while not found_p:
            current_node, current_lineage = node_lineage_pairs.pop(0)
            new_lineage = current_lineage + [(current_node, current_node.val)]
            if p == current_node:
                p_lineage = new_lineage
                found_p = True
            else:
                if current_node.left is not None:
                    node_lineage_pairs.append((current_node.left, new_lineage))
                if current_node.right is not None:
                    node_lineage_pairs.append((current_node.right, new_lineage))
        print(p_lineage)

        node_lineage_pairs = [(root, [])]
        while not found_q:
            current_node, current_lineage = node_lineage_pairs.pop(0)
            new_lineage = current_lineage + [(current_node, current_node.val)]
            if q == current_node:
                q_lineage = new_lineage
                found_q = True
            else:
                if current_node.left is not None:
                    node_lineage_pairs.append((current_node.left, new_lineage))
                if current_node.right is not None:
                    node_lineage_pairs.append((current_node.right, new_lineage))
        print(q_lineage)

        p_vals_list = [val for node, val in p_lineage][::-1]
        q_vals_list = [val for node, val in q_lineage][::-1]

        for x, y in zip(p_lineage[::-1], q_lineage[::-1]):
            if x[1] in q_vals_list:
                return x[0]
            if y[1] in p_vals_list:
                return y[0]

        return root
