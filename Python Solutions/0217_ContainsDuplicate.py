class Solution:
    # A pretty blunt solution -- since set() effectively produces a
    # deduplicated listing of the elements, just see if the length of
    # the set is less than that of the original list.
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
