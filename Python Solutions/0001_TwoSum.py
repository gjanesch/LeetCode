class Solution:
    # This is a fairly crude solution.  The thinking was:
    # 1. Sort it. (Didn't know that LeetCode offers the sortedcontainers
    #    library, so I didn't try to do anything with that.)
    # 2. For each value in the list:
    #   - Calculate the other value needed to get the sum.
    #   - If it's equal to the current value, check the adjacent elements
    #     to see if one of those is equal, and return the indices if so.
    #   - If not, just brute-force check if the other value is in the list.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(i, value) for i, value in enumerate(nums)]
        sorted_nums = sorted(indexed_nums, key=lambda x: x[1])
        sorted_indices = [n[0] for n in sorted_nums]
        sorted_values = [n[1] for n in sorted_nums]
        for i, x in enumerate(sorted_values):
            needed_value = target - x
            if needed_value == x:
                if i == 0 and sorted_values[1] == needed_value:
                    return [sorted_indices[0], sorted_indices[1]]
                elif i == len(sorted_values)-1 and sorted_values[i-1] == needed_value:
                    return [sorted_indices[i-1], sorted_indices[i]]
                elif sorted_values[i-1] == needed_value:
                    return [sorted_indices[i-1], sorted_indices[i]]
                elif sorted_values[i+1] == needed_value:
                    return [sorted_indices[i], sorted_indices[i+1]]
            elif needed_value in sorted_values:
                return [sorted_indices[i], sorted_indices[sorted_values.index(needed_value)]]
        return None
