class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k != 1 or len(s) == 1:
            return "".join(sorted(s))
        l = []
        for i in range(len(s)):
            l.append(s)
            s = s[1:] + s[0]
        return sorted(l)[0]
