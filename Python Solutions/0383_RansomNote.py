class Solution:
    """
    Two solutions were attempted here.

    The first (commented-out) one was to iterate over the ransom note's
    contents, and either remove a matching character, or, if one didn't
    exist, then you knew the result should be false.  If the loop
    completed, then all ransom note characters were in the magazine
    text.

    The second exploits properties of Python's Counter class.
    Subtraction works on matching keys, and anything with a negative or
    zero result is removed.  So by subtracting the magazine contents
    from the ransom contents, the result would be an empty counter if
    the magazine has the necessary characters, and a non-empty counter
    if it didn't.
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        mag = list(magazine)
        for char in ransomNote:
            if char in mag:
                mag.pop(mag.index(char))
            else:
                return False
        return True
        """

        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        if ransom - mag:
            return False
        else:
            return True
