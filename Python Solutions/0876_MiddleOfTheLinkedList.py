class Solution:
    """
    Basic two-pointer appoach, ordering the operations of movement so
    that the slower node is always at the halfway point.
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head

        while head.next:
            slow = slow.next
            head = head.next
            if head.next:
                head = head.next
        
        return slow
