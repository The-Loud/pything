import random

# Problem 1
def gensquares(n):
    for _ in range(n):
        yield _ ** 2

for _ in gensquares(10):
    print (_)


print("Problem 2")

# Problem 2
def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)

for _ in rand_num(1, 10, 12):
    print(_)

# Problem 3
s = 'hello'
j = iter(s)
print(next(j))
for _ in j:
    print(_)
