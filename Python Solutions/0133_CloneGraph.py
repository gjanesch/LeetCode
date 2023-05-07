class Solution:
    """
    Essentially just iterates over nodes, and while there are any we
    haven't looked at yet, get information from those and see if they
    link to anything else we haven't looked at yet.
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        node_queue = [node]
        new_nodes = {node.val: Node(node.val, [])}
        while node_queue:
            current_node = node_queue.pop(0)
            current_new_node = new_nodes[current_node.val]
            for n in current_node.neighbors:
                if n.val not in new_nodes:
                    new_nodes[n.val] = Node(n.val, [])
                    node_queue.append(n)
                current_new_node.neighbors.append(new_nodes[n.val])

        return new_nodes[node.val]
