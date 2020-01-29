# calculate pi to the number of places specified by the user.

# pi = ~3.14
# Nilakantha method

def calc_pi(n):
    p = 3
    sign = 1
    for i in range(2, n, 2):
        p = p + (sign * 4/(i * (i + 1) * (i + 2)))
        sign *= -1
    return p


print(calc_pi(float(input("Please enter a number: "))))
