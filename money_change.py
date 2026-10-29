def change(money):
    num_coins = 0
    denominations = [10, 5, 1]

    while money > 0:
        # Choose the largest coin that fits the remaining amount.
        for coin in denominations:
            if coin <= money:
                money = money - coin
                num_coins = num_coins + 1
                # Start again from the largest denomination.
                break

    return num_coins


print(change(28))
