class Solution:
    """
    Turns the integer strings in the list into integers, and then looks
    for sequences of two integers and a string to operate on.
    """
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = [t if t in "+-*/" else int(t) for t in tokens]
        idx = 0
        while len(tokens) > 1:
            t1, t2, t3 = tokens[idx], tokens[idx+1], tokens[idx+2]
            if type(t1) == int and type(t2) == int and type(t3) == str:
                if t3 == "+":
                    tokens[idx] = t1 + t2
                elif t3 == "-":
                    tokens[idx] = t1-t2
                elif t3 == "*":
                    tokens[idx] = t1 * t2
                else:
                    tokens[idx] = int(t1 / t2)
                tokens.pop(idx+1)
                tokens.pop(idx+1)
                idx = idx - 1
            else:
                idx = idx + 1
        return tokens[0]
