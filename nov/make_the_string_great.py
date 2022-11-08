class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            print(i, len(s))
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                s = s[:i] + s[i+2:]
                i -= 2
            i += 1 if i != -2 else 2
        return s
