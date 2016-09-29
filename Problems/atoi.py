import sys
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()
        s = ""
        foundSymbol = False
        firstDigit = False
        for c in A:
            if not foundSymbol and (c == "+" or c == "-"):
                foundSymbol = True
                if c == "-":
                    s += c
            elif c.isdigit() is True:
                firstDigit = True
                s += c
            else:
                break
        if firstDigit is False:
            return 0
        if s[0]!="-" and (len(str(2147483647))<=len(s) and str(2147483647)<s):
            return 2147483647
        elif s[0]=="-" and (len(str(2147483647))<=len(s[1:]) and str(2147483647)<s[1:]):
            return -2147483648
        else:
            return int(s)
sol = Solution()
print sol.atoi("0657730224337W   14621092")