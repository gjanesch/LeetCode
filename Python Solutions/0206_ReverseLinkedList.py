class Solution:
    """
    Basically just iterates over the given linked list, and then keeps
    constructing the backwards list by continually nesting the backward
    list in a new element.

    A little poking around showed that there are better (faster and
    less memory-intensive) solutions using the properties of linked
    lists better, but at this point in time, I'm still not used to
    them.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        forward, backward = head, None
        while forward is not None:
            backward = ListNode(forward.val, backward)
            forward = forward.next
        return backward

