def solution01(money):
    hundred5 = money // 500
    hundred = money % 500 // 100
    fifty = money % 500 % 100 // 50
    ten = money % 500 % 100 % 50 // 10

    count = hundred5 + hundred + fifty + ten

    return count


def solution02(money):
    coin_type = [500, 100, 50, 10]
    count = 0

    for coin in coin_type:
        count += money // coin
        money %= coin

    return count


print(solution01(1270))
