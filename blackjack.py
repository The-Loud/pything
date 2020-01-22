def blackjack(a, b, c):
    total = a + b + c
    if total <= 21:
        return total
    elif total > 21 and (a == 11 or b == 11 or c == 11):
        return total - 10
    else:
        return 'BUST'


print(str(blackjack(9, 9, 11)))
