# 122. Best Time to Buy and Sell Stock II

# Input: prices = [1,2,3,4,5]
# Output: 4

def maxProfit(prices):
    profit = 0
    
    # for each element in prices except the first
    for i in range(1, len(prices)):
        
        # check if the current element is greater than the previous element
        #    6 > 3
        if prices[i] > prices[i-1]:
            
            # add the difference to the profit
            #  profit += 6 - 3 = 3
            profit += prices[i] - prices[i-1]
    return profit



# Here is a more verbose solution that is easier to understand
def maxProfit2(prices):
    # float('inf') is a special value that is greater than any other number
    min_price = float('inf')
    max_profit = 0
    
    for i in range(len(prices)):
        
        # if the current price is less than the minimum price
        #     5 < 7          
        if prices[i] < min_price:
            # min_price is set to the current price
            #   min_price = 5
            min_price = prices[i]
        
        # if the current price minus the minimum price is greater than the maximum profit
        #  6 - 3 > 0
        elif prices[i] - min_price > max_profit:
            # set the maximum profit to the current price minus the minimum price
            # max_profit = 3
            max_profit = prices[i] - min_price 
    return max_profit
        
if __name__ == "__main__":
    prices1 = [7,5,3,6,4,15,20]
    prices2 = [1,2,3,4,5]
    
    print(maxProfit(prices1))
    print(maxProfit(prices2))
    
    print(maxProfit2(prices1))
    print(maxProfit2(prices2))
    
    