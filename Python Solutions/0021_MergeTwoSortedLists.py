class Solution:
    # This is just a bad, lazy solution that essentially "undoes" the
    # linking to make them flat, merge them, and then relink.
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2:
                return None
            else:
                return list2
        elif not list2:
            return list1
        else:
            l1, l2 = list1, list2
            l1_flat, l2_flat = [], []
            while l1:
                l1_flat.append(l1.val)
                l1 = l1.next
            while l2:
                l2_flat.append(l2.val)
                l2 = l2.next
            l1_flat.extend(l2_flat)
            sorted_list = sorted(l1_flat)[::-1]

            merged_list = ListNode(sorted_list.pop(0), None)
            for item in sorted_list:
                merged_list = ListNode(item, merged_list)
            return merged_list
