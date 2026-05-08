"""
买卖股票的最佳时机
核心思想
一次遍历，记录左边的最低价格，计算当前卖出能赚多少
维护一个 min_price：到目前为止最便宜的价格
每一天都算：今天卖能赚多少 = 今天价格 - min_price
记录最大的那个利润
"""


from typing import List

class Solution:
    def maxProfit(self,prices:List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for price in prices:                ### 直接遍历全部数组，不要用if判断每个大小
            max_profit=max(max_profit,price-min_price)
            min_price=min(price,min_price)
        return max_profit


if __name__=="__main__":
    prices=[7,1,5,3,6,4]
    #prices=[7,6,4,3,1]
    s=Solution()
    print(s.maxProfit(prices))
