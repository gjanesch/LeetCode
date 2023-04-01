class Solution:
    # This is actually a more proper solution than my first one, which I
    # coded up after seeing the first one do badly and getting a hint on
    # a better solution.
    # This code loops over the list in the following way:
    # 1. Start with easily-overridden values for the min and max (in
    #    retrospect, calculating the max and min are wasteful when Inf
    #    and 0 could have been used instead).
    # 2. If the current point is a new minimum, set it to the current
    #    minimum and reset the high value.
    # 3. If the current point is a new high, calculate the profit using
    #    this and the current minimum, and if it's higher than the
    #    current best_profit, set it to that.
    def maxProfit(self, prices: List[int]) -> int:
        max_possible = max(prices)
        min_possible = min(prices)
        best_profit, current_low, current_high = 0, max_possible, min_possible
        for p in prices:
            if p < current_low:
                current_low = p
                current_high = min_possible
            elif p > current_high:
                current_high = p
                if current_high - current_low > best_profit:
                    best_profit = current_high - current_low
        return best_profit
