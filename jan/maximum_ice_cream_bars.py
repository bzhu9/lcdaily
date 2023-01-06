class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ind = 0
        while ind < len(costs) and coins >= costs[ind]:
            coins -= costs[ind]
            ind += 1
        return ind
