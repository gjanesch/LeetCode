class Solution:
    """
    Sort the numbers, then while the current number is non-positive, do
    a two-pointer pass through the remainder of the array to find all
    pairs.

    This solution is slow according to LeetCode, but I can't figure out
    why since some faster solutions don't appear very different.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        solutions = []
        while i < (len(nums)-1) and nums[i] <= 0:
            a = i+1
            b = len(nums)-1
            target = -nums[i]
            while a < b:
                if nums[a] + nums[b] > target:
                    b = b - 1
                elif nums[a] + nums[b] < target:
                    a = a + 1
                else:
                    new_solution = [nums[i], nums[a], nums[b]]
                    if new_solution not in solutions:
                        solutions.append(new_solution)
                    a = a + 1
                    b = b - 1
                    while a<b and nums[a] == nums[a-1]:
                        a = a+1
                    while a<b and b < len(nums)-1 and nums[b] == nums[b+1]:
                        b = b+1
            i = i + 1
        return solutions
