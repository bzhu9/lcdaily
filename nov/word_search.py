class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [0, 1, 0, -1, 0]
        def dfs(board, r, c, visited, word, pos):
            if pos == len(word):
                return True
            if r<0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            results = False
            if board[r][c] == word[pos] and (r,c) not in visited:
                visited.add((r,c))
                for i in range(4):
                    results = results or dfs(board, d[i] + r, d[i+1] + c, visited, word, pos + 1)
                visited.remove((r,c))
            return results

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[::-1][0]:
                    if dfs(board, r, c, set(), word[::-1], 0):
                        return True
        return False
