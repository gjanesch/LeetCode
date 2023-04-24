class Solution:
    """
    Tried two separate methods.
    
    One was just directly converting the strings to integers, adding
    them, and then converting back, on the grounds that Python's 
    arbitrary-size integers should handle anything LeetCode throws at
    it.
    
    The second just handled one place at a time, and built the string
    accordingly.  This one was actually quite a bit slower.
    """
    def addBinary(self, a: str, b: str) -> str:
        #return format(int(a, 2) + int(b, 2), "b")
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        print(a, b)

        output = ""
        carry = False
        for i in range(max_len-1, -1, -1):
            if carry:
                if a[i] == b[i]:
                    output = "1" + output
                    carry = a[i] == "1"
                else:
                    output = "0" + output
                    carry = True
            else:
                if a[i] == b[i]:
                    output = "0" + output
                    carry = a[i] == "1"
                else:
                    output = "1" + output
                    carry = False
            print(i, output, carry)
        
        if carry:
            output = "1" + output
        return output
