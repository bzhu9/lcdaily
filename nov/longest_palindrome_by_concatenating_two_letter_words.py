class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        count = 0
        doubles = {}
        for word in words:
            if word[0] == word[1]:
                if word in doubles:
                    del doubles[word]
                else:
                    doubles[word] = 1
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        for word in d:
            if word[0] == word[1]:
                count += d[word]//2
            elif word[::-1] in d:
                count += min(d[word], d[word[::-1]])
                d[word] = 0
        return (2*count + 1) * 2 if len(doubles) > 0 else 4*count
