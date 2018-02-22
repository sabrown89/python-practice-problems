from app import maximize_profit

stock_trades = "1 2 100"
mp = maximize_profit.MaximizeProfit(stock_trades)

def test_sell_indexes():
    assert mp.sell_indexes() == [2]

def test_dict_buy_indexes():
    assert mp.dict_sell_buy_indexes() == {2: [0,2]}

def test_maximize_profit():
    assert mp.maximize_profit() == 197
