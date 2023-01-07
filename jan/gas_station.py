class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        i = 0
        for s in range (len(gas)):
            tank += gas[s] - cost[s]
            if tank < 0:
                tank = 0
                i = s + 1
        return i
