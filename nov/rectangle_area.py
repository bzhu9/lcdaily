class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if bx1 > ax2 or ax1 > bx2 or by1 > ay2 or ay1 > by2:
            return (ax2-ax1) * (ay2 - ay1) + (bx2-bx1) * (by2 - by1)
        total = (ax2-ax1) * (ay2 - ay1) + (bx2-bx1) * (by2 - by1)
        width = 0
        height = 0
        if bx1 >= ax1 and bx1 <= ax2 and bx2 > ax2:
            width = ax2 - bx1
        elif ax1 >= bx1 and ax1 <= bx2 and ax2 > bx2:
            width = bx2 - ax1
        else:
            width = min(ax2 - ax1, bx2 - bx1)

        if by2 >= ay1 and by2 <= ay2 and by1 < ay1:
            height = by2 - ay1
        elif ay2 >= by1 and ay2 <= by2 and ay1 < by1:
            height = ay2 - by1
        else:
            height = min(ay2 - ay1, by2 - by1)

        if ax1 >= bx1 and ax2 <= bx2 and ay1 >= by1 and ay2 <= by2:
            return (bx2-bx1) * (by2 - by1)
        if bx1 >= ax1 and bx2 <= ax2 and by1 >= ay1 and by2 <= ay2:
            return (ax2-ax1) * (ay2 - ay1)

        return total - width*height
