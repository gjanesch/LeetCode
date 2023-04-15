class Solution:
    """
    The longest palindrome will be equal in length to the twice number
    of pairs that consist of the same letter (doubled since both
    characters will be in the palindrome) plus an unpaired character if
    there is one.

    So the counter gets counts of the string's characters, and then we
    add twice the number of pairs for each character, and keep track of
    whether we've found any unpaired characters (we only need one, so
    we can short-circuit the logic here).
    """
    def longestPalindrome(self, s: str) -> int:
        string_counter = Counter(s)
        has_odd_character = False
        palindrome_length = 0
        for k, v in string_counter.items():
            palindrome_length = palindrome_length + 2 * (v//2)
            if (not has_odd_character) and v%2 == 1:
                has_odd_character = True
        return palindrome_length + has_odd_character
