class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = [""]
        for letter in s:
            if a[-1] == letter:
                a.pop()
            else:
                a.append(letter)
        return "".join(a)
