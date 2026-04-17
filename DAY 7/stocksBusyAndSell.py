class Solution:
    def busSellStocks(self,prices:list)->int:
        min_price=prices[0]
        max_profit=0

        for price in range(prices):
            if price<min_price:
                return price
            else:
                max_profit = price-min_price
            return max_profit