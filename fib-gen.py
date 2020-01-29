def fibonacci_gen(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

s = fibonacci_gen(int(input("Please enter a number: ")))

for _ in s:
    print(_)
