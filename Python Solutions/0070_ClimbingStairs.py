from math import factorial, floor

class Solution:
    # This solution is a bit of a cheat.  Because Python has arbitrary-
    # size integers, calculating factorials directly is feasable, at
    # least up to 2000! in a quick check (for comparison, 21! is too
    # large for a normal 64-bit integer).  The problem says we don't
    # have to worry about more than 45 steps, so we'll never need to
    # calculate anything bigger than 45!, and therefore we can just
    # calculate the number of permutations directly.
    def climbStairs(self, n: int) -> int:
        max_two_steps = floor(n/2)
        possibilities = 0
        for x in range(max_two_steps+1):
            possibilities = possibilities + self.permutations(n-2*x, x)
        return possibilities

    def permutations(self, n_1: int, n_2: int) -> int:
        return int(factorial(n_1 + n_2)/(factorial(n_1) * factorial(n_2)))
