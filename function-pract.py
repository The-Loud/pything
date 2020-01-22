# Warmup

# problem 3


def makes_twenty(a, b):
    return (a+b) == 20 or a == 20 or b == 20


# almost there
def almost_there(num):
    return (abs(num) >= 90 and abs(num) <= 110) or (abs(num) >= 190 and abs(num) <= 210)


print(almost_there(int(input('enter a number '))))


# part 2
# numlist [3,4,5,1,3,3]

def has_33(*args):
    for i in args:
        if i == 3 and i + 1 == 3:
            print(args)
            return True


print(has_33(2, 3, 3, 4))
