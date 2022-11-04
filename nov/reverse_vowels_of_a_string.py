class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                v.append(s[i])
        out = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                out.append(v.pop())
            else:
                out.append(s[i])
        return "".join(out)
