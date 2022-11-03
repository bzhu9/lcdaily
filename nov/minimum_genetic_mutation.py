class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = {start}
        q = deque([[start,0]])
        while len(q) > 0:
            curr, l = q.popleft()
            if curr == end:
                return l
            for i in range (len(curr)):
                for c in "ACGT":
                    # print (curr[:i] + c + curr[i+1:])
                    if curr[:i] + c + curr[i+1:] not in visited and curr[:i] + c + curr[i+1:] in bank:
                        visited.add(curr[:i] + c + curr[i+1:])
                        q.append([curr[:i] + c + curr[i+1:], l+1])
        return -1

