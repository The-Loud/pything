# Problem 1

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print('Cannot multiply strings!')

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('Who divides by zero kek')
finally:
    print('This runs anyway')

def ask():
    while True:
        try:
            inp = int(input('Input an integer: '))
        except:
            print('That\'s not an integer!')
            continue
        else:
            break
    print(f'Thank you, your number squared is: {inp ** 2}')

ask()
