class Solution:
    """
    Iterates over the string, appending new characters as appropriate and keeping track of the maximum-length substring seen.

    Some other (better) solutions keep track of just two indices to mark the substring where they're looking instead of trying to continually add to and remove from the a single substring, which might be better.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = ""
        max_len = 0
        for char in s:
            if char in current_substring:
                max_len = max(max_len, len(current_substring))
                current_substring = current_substring[current_substring.index(char)+1:]
            current_substring = current_substring + char
        return max(max_len, len(current_substring))
