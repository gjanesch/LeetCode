class Solution:
    """
    I tried two different solutions for this.

    The short one was to use the fact that Python treats strings as
    iterables and quickly filter and convert the string to a list with
    a list comprehension, and then just check if the list is the same
    forwards as it is backwards.

    The longer one was a basic two-pointer approach, scanning over the
    string until it either found a mismatch or the pointers were close
    enough that we could say it was a palindrome.

    Interestingly, while the two pointer approach was a bit less memory-
    intensive, the shorter method was quite a bit quicker on the
    testcases.
    """

    PALINDROME_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789")

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        low_idx, high_idx = 0, len(s)-1
        while high_idx > low_idx:
            low_char = s[low_idx]
            high_char = s[high_idx]
            if low_char not in self.PALINDROME_CHARS:
                low_idx = low_idx + 1
            elif high_char not in self.PALINDROME_CHARS:
                high_idx = high_idx - 1
            elif low_char != high_char:
                return False
            else:
                if high_idx - low_idx == 1:
                    return True
                else:
                    low_idx = low_idx+1
                    high_idx = high_idx-1
        return True

        """
        str_list = [c for c in s.lower() if c in self.PALINDROME_CHARS]
        return str_list == str_list[::-1]
        """
