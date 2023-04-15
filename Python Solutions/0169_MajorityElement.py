class Solution:
    """
    Two different solutions were attempted, both pretty brief.  The
    first just returns the most common element from a counter, while
    the second relies on the fact that any element that appears more
    than floor(len(nums)/2) times has to be in the middle element(s),
    so you can just sort and check that.
    """
    def majorityElement(self, nums: List[int]) -> int:
        """
        return Counter(nums).most_common(1)[0][0]
        """

        return sorted(nums)[len(nums)//2]
