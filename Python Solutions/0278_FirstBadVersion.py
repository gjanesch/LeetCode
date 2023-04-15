class Solution:
    """
    This is essentially just a binary search for the starting point --
    iteratively split the search space until you're down to two values
    and then check whether the lower bound is bad or not (one of the
    two limits has to be the first bad version) and return either it or
    the upper limit.
    """
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            lower = 1
            upper = n
            while upper - lower > 1:
                new_idx = floor((lower+upper)/2)
                if isBadVersion(new_idx):
                    upper = new_idx
                else:
                    lower = new_idx

            if isBadVersion(lower):
                return lower
            else:
                return upper
