 from bisect import bisect_left

class Solution:
    # I did this after the first two sum problem (#0001), and seeing
    # what was theoretically quite good there, but I didn't just want
    # to copy that.  Unfortunately, the best alternative I could think
    # of was just a tweaked version of the solution I had to #0001,
    # using the bisect_left function to give me the index for where to
    # look for the matching value (even though that's not quite what the
    # function is intended for) if the current number and the needed
    # value don't match.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for idx, n in enumerate(numbers):
            desired_number = target - n
            if n == desired_number:
                if numbers[idx-1] == n:
                    return [idx, idx+1]
                elif numbers[idx+1] == n:
                    return [idx+1, idx+2]
            else:
                desired_idx = bisect_left(numbers, desired_number)
                if desired_idx < l and numbers[desired_idx] == desired_number:
                    return [idx+1, desired_idx+1]
        return None
