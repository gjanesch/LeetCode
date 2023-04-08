class Solution:
    # Uses a list as a stack.  As we iterate over characters, the left-
    # hand ones get added when they appear in a string and removed if
    # they match the next right-hand character.  At the end, we need to
    # check if the list is empty, since something like "()[" would
    # complete the for loop but isn't actually valid.
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            #print(stack)
            if char in "({[":
                stack.append(char)
            elif len(stack) > 0:
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return stack == []
