def how_much_change(coin_denomination_list, coin_quantity_list, value):
    all_coins = []
    for i in coin_denomination_list:
        for g in coin_quantity_list:
            all_coins.append(i)
    print(all_coins)
    coin_list = [] #answer
    for i in coin_quantity_list:
        coin_list.append(0)
    print(coin_list)

    current_value = 0.0

    def count_value():
        current_value = 0.0
        for i in range(len(coin_denomination_list)):
            current_value += coin_denomination_list[i] * coin_list[i]
        return round(current_value, 2)

    maxing_coin = 0
    while current_value != value:
        if current_value < value:
            if coin_list[maxing_coin] < coin_quantity_list[maxing_coin]:
                coin_list[maxing_coin] += 1
                current_value = count_value()
                print(current_value, maxing_coin)
            else:
                maxing_coin += 1
        else:
            coin_list[maxing_coin-1] -= 1
            maxing_coin += 1
            current_value = count_value()
            print(current_value, maxing_coin)
    return coin_list


coin_denomination_list = [0.50, 0.15, 0.10, 0.05]
coin_quantity_list = [20, 20, 5, 3]
value = 6.70

print(how_much_change(coin_denomination_list, coin_quantity_list, value))