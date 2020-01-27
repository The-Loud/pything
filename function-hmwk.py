# Calc the volume of a sphere.

import math
import string


def vol(rad):
    return (4 / 3) * math.pi * (rad ** 3)


print(vol(2))


# Write a function that checks whether a
# number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    if num in range(low, high + 1):
        return num


print(ran_check(5, 6, 7))

# And if you want to return a bool instead:


def ran_bool(num, low, high):
    return num in range(low, high + 1)


print(ran_bool(5, 6, 7))

# Not working


def up_low(s):
    ups = 0
    downs = 0
    for i in s:
        if i.isupper():
            ups += 1
        elif i.islower():
            downs += 1
    print('Number of upper case: ' + str(ups))
    print('Number of upper case: ' + str(downs))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))


def unique_list(lst):
    newlist = []
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    print(newlist)


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


print(multiply([1, 2, 3, -4]))


def palindrome(s):
    return s[::] == s[::-1]


print(palindrome('helleh'))


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))
