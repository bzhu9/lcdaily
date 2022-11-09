class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        count = 1
        while self.prices and self.prices[-1][1] <= price:
            count += self.prices.pop()[0]
        self.prices.append((count, price))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
