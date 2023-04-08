class Solution:
    """
    I tried this two different ways, though both begin with using
    Counter from the already-imported collections library to tabulate
    the contents of s.

    One method was to just use Counter on t and then compare the other
    Counter.  The other tried to build it one character at a time,
    checking at each step if the current character was actually in s.
    The latter method was a lot slower.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)
        """
        s_dict = Counter(s)
        t_dict = defaultdict(int)
        for char in t:
            if char in s_dict:
                print(char)
                t_dict[char] += 1
            else:
                return False"""

        return s_dict == t_dict
