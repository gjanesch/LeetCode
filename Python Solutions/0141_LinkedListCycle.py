class Solution:
    # Keeps track of two separate points in the list, one which
    # advances twice as fast as thet other.  If there's a cycle,
    # eventually they'll end up at the same node; if not, the faster
    # one will run into the end at some point.
    #
    # The only real difference between the two solutions is that the
    # second is more terse -- it was actually marginally slower in one
    # run.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        elif head.next is None:
            return False
        else:
            node1 = head
            node2 = head
            while True:
                node1 = node1.next
                node2 = node2.next
                if node2.next is None:
                    return False
                else:
                    node2 = node2.next
                    if node2.next is None:
                        return False
                    elif node1 == node2:
                        return True
        """
        node1 = head
        node2 = head
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                return True
        return False
        """
