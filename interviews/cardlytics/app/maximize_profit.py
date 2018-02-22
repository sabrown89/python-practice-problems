class MaximizeProfit():
    def __init__(self, stock_trades):
        self.stock_trades = stock_trades

    def maximize_profit(self):
        profit = []
        if max(self.stock_trades) == self.stock_trades[0]
        for sell_index, buy_list in self.dict_sell_buy_indexes().items():
            sell_price = self.slist()[sell_index]
            buy_prices = []
            for buy_index in range(buy_list[0], buy_list[1]):
                buy_prices.append(self.slist()[buy_index])
            for buy_price in buy_prices:
                profit.append(sell_price - buy_price)
        return sum(profit)

    def slist(self):
        list_of_strings = self.stock_trades.split(' ')
        return [int(num) for num in list_of_strings]

    def sell_indexes(self):
        length = len(self.slist()) - 1
        sell_indexes = []
        for num in range(0, length):
            if self.slist()[num] > self.slist()[num + 1]:
                sell_indexes.append(num)
            elif self.slist()[num + 1] > self.slist()[num] and self.slist()[num + 1] == self.slist()[-1]:
                sell_indexes.append(num + 1)
        return sell_indexes

    def dict_sell_buy_indexes(self):
        stock_data = {}
        for i,v in enumerate(self.sell_indexes()):
            if i == 0:
                stock_data[v] = [i,v]
            else:
                last_sell_index = self.sell_indexes()[i-1]
                stock_data[v] = [last_sell_index + 1, v]
        return stock_data
