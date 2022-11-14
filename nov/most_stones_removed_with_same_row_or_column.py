class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # use union find -> total - #sets
        visited = set()
        componentNum = 0
        rows = {}
        columns = {}
        for x, y in stones:
            if x not in rows:
                rows[x] = []
            if y not in columns:
                columns[y] = []
            rows[x].append((x,y))
            columns[y].append((x,y))
        for x, y in stones:
            if (x,y) not in visited:
                componentNum += 1
                q = deque([(x,y)])
                while q:
                    i,j = q.popleft()
                    if (i,j) not in visited:
                        for r,c in rows[i]:
                            q.append((r,c))
                        for r,c in columns[j]:
                            q.append((r,c))
                    visited.add((i,j))
        return len(stones) - componentNum
