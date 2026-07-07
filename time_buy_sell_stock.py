prices=[10,8,7,5,2]
#output=0 (prices are decreasing)
prices2=[10,1,5,6,7,1]
#output=6 (buy at 1 sell at 6)


def stock_profit(prices):
    left=0
    right=1
    max_profit=0

    while right<len(prices):
        if prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            max_profit=max(max_profit,profit)
        else:
            left=right
        right+=1
    return max_profit            


print(stock_profit(prices))
print(stock_profit(prices2))

#time=O(n)
#space=O(1)