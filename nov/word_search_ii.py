class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end = False
class Tree:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        traverse = self.root
        for letter in word:
            if letter not in traverse.children:
                new = Node(letter)
                traverse.children[letter] = new
            traverse = traverse.children[letter]
        traverse.end = True
    
    def search(self, word):
        traverse = self.root
        for letter in word:
            if letter not in traverse.children:
                return False
            traverse = traverse.children[letter]
        return traverse.end
    
    def isValid(self, word):
        traverse = self.root
        for letter in word:
            if letter not in traverse.children:
                return False
            traverse = traverse.children[letter]
        return True

    def delete(self, root, word, depth):
        if depth == len(word):
            if not root.end:
                return False
            root.end = False
            return len(root.children) == 0
        if word[depth] not in root.children:
            return False
        traverse = root.children[word[depth]]
        unique = self.delete(traverse, word, depth + 1)
        if unique:
            del root.children[word[depth]]
            return len(root.children) == 0
        return False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        alpha = Tree()
        for word in words:
            alpha.insert(word)
        found = []

        def dfs(r, c, curr):
            if len(board) > r >= 0 <= c < len(board[0]):
                letter = board[r][c]
                new = curr + letter

                if not alpha.isValid(new):
                    return
                if alpha.search(new):
                    found.append(new)
                    alpha.delete(alpha.root, new, 0)
                board[r][c] = "-1"
                d = [0, -1, 0, 1, 0]
                for i in range(4):
                    dfs(r+d[i], c+d[i+1], new)
                board[r][c] = letter
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                if len(alpha.root.children) > 0:
                    dfs(r,c, "")
        return found
        
