class Solution:
    # Standard binary search.  The first three cases of the if
    # statement screen out lists of length one or two, which means the
    # final case can be written without having to worry about those
    # edge cases.
    def search(self, nums: List[int], target: int) -> int:
        low_idx, high_idx = 0, len(nums)-1
        if (target < nums[low_idx]) or (target > nums[high_idx]):
            return -1
        elif nums[low_idx] == target:
            return low_idx
        elif nums[high_idx] == target:
            return high_idx
        else:
            while high_idx - low_idx > 1:
                current_idx = floor((low_idx + high_idx)/2)
                if nums[current_idx] == target:
                    return current_idx
                elif nums[current_idx] > target:
                    high_idx = current_idx
                else:
                    low_idx = current_idx
            return -1
