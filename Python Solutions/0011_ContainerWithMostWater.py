class Solution:
    # This solution essentially operated by keeping track of the lowest
    # and highest indices for peaks of equal or greater height, seeing
    # which was farther, calculating the amount of water, and updating
    # the maximum if the current amount is higher.
    # The lowest value is set to 100000 since the problem specification
    # said that the maximum length of the list of peaks was 100000.
    def maxArea(self, height: List[int]) -> int:
        lowest, highest, max_area = 100000, 0, 0

        enumerated_list = list(enumerate(height))
        sorted_list = sorted(enumerated_list, key=lambda x: -x[1])

        for idx, height in sorted_list:
            if idx < lowest:
                lowest = idx
            if idx > highest:
                highest = idx
            current_area = max(idx - lowest, highest - idx) * height
            if current_area > max_area:
                max_area = current_area

        return max_area
