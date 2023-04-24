class Solution:
    """
    I kind of just stumbled into this one.  It just tries to keep a
    running total of all values so far, with an adjustment for the case
    where the next value is actually greater than the running sum,
    which happens with some negative cases.
    
    Looking over other solutions/algorithms for this problem, I'm aware
    that this is cumbersome at best (in particular, the second loop may
    be totally redundant).
    """
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        
        max_sum = sum(nums)
        running_sum = 0
        highest_idx = None
        for idx, val in enumerate(nums):
            running_sum = running_sum + val
            if val > running_sum:
                running_sum = val
            if running_sum > max_sum:
                highest_idx = idx
                max_sum = running_sum
        if highest_idx is not None:
            nums = nums[:highest_idx+1]
        
        running_sum = 0
        highest_idx = None
        for idx, val in enumerate(nums[::-1]):
            running_sum = running_sum + val
            if val > running_sum:
                running_sum = val
            if running_sum > max_sum:
                highest_idx = idx
                max_sum = running_sum
        
        return max_sum
