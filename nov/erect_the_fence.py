class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p1, p2, p3):
            a = p2[0]-p1[0]
            b = p2[1]-p1[1]
            c = p3[0]-p1[0]
            d = p3[1]-p1[1]
            return a*d - b*c
        
        def hull (points):
            stack = []
            for p in points:
                while len(stack) > 1 and cross(stack[-2], stack[-1], p) > 0:
                    stack.pop()
                stack.append(tuple(p))
            return stack
        trees.sort()
        return list(set(hull(trees) + hull(trees[::-1])))
