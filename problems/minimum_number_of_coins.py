def minimum_number_of_coins(amount):
    coins = 0
    split_amount = str(amount).split('.')
    dollars = 0
    if len(split_amount) > 1:
        dollars = int(split_amount[0])
    cents = int(split_amount[1])
    pennies = cents % 10
    penny_amount = pennies - 5
    if penny_amount < 0:
        coins += pennies
    else:
        coins += penny_amount
    cents = cents - coins
    nickels = cents % 25
    if nickels % 10 != 0:
        coins += 1
        cents = cents - 5
    dimes = int(cents % 25 / 10)
    coins += dimes
    cents = cents - (dimes * 10)
    coins += int(cents / 25)

    coins += int(dollars / 25 * 100)
    return coins

